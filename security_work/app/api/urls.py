from django.urls import path

from .views import PassportAPIView

urlpatterns = [
    path('passport/edit/', PassportAPIView.as_view(), name='passport_edit'),
]
