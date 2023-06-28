from django.urls import path
from _help.views import Contact

urlpatterns = [
    path('', Contact, name='contact')
]
