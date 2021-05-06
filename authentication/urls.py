from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.LoginAuthView.as_view(), name='loginMe'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('password-change/', views.CustomPasswordChangeView.as_view(), name='pass_change'),
    path('password-reset/', views.ForgetPasswordView.as_view(), name='pass_reset'),
    path('password-reset-done/', views.pass_reset_done, name='password_done'),
    path('set-password/<uidb64>/<token>/', views.SetNewPassword.as_view(), name='set_new_pass'),
    path('logout/', views.logoutMe, name='logoutMe')
]
