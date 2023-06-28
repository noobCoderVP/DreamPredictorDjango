from django.urls import path

from _predictor.views import Predictor

urlpatterns = [
    path('', Predictor, name='predictor'),
]
