from django import forms
from .models import Organisation


class OrganisationForm(forms.ModelForm):
    class Meta:
        model = Organisation
        fields = '__all__'
        exclude = ['gold_sign', 'gold_sign_date',
                   'valuatied_workplace_percent',
                   'workers_on_danger_positions_percent',
                   'average_percent_provided_coveralls',
                   'average_percent_provided_disinfectants',
                   'percent_of_workers_with_medical_brief',
                   'persnt_of_educated']


