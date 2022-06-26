from django.urls import path
from .views import user_lk, homepage, add_organisation

urlpatterns = [
    path('lk/', user_lk, name='lk'),
    path('organizations/add/', add_organisation),
    path('', homepage),
]
urlpatterns += [eval(f"path('addOrganisation/{i}', add_organisation)") for i
                in range(8)]
