from django.urls import path
from .views import *


urlpatterns = [
    path('', accounts, name='accounts'),
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('signup/', Signup, name='signup'),
    path('profile/', profile, name='profile'),
    path('edit-profile/', EditProfile, name='edit profile'),
    path('forget-password/', ForgetPassword, name='forget-password'),
    path('reset-password/<str:token>', ResetPassword, name='reset-password'),
]