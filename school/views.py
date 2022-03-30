from django.shortcuts import render
from rest_framework import generics
from .models import StudentProfile, TeacherProfile
from .serializers import StudentProfileSerializer, TeacherProfileSerializer
from .permissions import IsStudent, IsTeacher
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

class StudentsRetrieveViewSet(generics.RetrieveAPIView):

    """An endpoint to get a student's particular details"""

    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer
    permission_classes = [IsAuthenticated, IsStudent]

class StudentCreateListViewSet(generics.ListCreateAPIView):

    """An endpoint for teachers adn super users to create and list students"""
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer
    permission_classes = [IsAuthenticated, IsTeacher | IsAdminUser]


class TeacherCreateListViewSet(generics.ListCreateAPIView):

    """An endpoint for Super Users to create and view Teacher"""
    queryset = TeacherProfile.objects.all()
    serializer_class = TeacherProfileSerializer
    permission_classes = [IsAdminUser]
