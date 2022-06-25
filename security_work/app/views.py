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
from fpdf import FPDF


def PassportToPDF(Org):
    #TODO Сделать поля на русском и выбрать место/способо сохранения файла
    pdf = FPDF()
    pdf.set_font("Arial", size=12)
    pdf.add_page()
    data = serializers.serialize("python", [Org])[0]["fields"]
    col_width = pdf.w / 2.5
    row_height = pdf.font_size * 3
    for key, value in data.items():
        pdf.cell(col_width, row_height,
                 txt=str(key), border=1)
        pdf.cell(col_width, row_height,
                 txt=str(value), border=1)
        pdf.ln(row_height)
    pdf.output('simple_table.pdf')


def user_lk(request):
    if not request.user.is_authenticated:
        return redirect('/')

    user = request.user
    organisations = Organisation.objects.filter(user_id=user.id).all()
    return render(request, "lk.html", {
        "organisations": serializers.serialize("python", organisations)
    })


def admin_lk(request):
    context = {}
    users = User.objects.all()
    for user in users:
        context['users'] = context.get('users', []) + [[user,
                                                        serializers.serialize(
                                                            'python',
                                                            Organisation.objects.filter(
                                                                user_id=user.id))]]
    return render(request, 'lk_admin.html', context)


def homepage(request):
    return render(request, "homepage.html")


# TODO возможность загрузить файлы для каждого поля
def add_organisation(request):
    form = OrganisationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('/lk/')

    return render(request, "add_organisation.html", {
        'form': form
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
        return render(request, 'add_organisation.html', context=data)

    # def post(self, request):
    #     data = {"org_form": OrganisationForm}
    #     return render(request, '', context=data)
