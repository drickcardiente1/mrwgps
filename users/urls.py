from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', include('social_django.urls', namespace='social')),
    # socials close form
    path("close/", views.close, name="close"),
    # home
    path('', views.home, name='home'),
    # manual login
    path('login/', views.log_in_view, name='login'),
    # manual login submit proccess
    path('login_proccess/', views.log_in_proccess, name='login_proccess'),
    # forgot-password proccess
    path('forgot_password/', views.forgot_password_proccess, name='forgot_password'),
    # forgot-password proccess
    path('newpwd_confirmation/', views.forgot_password_confirm_proccess, name='newpwd_confirmation'),
    # logout
    path("logout/", views.signout, name='logout'),
    # signup manual
    path('signup/', views.sign_up_view, name='signup'),
    path('submit_register/', views.submit_register, name='submit_register'),
    path('send_otpregistration/', views.action_otpsendregistration, name='send_otpregistration'),
    # check users status
    path('user_stats', views.user_stats, name='user_stats'),
    path('home_stats', views.home_stats, name='home_stats'),
]