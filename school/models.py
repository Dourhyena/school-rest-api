from django.db import models
from django.conf import settings

# Create your models here.

class StudentProfile(models.Model):
    teacher = models.OneToOneField(settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE)
    roll_no = models.CharField(max_length = 100)
    grade = models.PositiveIntegerField()
    section = models.CharField(max_length = 1)

    # class Meta:
    #     default_permissions = ('add',)
    #     permissions = (('can_view_own_profile', 'Can view own profile'))

class TeacherProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits = 6, decimal_places = 2)
    subject = models.CharField(max_length = 100)
    students = models.ManyToManyField('StudentProfile', related_name = 'student')

        # class Meta:
        #     default_permissions = ('add',)
        #     permissions = (('can_add_students', 'Can Add Students'),
        #                     ('can_list_students', 'Can list students'))
