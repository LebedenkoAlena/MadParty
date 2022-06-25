from django.contrib import admin
from .models import Organisation


# Register your models here.
class AdminOrganisation(admin.ModelAdmin):
    class Meta:
        model = Organisation


admin.site.register(Organisation, AdminOrganisation)
