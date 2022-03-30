from django.urls import path, include
from management import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [

    # Used to signup as a teacher or a student
    path('signup/', views.SignUpView.as_view(), name = 'signup'),

    # Used to obtain refresh and access token
    path('login/access/', views.MyTokenObtainPairView.as_view(), name = 'access-token'),

    # Used to obtain access token from refresh token
    path('login/refresh/', jwt_views.TokenRefreshView.as_view(), name='token-refresh'),

    # Used to reset password if forgotten
    path('login/changepassword/', views.ChangePasswordView.as_view(), name='reset-password')

]
