from django.shortcuts import render, redirect
from django.core import serializers
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import View

from .forms import (GeneralOrgForm, OccupationSafetyForm,
                    ProfessionalRiskForm,
                    WorkingConditionsForm,
                    IndustrialInjuriesForm, CommonDataForm,
                    LaborProtectionTrainingForm,
                    CollectiveAgreementForm, OrganisationForm)
from django.contrib.auth.decorators import login_required
from .models import Organisation



def user_lk(request):
    if not request.user.is_authenticated:
        return redirect('/')

    if request.user.is_superuser:
        context = {}
        users = User.objects.all()
        for user in users:
            context['users'] = context.get('users', []) + [[user,
                                                            serializers.serialize(
                                                                'python',
                                                                Organisation.objects.filter(
                                                                    user_id=user.id))]]
        return render(request, 'lk_admin.html', context)
    else:
        user = request.user
        organisations = Organisation.objects.filter(user_id=user.id).all()
        return render(request, "lk.html", {
            "organisations": serializers.serialize("python", organisations)
        })


def homepage(request):
    return render(request, "homepage.html")


def add_organisation(request):
    form = OrganisationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            org = form.save()
            Organisation.objects.get(id=org.id).calculate_percents()
            return redirect('/lk/')

    return render(request, "organizations/add_organization.html", {
        'forms': [GeneralOrgForm,
                  OccupationSafetyForm,
                  ProfessionalRiskForm,
                  WorkingConditionsForm,
                  IndustrialInjuriesForm,
                  CommonDataForm,
                  LaborProtectionTrainingForm,
                  CollectiveAgreementForm]
    })


# TODO Сделать редактирование
@login_required
class PassportOrgView(View):
    login_url = reverse_lazy('login')
    redirect_field_name = 'login'
    model = Organisation

    def get(self, request):
        data = {'org_forms': [GeneralOrgForm,
                              OccupationSafetyForm,
                              ProfessionalRiskForm,
                              WorkingConditionsForm,
                              IndustrialInjuriesForm,
                              CommonDataForm,
                              LaborProtectionTrainingForm,
                              CollectiveAgreementForm]}
        return render(request, 'organizations/add_organisation.html',
                      context=data)


@login_required
class GeneralOrgView(View):
    login_url = reverse_lazy('login')
    redirect_field_name = 'login'
    model = Organisation

    def post(self, request, id):
        data = {'form': GeneralOrgForm}
        return render(request, 'organizations/add_organisation.html',
                      context=data)


@login_required
class OccupationSafetyView(View):
    login_url = reverse_lazy('login')
    redirect_field_name = 'login'
    model = Organisation

    def post(self, request, id):
        data = {'form': OccupationSafetyForm}
        return render(request, 'organizations/add_organisation.html',
                      context=data)


@login_required
class ProfessionalRiskView(View):
    login_url = reverse_lazy('login')
    redirect_field_name = 'login'
    model = Organisation

    def post(self, request, id):
        data = {'form': ProfessionalRiskForm}
        return render(request, 'organizations/add_organisation.html',
                      context=data)


@login_required
class WorkingConditionsView(View):
    login_url = reverse_lazy('login')
    redirect_field_name = 'login'
    model = Organisation

    def post(self, request, id):
        data = {'form': WorkingConditionsForm}
        return render(request, 'organizations/add_organisation.html',
                      context=data)


@login_required
class IndustrialInjuriesView(View):
    login_url = reverse_lazy('login')
    redirect_field_name = 'login'
    model = Organisation

    def post(self, request, id):
        data = {'form': IndustrialInjuriesForm}
        return render(request, 'organizations/add_organisation.html',
                      context=data)


@login_required
class CommonDataView(View):
    login_url = reverse_lazy('login')
    redirect_field_name = 'login'
    model = Organisation

    def post(self, request, id):
        data = {'form': CommonDataForm}
        return render(request, 'organizations/add_organisation.html',
                      context=data)


@login_required
class LaborProtectionTrainingView(View):
    login_url = reverse_lazy('login')
    redirect_field_name = 'login'
    model = Organisation

    def post(self, request, id):
        data = {'form': LaborProtectionTrainingForm}
        return render(request, 'organizations/add_organisation.html',
                      context=data)


@login_required
class CollectiveAgreementView(View):
    login_url = reverse_lazy('login')
    redirect_field_name = 'login'
    model = Organisation

    def post(self, request, id):
        data = {'form': CollectiveAgreementForm}
        return render(request, 'organizations/add_organisation.html',
                      context=data)
