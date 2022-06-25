from django.urls import path
from .views import user_lk, homepage


urlpatterns = [
    path('lk/', user_lk, name='lk'),
    path('', homepage)
]
