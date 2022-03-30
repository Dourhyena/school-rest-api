from django.urls import path, include
from school import views


urlpatterns = [

    # Used to retrieve own details of student
    path('student/<int:pk>/', views.StudentsRetrieveViewSet.as_view(), name = 'student-view'),

    # Used to create and list students
    path('teacher/', views.StudentCreateListViewSet.as_view(), name='teacher-view'),

    # Used to create and list teachers
    path('superuser/', views.TeacherCreateListViewSet.as_view(), name='superuser-view'),

]
