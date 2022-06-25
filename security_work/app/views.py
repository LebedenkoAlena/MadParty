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

    user = request.user
    organisations = Organisation.objects.filter(user_id=user.id).all()
    print(organisations)
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
