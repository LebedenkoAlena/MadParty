from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .models import Organisation


# Create your views here.
def user_lk(request):
    if not request.user.is_authenticated:
        return redirect('/')

    user = request.user
    organisations = Organisation.objects.filter(user_id=user.id)

    return render(request, "lk.html", {
        "organisations": organisations
    })
