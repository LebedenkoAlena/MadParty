from django.shortcuts import render, redirect
from django.core import serializers
from .forms import OrganisationForm
from .models import Organisation
from django.contrib.auth.models import User


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
        context['users'] = context.get('users', []) + [[user, serializers.serialize('python', Organisation.objects.filter(user_id=user.id))]]
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
