from django.urls import path
from .views import user_lk, homepage, add_organisation


urlpatterns = [
    path('lk/', user_lk, name='lk'),
    path('addOrganisation/', add_organisation),
    path('', homepage),
]
