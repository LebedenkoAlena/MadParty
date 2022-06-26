from django.contrib.auth.mixins import LoginRequiredMixin
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

from fpdf import FPDF


def passport_to_pdf(org):
    pdf = FPDF()
    pdf.add_font('Sans', style='', fname='static/font/DejaVuSans.ttf',
                 uni=True)
    pdf.set_font("Sans", size=12)
    pdf.add_page()
    data = serializers.serialize("python", [org])[0]["fields"]
    col_width = pdf.w / 1.1
    row_height = pdf.font_size * 1.5
    for key, value in data.items():
        if value is True:
            value = 'Да'
        if value is False:
            value = 'Нет'
        if key == 'is_risk_valuation_done' or key == 'is_valuation_done':
            d = {"YES": "Да", "NO": "Нет", "PARTIALLY": "Частично"}
            value = d.get(value, '')
        pdf.multi_cell(col_width, row_height,
                       txt=str(org._meta.get_field(key).verbose_name),
                       border=1)
        pdf.multi_cell(col_width, row_height,
                       txt=str(value), border=1)
        pdf.ln(row_height)
    pdf.output(f'{org.id}.pdf')


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
        return render(request, 'organizations/add_organisation.html',
                      context=data)


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
