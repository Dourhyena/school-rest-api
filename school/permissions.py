from rest_framework import permissions

class IsStudent(permissions.BasePermission):

    message = 'Cannot view details of other students'

    def has_object_permission(self, request, view, obj):

        """Check student is trying to view their own profile"""
        return obj.id == request.user.id

class IsTeacher(permissions.BasePermission):

    message = 'Not logged in as a teacher'
    def has_permission(self, request, view):

        """Check teacher is trying to add or view student"""
        return request.user.groups.filter(name='teacher').count() == 1
