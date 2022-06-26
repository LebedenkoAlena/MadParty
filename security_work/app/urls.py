from django.urls import path
from . import views

urlpatterns = [
    path('lk/', views.user_lk, name='lk'),
    path('organizations/add/', views.add_organisation),
    path('', views.homepage),
    path('lk_admin/', views.admin_lk, name='lk_admin')
]
