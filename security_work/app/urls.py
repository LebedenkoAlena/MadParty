from django.urls import path
from .views import user_lk


urlpatterns = [
    path('lk/', user_lk, name='lk'),
]
