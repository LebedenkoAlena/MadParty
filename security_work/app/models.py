from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


User = get_user_model()


class Organisation(models.Model):
    """
    Class, that contains passport of Organisation
    """
    user_id = models.ForeignKey(default=None, verbose_name='Пользователь', to=User, related_name='user', on_delete=models.SET_NULL, null=True)

    ANSWER_CHOICES = [
        ("YES", "Да"),
        ("NO", "Нет"),
        ("PARTIALLY", "Частично"),
    ]

    # General
    opf = models.TextField(verbose_name="ОПФ", null=True, blank=True)
    name = models.TextField(verbose_name="Название/имя", null=True, blank=True)
    short_name = models.TextField(verbose_name="Краткое название/имя", null=True, blank=True)
    address = models.TextField(verbose_name="Юридический адрес", null=True, blank=True)
    fact_address = models.TextField(verbose_name="Фактический адрес", null=True, blank=True)
    leader_name = models.TextField(verbose_name="ФИО руководителя и должность", null=True, blank=True)
    inn = models.CharField(max_length=100, verbose_name="ИНН", null=True, blank=True)
    oktmo = models.CharField(max_length=100, verbose_name="ОКТМО", null=True, blank=True)
    activity_type = models.TextField(verbose_name="Вид деятельности", null=True, blank=True)
    workers_number = models.IntegerField(verbose_name="Численность работников", null=True, blank=True)
    leader_phone = models.CharField(max_length=50, verbose_name="Телефон руководителя", null=True, blank=True)
    official_email = models.EmailField(verbose_name="E-mail официальный", null=True, blank=True)
    name_safety_specialist = models.TextField(verbose_name="ФИО специалиста по охране труда", null=True, blank=True)
    specialist_phone = models.CharField(max_length=50, verbose_name="Телефон специалиста по охране труда", null=True, blank=True)
    specialist_email = models.EmailField(verbose_name="E-mail официальный", null=True, blank=True)
    gold_sign = models.BooleanField(verbose_name="Золотой знак", null=True, blank=True)
    gold_sign_date = models.DateField(verbose_name="Дата получение золотого знака", null=True, blank=True)

    # Occupation safety valuation
    is_valuation_done = models.CharField(max_length=50, verbose_name="Специальная оценка проведена", choices=ANSWER_CHOICES, null=True, blank=True)
    report_date = models.DateField(verbose_name="Дата отчета", default=timezone.now, blank=True, null=True)
    report_number = models.CharField(max_length=50, verbose_name="Номер отчета", null=True, blank=True)
    workplace_number = models.IntegerField(verbose_name="Всего рабочих мест", null=True, blank=True)
    workplace_number_with_valuation = models.IntegerField(verbose_name="Количество рабочих мест, на которых проведена СОУТ", null=True, blank=True)
    valuated_workplace_percent = models.CharField(max_length=50, verbose_name="Процент рабочих мест, охваченых СОУТ", null=True, blank=True)
    class1_workplace_number = models.IntegerField(verbose_name="Всего рабочих мест с условием труда 1 класса", null=True, blank=True)
    class1_workers_number = models.IntegerField(verbose_name="Всего человек, работающих на рабочих местах с условием труда 1 класса", null=True, blank=True)
    class2_workplace_number = models.IntegerField(verbose_name="Всего рабочих мест с условием труда 2 класса", null=True, blank=True)
    class2_workers_number = models.IntegerField(verbose_name="Всего человек, работающих на рабочих местах с условием труда 2 класса", null=True, blank=True)
    class31_workplace_number = models.IntegerField(verbose_name="Всего рабочих мест с условием труда 3.1 класса", null=True, blank=True)
    class31_workers_number = models.IntegerField(verbose_name="Всего человек, работающих на рабочих местах с условием труда 3.1 класса", null=True, blank=True)
    class32_workplace_number = models.IntegerField(verbose_name="Всего рабочих мест с условием труда 3.2 класса", null=True, blank=True)
    class32_workers_number = models.IntegerField(verbose_name="Всего человек, работающих на рабочих местах с условием труда 3.2 класса", null=True, blank=True)
    class33_workplace_number = models.IntegerField(verbose_name="Всего рабочих мест с условием труда 3.3 класса", null=True, blank=True)
    class33_workers_number = models.IntegerField(verbose_name="Всего человек, работающих на рабочих местах с условием труда 3.3 класса", null=True, blank=True)
    class34_workplace_number = models.IntegerField(verbose_name="Всего рабочих мест с условием труда 3.4 класса", null=True, blank=True)
    class34_workers_number = models.IntegerField(verbose_name="Всего человек, работающих на рабочих местах с условием труда 3.4 класса", null=True, blank=True)
    class4_workplace_number = models.IntegerField(verbose_name="Всего рабочих мест с условием труда 4 класса", null=True, blank=True)
    class4_workers_number = models.IntegerField(verbose_name="Всего человек, работающих на рабочих местах с условием труда 4 класса", null=True, blank=True)
    workers_on_danger_positions_percent = models.CharField(max_length=50, verbose_name="Процент рабочих на опасных местах", null=True, blank=True)

    # Professional risks control
    is_risk_valuation_done = models.CharField(max_length=50, choices=ANSWER_CHOICES, verbose_name="Оценка проф. рисков проведена", null=True, blank=True)
    risk_valuation_date = models.DateField(verbose_name="Дата последней проверки проф. рисков", null=True, blank=True)

    # Working conditions
    workers_number_with_free_coveralls = models.IntegerField(verbose_name="Всего человек, бесплатно получающих СИЗ", null=True, blank=True)
    average_percent_provided_coveralls = models.CharField(max_length=50, verbose_name="Средний процент обеспеченности работников СИЗ", null=True, blank=True)
    workers_number_with_free_disinfectants = models.IntegerField(verbose_name="Всего человек, бесплатно получающих обеззараживающие средства", null=True, blank=True)
    average_percent_provided_disinfectants = models.CharField(max_length=50, verbose_name="Средний процент обеспеченности работников обеззараживающими средствами", null=True, blank=True)
    workers_number_with_medical_brief = models.IntegerField(verbose_name="Всего человек, прошедищих мед. осмотры", null=True, blank=True)
    percent_of_workers_with_medical_brief = models.CharField(max_length=50, verbose_name="Процент работников, прошедщих мед. осмотры", null=True, blank=True)

    # Industrial injuries
    number_of_died_workers = models.IntegerField(verbose_name="Всего человек, погибших на производстве", null=True, blank=True)
    died_workers_info = models.TextField(verbose_name="Информация о погибших работниках (дата, должность, возраст)", null=True, blank=True)
    number_of_hard_injury = models.IntegerField(verbose_name="Всего человек, получивших тяжелые травмы на производстве", null=True, blank=True)
    hard_injured_workers_info = models.TextField(verbose_name="Информация о работниках, получивших тяжелые травмы (дата, должность, возраст)", null=True, blank=True)
    number_of_group_accidents = models.IntegerField(
        verbose_name="Всего групповых несчастных случаев", null=True, blank=True)
    group_accidents_info = models.TextField(
        verbose_name="Информация о групповых несчастных случаях (дата, должность, возраст)", null=True, blank=True)
    number_of_light_injury = models.IntegerField(
        verbose_name="Всего человек, получивших легкие травмы на производстве", null=True, blank=True)
    light_injured_workers_info = models.TextField(
        verbose_name="Информация о работниках, получивших легкие травмы (дата, должность, возраст)", null=True, blank=True)
    number_of_micro_injury = models.IntegerField(
        verbose_name="Всего человек, получивших микротравмы на производстве", null=True, blank=True)
    micro_injured_workers_info = models.TextField(
        verbose_name="Информация о работниках, получивших микротравмы (дата, должность, возраст)", null=True, blank=True)

    # Common data
    normative_act = models.BooleanField(verbose_name="Наличие локального нормативного акта", null=True, blank=True)
    committee = models.BooleanField(verbose_name="Наличие комитета (комиссии) по охране труда", null=True, blank=True)
    count_security_workers = models.IntegerField(verbose_name="Наличие уполномоченных (доверенных) лиц по охране труда", null=True, blank=True)
    agreement_of_security_work = models.BooleanField(verbose_name="Наличие соглашения по охране труда в организации", null=True, blank=True)
    cabinet_of_security_work = models.BooleanField(verbose_name="Наличие кабинета (уголка) охраны труда", null=True, blank=True)
    cabinet_of_first_aid = models.BooleanField(verbose_name="Наличие помещения для оказания медицинской помощи", null=True, blank=True)
    plan_of_upgrade_workers_conditions = models.BooleanField(verbose_name="Наличие плана мероприятий по улучшению и оздоровлению условий труда", null=True, blank=True)
    financing_plan = models.IntegerField(verbose_name="Объем финансирования плана мероприятий по улучшению и оздоровлению условий труда (тыс. руб.)", null=True, blank=True)
    program_of_saving_aid_of_workers = models.BooleanField(verbose_name="Наличие корпоративной программы сохранения здоровья работников", null=True, blank=True)

    # Labor protection training
    count_of_workers = models.IntegerField(verbose_name="Количество работников, которые должны проходить обучение по охране труда", null=True, blank=True)
    percent_of_educated = models.CharField(max_length=50, verbose_name="% фактически прошедших такое обучение", null=True, blank=True)
    timely_passage = models.BooleanField(verbose_name="Своевременное проведение инструктажей по охране труда", null=True, blank=True)

    # Collective agreement
    trade_union_organisation = models.BooleanField(verbose_name="Наличие профсоюзной организации", null=True, blank=True)
    collective_agreement = models.TextField(verbose_name="Наличие коллективного договора", null=True, blank=True)
    change_agreement = models.TextField(verbose_name="Изменения в колдоговор", null=True, blank=True)
