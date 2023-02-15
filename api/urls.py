from django.urls import path, include
from api import views

app_name = "api"


urlpatterns = [
    # ex: api/user/login/
    path("otp/", views.OTPView.as_view(), name="OTP"),
    path("login/", views.LoginView.as_view(), name="Login"),
    path("register/", views.RegisterView.as_view(), name="Register"),
    path("reset/sendotp/", views.OTPViewForgotPassword.as_view(), name="reset_user_password"),
    path("reset/password/", views.PasswordResetView.as_view(), name="reset_user_password"),

    # social
    path('currentUser/', views.CurrentUser.as_view(), name="current"),
]
