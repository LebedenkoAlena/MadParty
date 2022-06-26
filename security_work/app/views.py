from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
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
from .models import Organisation
import datetime as dt


@login_required
def accept_gold_sign(request, org_id):
    if request.user.is_superuser:
        organisation = Organisation.objects.get(pk=org_id).first()
        organisation.gold_sign = "CONFIRMED"
        organisation.gold_sign_date = dt.date.today()
        organisation.save()


@login_required
def reject_gold_sign(request, org_id):
    if request.user.is_superuser:
        organisation = Organisation.objects.get(pk=org_id).first()
        organisation.gold_sign = "MISSING"
        organisation.gold_sign_date = None
        organisation.save()


@login_required
def ask_for_a_gold_sign(request, org_id):
    organisation = Organisation.objects.get(pk=org_id).first()
    if request.user.id == organisation.user_id:
        organisation.gold_sign = "UNDER_CONSIDERATION"
        organisation.gold_sign_date = None
        organisation.save()


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

class PassportOrgView(LoginRequiredMixin, View):
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


class GeneralOrgView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    redirect_field_name = 'login'
    model = Organisation

    def post(self, request, id):
        data = {'form': GeneralOrgForm}
        form = GeneralOrgForm(request.POST or None)
        if form.is_valid():
            org = Organisation.objects.get(id=id)
            for k, v in form.cleaned_data.items():
                eval(f"org.{k} = {v}")
            org.save()
            return HttpResponse("OK")


class OccupationSafetyView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    redirect_field_name = 'login'
    model = Organisation

    def post(self, request, id):
        data = {'form': OccupationSafetyForm}
        return render(request, 'organizations/add_organisation.html',
                      context=data)


class ProfessionalRiskView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    redirect_field_name = 'login'
    model = Organisation

    def post(self, request, id):
        data = {'form': ProfessionalRiskForm}
        return render(request, 'organizations/add_organisation.html',
                      context=data)


class WorkingConditionsView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    redirect_field_name = 'login'
    model = Organisation

    def post(self, request, id):
        data = {'form': WorkingConditionsForm}
        return render(request, 'organizations/add_organisation.html',
                      context=data)


class IndustrialInjuriesView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    redirect_field_name = 'login'
    model = Organisation

    def post(self, request, id):
        data = {'form': IndustrialInjuriesForm}
        return render(request, 'organizations/add_organisation.html',
                      context=data)


class CommonDataView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    redirect_field_name = 'login'
    model = Organisation

    def post(self, request, id):
        data = {'form': CommonDataForm}
        return render(request, 'organizations/add_organisation.html',
                      context=data)


class LaborProtectionTrainingView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    redirect_field_name = 'login'
    model = Organisation

    def post(self, request, id):
        data = {'form': LaborProtectionTrainingForm}
        return render(request, 'organizations/add_organisation.html',
                      context=data)


class CollectiveAgreementView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    redirect_field_name = 'login'
    model = Organisation

    def post(self, request, id):
        data = {'form': CollectiveAgreementForm}
        return render(request, 'organizations/add_organisation.html',
                      context=data)
