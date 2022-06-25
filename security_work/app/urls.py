from django.urls import path
from .views import user_lk, homepage, add_organisation, admin_lk


urlpatterns = [
    path('lk/', user_lk, name='lk'),
    path('addOrganisation/', add_organisation),
    path('', homepage),
    path('lk_admin/', admin_lk, name='lk_admin')
]
