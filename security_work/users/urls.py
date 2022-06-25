from django.urls import path
from .views import UserLoginView, LogoutView, create_user

urlpatterns = [
    path('signup/', create_user, name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
