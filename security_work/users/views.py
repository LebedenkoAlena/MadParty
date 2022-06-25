from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic import FormView, View
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserCreateForm, UserLoginForm
from django.contrib.auth import get_user_model, login

User = get_user_model()


def create_user(request):
    form = UserCreateForm(request.POST or None)
    context = dict()

    if request.user.is_active:
        return redirect("/")

    if request.method == "POST":
        if form.is_valid():
            form.non_field_errors()
            if User.objects.get(email=form.cleaned_data["email"]):
                form.add_error("__all__", "Пользователь с такой почтной уже существует.")
            else:
                user = form.save(commit=False)
                user.set_password(form.cleaned_data["password1"])
                user.save()
                login(request, user)
                return redirect("/")

    context["form"] = form
    return render(request, template_name="users/register.html", context=context)


class UserLoginView(LoginView):
    form_class = UserLoginForm
    authentication_form = UserLoginForm
    success_url = '/'
    template_name = 'users/login.html'
    redirect_authenticated_user = True


class LogoutView(LogoutView):
    next_page = reverse_lazy("login")
