from django.urls import path
from .views import UserLoginView, Logout

from .views import signup

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]
