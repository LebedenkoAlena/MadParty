from django.shortcuts import render, redirect
from .models import Organisation
from django.core import serializers


# Create your views here.
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
