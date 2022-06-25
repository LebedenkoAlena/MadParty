from django.shortcuts import render, redirect
from django.views.generic import FormView, View
from .forms import CreateUserForm, UserLoginForm
from django.contrib.auth import get_user_model, logout, login

User = get_user_model()


def signup(request):
    template_name = 'users/register.html'
    form = CreateUserForm(request.POST or None)
    form_error = ''
    if request.method == 'POST':
        if form.is_valid():
            if not User.objects.filter(email=form.cleaned_data['email']):
                form.save()
                return redirect('')
            else:
                form_error = f'Почта {form.cleaned_data["email"]} уже используется'
    context = {'form': form, 'form_error': form_error}
    return render(request, template_name, context)


class LoginView(FormView):
    form_class = UserLoginForm
    success_url = '/'
    template_name = 'users/login.html'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super().form_valid(form)


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('/')
