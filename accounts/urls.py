from django.urls import path
from .views import *


urlpatterns = [
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('signup/', Signup, name='signup'),
    path('profile/', profile, name='profile'),
    path('edit-profile/', EditProfile, name='edit profile'),
]