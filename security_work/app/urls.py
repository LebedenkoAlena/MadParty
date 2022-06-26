from django.urls import path
from .views import user_lk, homepage, add_organisation
from .views import (GeneralOrgView, OccupationSafetyView, ProfessionalRiskView,
                    WorkingConditionsView, IndustrialInjuriesView,
                    CommonDataView, LaborProtectionTrainingView,
                    CollectiveAgreementView)

VIEW_LIST = [GeneralOrgView, OccupationSafetyView, ProfessionalRiskView,
             WorkingConditionsView, IndustrialInjuriesView,
             CommonDataView, LaborProtectionTrainingView,
             CollectiveAgreementView]
urlpatterns = [
    path('profile/', user_lk, name='lk'),
    path('organizations/add/', add_organisation),
    path('', homepage),
]
# urlpatterns += [
#     eval(f"path('organization/edit/{i}', {VIEW_LIST[i]}.as_view())") for i
#     in range(8)]
