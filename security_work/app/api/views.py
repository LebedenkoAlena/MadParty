from django.http import FileResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers as rest_serializers, viewsets
from django.shortcuts import get_object_or_404
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer
from ..models import Organisation
from django.core import serializers

from fpdf import FPDF


class PassportAPIView(APIView):
    def get(self, request, *args, **kwargs):
        data = [{'id': 1, "name": "Valera"}, {'id': 2, "name": "Anton"}]
        return Response(data)


class OrganisationSerializer(rest_serializers.HyperlinkedModelSerializer):
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
                  'specialist_email',
                  'is_valuation_done',
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
                  'class4_workers_number',
                  'is_risk_valuation_done',
                  'risk_valuation_date',
                  'workers_number_with_free_coveralls',
                  'workers_number_with_free_disinfectants',
                  'workers_number_with_medical_brief',
                  'number_of_died_workers',
                  'died_workers_info',
                  'number_of_hard_injury',
                  'hard_injured_workers_info',
                  'number_of_group_accidents',
                  'group_accidents_info',
                  'number_of_light_injury',
                  'light_injured_workers_info',
                  'number_of_micro_injury',
                  'micro_injured_workers_info',
                  'normative_act',
                  'committee',
                  'count_security_workers',
                  'agreement_of_security_work',
                  'cabinet_of_security_work',
                  'cabinet_of_first_aid',
                  'plan_of_upgrade_workers_conditions',
                  'financing_plan',
                  'program_of_saving_aid_of_workers',
                  'count_of_workers',
                  'timely_passage',
                  'trade_union_organisation',
                  'collective_agreement',
                  'change_agreement']


class OrganisationViewSet(viewsets.ViewSet):
    parser_classes = (XMLParser,)
    renderer_classes = (XMLRenderer,)

    def retrieve(self, request, pk=None):
        queryset = Organisation.objects.all()
        organisation = get_object_or_404(queryset, pk=pk)
        serializer = OrganisationSerializer(organisation)
        return Response(serializer.data)


class OrganisationPDFAPI(APIView):
    def get(self, request, pk=None):
        queryset = Organisation.objects.all()
        org = get_object_or_404(queryset, pk=pk)

        pdf = FPDF()
        pdf.add_font('Sans', style='', fname='static/font/DejaVuSans.ttf',
                     uni=True)
        pdf.set_font("Sans", size=12)
        pdf.add_page()
        data = serializers.serialize("python", [org])[0]["fields"]
        col_width = pdf.w / 1.1
        row_height = pdf.font_size * 1.5
        for key, value in data.items():
            if value is True:
                value = 'Да'
            if value is False:
                value = 'Нет'
            if key == 'is_risk_valuation_done' or key == 'is_valuation_done':
                d = {"YES": "Да", "NO": "Нет", "PARTIALLY": "Частично"}
                value = d.get(value, '')
            pdf.multi_cell(col_width, row_height,
                           txt=str(org._meta.get_field(key).verbose_name),
                           border=1)
            pdf.multi_cell(col_width, row_height,
                           txt=str(value), border=1)
            pdf.ln(row_height)
        pdf.output(f'{org.id}.pdf')

        return FileResponse(open(f'{org.id}.pdf', 'rb'), content_type='application/pdf')
