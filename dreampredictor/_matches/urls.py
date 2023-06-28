from django.urls import path

from _matches.views import Matches

urlpatterns = [
    path('', Matches, name='matches'),
]
