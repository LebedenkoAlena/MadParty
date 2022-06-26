from django.urls import path

from .views import PassportAPIView, OrganisationViewSet, OrganisationPDFAPI


urlpatterns = [
    path('passport/edit/', PassportAPIView.as_view(), name='passport_edit'),
    path('xml/<int:pk>', OrganisationViewSet.as_view({'get': 'retrieve'}), name="org-xml"),
    path('pdf/<int:pk>', OrganisationPDFAPI.as_view(), name="org-pdf")
]
