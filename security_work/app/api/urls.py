from django.urls import path

from .views import PassportAPIView
from .views import OrganisationViewSet


urlpatterns = [
    path('passport/edit/', PassportAPIView.as_view(), name='passport_edit'),
    path('xml/<int:pk>', OrganisationViewSet.as_view({'get': 'retrieve'}))
]
