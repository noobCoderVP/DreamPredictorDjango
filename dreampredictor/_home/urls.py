from django.urls import path

from _home.views import Home, Login, Register, Test, Profile, Logout

urlpatterns = [
    path('', Home, name='home'),
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('register/', Register, name='register'),
    path('profile/', Profile, name='profile'),
    path('test/', Test, name='Test')
]
