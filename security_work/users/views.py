from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic import FormView, View
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from .forms import UserCreateForm, UserLoginForm
from security_work.app.forms import (GeneralOrgForm, OccupationSafetyForm,
                                     ProfessionalRiskForm,
                                     WorkingConditionsForm,
                                     IndustrialInjuriesForm, CommonDataForm,
                                     LaborProtectionTrainingForm,
                                     CollectiveAgreementForm, OrganisationForm)
from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from security_work.app.models import Organisation

User = get_user_model()


def create_user(request):
    form = UserCreateForm(request.POST or None)
    context = dict()

    if request.user.is_active:
        return redirect("/")

    if request.method == "POST":
        if form.is_valid():
            form.non_field_errors()
            if User.objects.filter(email=form.cleaned_data["email"]):
                form.add_error("__all__",
                               "Пользователь с такой почтой уже существует.")
            else:
                user = form.save(commit=False)
                user.set_password(form.cleaned_data["password1"])
                user.save()
                login(request, user)
                return redirect("/")

    context["form"] = form
    return render(request, template_name="users/register.html",
                  context=context)


class UserLoginView(LoginView):
    form_class = UserLoginForm
    authentication_form = UserLoginForm
    success_url = '/'
    template_name = 'users/login.html'
    redirect_authenticated_user = True


class LogoutView(LogoutView):
    next_page = reverse_lazy("login")


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
