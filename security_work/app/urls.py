from django.urls import path
from .views import user_lk, homepage, edit_organization, create_organization
from .views import (GeneralOrgView, OccupationSafetyView, ProfessionalRiskView,
                    WorkingConditionsView, IndustrialInjuriesView,
                    CommonDataView, LaborProtectionTrainingView,
                    CollectiveAgreementView)

VIEW_LIST = ['GeneralOrgView', 'OccupationSafetyView', 'ProfessionalRiskView',
             'WorkingConditionsView', 'IndustrialInjuriesView',
             'CommonDataView', 'LaborProtectionTrainingView',
             'CollectiveAgreementView']
urlpatterns = [
    path('profile/', user_lk, name='profile'),
    path('organizations/edit/<int:pk>/', edit_organization, name="org-edit"),
    path('organizations/create/', create_organization, name="org-create"),
    path('', homepage),
]
urlpatterns += [eval(
    f"path('organization/edit/<int:pk>/{i}', {VIEW_LIST[i]}.as_view())")
    for i in range(8)]
