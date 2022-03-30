from rest_framework import serializers
from django.contrib.auth.models import User, Group, Permission
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.contenttypes.models import ContentType
from school.models import TeacherProfile, StudentProfile


class SignUpSerializer(serializers.ModelSerializer):

    """Serializer for registering"""

    # Users can register as a teacher or a student.
    choices = [
        ('teacher'),
        ('student')
    ]
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    role = serializers.ChoiceField(choices, write_only = True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])


    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name', 'role')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def create_group_and_assign(self, user, groupname):

        # Creates group if not present
        group, created = Group.objects.get_or_create(name = groupname)
        if created:
            if group.name == 'teacher':
                teacher_ct = ContentType.objects.get_for_model(TeacherProfile)

                # Creates appropriate permissions for Teachers
                add_permission = Permission.objects.create(
                codename='can_add_students', name='Can add students', content_type=teacher_ct)
                list_permission = Permission.objects.create(codename='can_list_students',
                name='Can list students', content_type=teacher_ct)

                # Adds the permissions to the newly created group
                group.permissions.add(add_permission, list_permission)

            elif group.name == 'student':
                teacher_ct = ContentType.objects.get_for_model(StudentProfile)

                # Creates appropriate permissions for Students
                view_permission =  Permission.objects.create(codename='can_view_profile',
                name='Can view profile', content_type=teacher_ct)

                # Adds the permissions to the newly created group
                group.permissions.add(view_permission)

        # Adds user to the group
        user.groups.add(group)



    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )


        user.set_password(validated_data['password'])
        user.save()



        groupname = self.validated_data['role']
        self.create_group_and_assign(user, groupname)

        return user

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    """Serializer for obtaining JWT Tokens"""

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        data['id'] = self.user.id
        return data

class ChangePasswordSerializer(serializers.Serializer):

    """Serializer for reset password endpoint"""
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
