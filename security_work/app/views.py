from django.shortcuts import render, redirect
from django.core import serializers
from .forms import OrganisationForm
from .models import Organisation


def user_lk(request):
    if not request.user.is_authenticated:
        return redirect('/')

    user = request.user
    organisations = Organisation.objects.filter(user_id=user.id)

    return render(request, "lk.html", {
        "organisations": serializers.serialize("python", organisations)
    })


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
