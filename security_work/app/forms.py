from django import forms
from .models import Organisation


class SubAttrsFormMixin(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"placeholder": field.label, "name": name})


class OrganisationForm(forms.ModelForm):
    class Meta:
        model = Organisation
        fields = '__all__'
        exclude = [
                   'gold_sign',
                   'gold_sign_date',
                   'valuated_workplace_percent',
                   'workers_on_danger_positions_percent',
                   'average_percent_provided_coveralls',
                   'average_percent_provided_disinfectants',
                   'percent_of_workers_with_medical_brief',
                   'percent_of_educated']


class GeneralOrgForm(forms.ModelForm):

    @property
    def title(self):
        return "Общие сведения"

    class Meta:
        model = Organisation
        fields = ['opf',
                  'name',
                  'short_name',
                  'address',
                  'fact_address',
                  'leader_name',
                  'inn',
                  'oktmo',
                  'activity_type',
                  'workers_number',
                  'leader_phone',
                  'official_email',
                  'name_safety_specialist',
                  'specialist_phone',
                  'specialist_email']


class OccupationSafetyForm(forms.ModelForm):

    @property
    def title(self):
        return "Специальная оценка условий труда (СОУТ)"

    class Meta:
        model = Organisation
        fields = ['is_valuation_done',
                  'report_date',
                  'report_number',
                  'workplace_number',
                  'workplace_number_with_valuation',
                  'class1_workplace_number',
                  'class1_workers_number',
                  'class2_workplace_number',
                  'class2_workers_number',
                  'class31_workplace_number',
                  'class31_workers_number',
                  'class32_workplace_number',
                  'class32_workers_number',
                  'class33_workplace_number',
                  'class33_workers_number',
                  'class34_workplace_number',
                  'class34_workers_number',
                  'class4_workplace_number',
                  'class4_workers_number']


class ProfessionalRiskForm(forms.ModelForm):

    @property
    def title(self):
        return "Управление профрисками"

    class Meta:
        model = Organisation
        fields = ['is_risk_valuation_done',
                  'risk_valuation_date']


class WorkingConditionsForm(forms.ModelForm):

    @property
    def title(self):
        return "Условия труда"

    class Meta:
        model = Organisation
        fields = ['workers_number_with_free_coveralls',
                  'workers_number_with_free_disinfectants',
                  'workers_number_with_medical_brief']


class IndustrialInjuriesForm(forms.ModelForm):

    @property
    def title(self):
        return "Производственный травматизм"

    class Meta:
        model = Organisation
        fields = ['number_of_died_workers',
                  'died_workers_info',
                  'number_of_hard_injury',
                  'hard_injured_workers_info',
                  'number_of_group_accidents',
                  'group_accidents_info',
                  'number_of_light_injury',
                  'light_injured_workers_info',
                  'number_of_micro_injury',
                  'micro_injured_workers_info']


class CommonDataForm(forms.ModelForm):

    @property
    def title(self):
        return "Общие данные"

    class Meta:
        model = Organisation
        fields = ['normative_act',
                  'committee',
                  'count_security_workers',
                  'agreement_of_security_work',
                  'cabinet_of_security_work',
                  'cabinet_of_first_aid',
                  'plan_of_upgrade_workers_conditions',
                  'financing_plan',
                  'program_of_saving_aid_of_workers']


class LaborProtectionTrainingForm(forms.ModelForm):

    @property
    def title(self):
        return "Обучение по охране труда"

    class Meta:
        model = Organisation
        fields = ['count_of_workers',
                  'timely_passage']


class CollectiveAgreementForm(forms.ModelForm):

    @property
    def title(self):
        return "Коллективный договор"

    class Meta:
        model = Organisation
        fields = ['trade_union_organisation',
                  'collective_agreement',
                  'change_agreement']
