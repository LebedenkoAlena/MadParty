from django.db import models


# Create your models here.
class Organisation(models.Model):
    """
    Class, that contains passport of Organisation
    """

    # General
    opf = models.CharField(max_length=100, verbose_name="ОПФ", null=True, blank=False)
    name = models.CharField(max_length=100, verbose_name="Название/имя", null=True, blank=False)
    short_name = models.CharField(max_length=100, verbose_name="Краткое название/имя", null=True, blank=False)
    legal_address = models.CharField(max_length=100, verbose_name="Юридический адрес", null=True, blank=False)
    fact_address = models.CharField(max_length=100, verbose_name="Фактический адрес", null=True, blank=False)
    leader_name = models.CharField(max_length=100, verbose_name="ФИО руководителя", null=True, blank=False)
    inn = models.CharField(max_length=100, verbose_name="ИНН", null=True, blank=False)
    oktmo = models.CharField(max_length=100, verbose_name="ОКТМО", null=True, blank=False)
    activity_type = models.CharField(max_length=100, verbose_name="Вид деятельности", null=True, blank=False)
    empoyers_number = models.CharField(max_length=100, verbose_name="Численность работников", null=True, blank=False)
    leader_phone = models.CharField(max_length=50, verbose_name="Телефон руководителя", null=True, blank=False)
    official_email = models.EmailField(max_length=254, verbose_name="E-mail официальный")
    name_safety_specialist = models.CharField(max_length=50, verbose_name="ФИО специалиста по охране труда", null=True, blank=False)
    specialist_phone = models.CharField(max_length=50, verbose_name="Телефон специалиста по охране труда", null=True, blank=False)
    specialist_email = models.EmailField(max_length=254, verbose_name="E-mail официальный")
    gold_sign = models.BooleanField(verbose_name="Золотой знак")
    gold_sign_date = models.DateField(verbose_name="Дата получение золотого знака")
    # Common data
    normative_act = models.BooleanField(verbose_name="Наличие локального нормативного акта", null=True)
    committee = models.BooleanField(verbose_name="Наличие комитета (комиссии) по охране труда", null=True)
    count_security_workers = models.IntegerField(verbose_name="Наличие уполномоченных (доверенных) лиц по охране труда", null=True)
    agreement_of_security_work = models.BooleanField(verbose_name="Наличие соглашения по охране труда в организации", null=True)
    cabinet_of_security_work = models.BooleanField(verbose_name="Наличие кабинета (уголка) охраны труда", null=True)
    cabinet_of_first_aid = models.BooleanField(verbose_name="Наличие помещения для оказания медицинской помощи", null=True)
    plan_of_upgrade_workers_conditions = models.BooleanField(verbose_name="Наличие плана мероприятий по улучшению и оздоровлению условий труда", null=True)
    financing_plan = models.IntegerField(verbose_name="Объем финансирования плана мероприятий по улучшению и оздоровлению условий труда (тыс. руб.)", null=True)
    programm_of_saving_aid_of_workers = models.BooleanField(verbose_name="Наличие корпоративной программы сохранения здоровья работников", null=True)


    # Occupation safety valuation
    is_valuation_done = models.CharField(max_length=50, verbose_name="Специальная оценка проведена", null=True, blank=False)
    report_date = models.DateField(verbose_name="Дата отчета")
    report_number = models.CharField(max_length=50, verbose_name="Номер отчета", null=True, blank=False)
    workplace_number = models.PositiveBigIntegerField(verbose_name="Всего рабочих мест")
    workplace_number_with_valuation = models.PositiveBigIntegerField(verbose_name="Всего рабочих мест")
    valuatied_workplace_percent = models.CharField(max_length=50, verbose_name="Процент рабочих мест, охваченых СОУТ", null=True, blank=False)
    class1_workplace_number = models.PositiveBigIntegerField(verbose_name="Всего рабочих мест с условием труда 1 класса")
    class1_workers_number = models.PositiveBigIntegerField(verbose_name="Всего человек, работающих на рабочих местах с условием труда 1 класса")
    class2_workplace_number = models.PositiveBigIntegerField(verbose_name="Всего рабочих мест с условием труда 2 класса")
    class2_workers_number = models.PositiveBigIntegerField(verbose_name="Всего человек, работающих на рабочих местах с условием труда 2 класса")
    class31_workplace_number = models.PositiveBigIntegerField(verbose_name="Всего рабочих мест с условием труда 3.1 класса")
    class31_workers_number = models.PositiveBigIntegerField(verbose_name="Всего человек, работающих на рабочих местах с условием труда 3.1 класса")
    class32_workplace_number = models.PositiveBigIntegerField(verbose_name="Всего рабочих мест с условием труда 3.2 класса")
    class32_workers_number = models.PositiveBigIntegerField(verbose_name="Всего человек, работающих на рабочих местах с условием труда 3.2 класса")
    class33_workplace_number = models.PositiveBigIntegerField(verbose_name="Всего рабочих мест с условием труда 3.3 класса")
    class33_workers_number = models.PositiveBigIntegerField(verbose_name="Всего человек, работающих на рабочих местах с условием труда 3.3 класса")
    class34_workplace_number = models.PositiveBigIntegerField(verbose_name="Всего рабочих мест с условием труда 3.4 класса")
    class34_workers_number = models.PositiveBigIntegerField(verbose_name="Всего человек, работающих на рабочих местах с условием труда 3.4 класса")
    class4_workplace_number = models.PositiveBigIntegerField(verbose_name="Всего рабочих мест с условием труда 4 класса")
    class4_workers_number = models.PositiveBigIntegerField(verbose_name="Всего человек, работающих на рабочих местах с условием труда 4 класса")
    workers_on_danger_positions_percent = models.CharField(max_length=50, verbose_name="Процент рабочих на опасных местах", null=True, blank=False)

    # Professional risks control
    is_risk_valuation_done = models.CharField(max_length=50, verbose_name="Оценка проф. рисков проведена", null=True, blank=False)
    risk_valuation_date = models.DateField(verbose_name="Дата последней проверки проф. рисков")

    # Working conditions
    workers_number_with_free_coveralls = models.PositiveBigIntegerField(verbose_name="Всего человек, бесплатно получающих СИЗ")
    average_percent_provided_coveralls = models.CharField(max_length=50, verbose_name="Средний процент обеспеченности работников СИЗ", null=True, blank=False)
    workers_number_with_free_disinfectants = models.PositiveBigIntegerField(verbose_name="Всего человек, бесплатно получающих обеззараживающие средства")
    average_percent_provided_disinfectants = models.CharField(max_length=50, verbose_name="Средний процент обеспеченности работников обеззараживающими средствами", null=True, blank=False)
    workers_number_with_medical_brief = models.PositiveBigIntegerField(verbose_name="Всего человек, прошедищих мед. осмотры")
    percent_of_workers_with_medical_brief = models.CharField(max_length=50, verbose_name="Процент работников, прошедщих мед. осмотры", null=True, blank=False)

    # Industrial injuries
    number_of_died_workers = models.PositiveBigIntegerField(verbose_name="Всего человек, погибших на производстве")
    died_workers_info = models.TextField(verbose_name="Информация о погибших работниках (дата, должность, возраст)")
    number_of_hard_injury = models.PositiveBigIntegerField(verbose_name="Всего человек, получивших тяжелые травмы на производстве")
    hard_injured_workers_info = models.TextField(verbose_name="Информация о работниках, получивших тяжелые травмы (дата, должность, возраст)")
    number_of_group_accidents = models.PositiveBigIntegerField(
        verbose_name="Всего групповых несчастных случаев")
    group_accidents_info = models.TextField(
        verbose_name="Информация о групповых несчастных случаях (дата, должность, возраст)")
    number_of_light_injury = models.PositiveBigIntegerField(
        verbose_name="Всего человек, получивших легкие травмы на производстве")
    light_injured_workers_info = models.TextField(
        verbose_name="Информация о работниках, получивших легкие травмы (дата, должность, возраст)")
    number_of_micro_injury = models.PositiveBigIntegerField(
        verbose_name="Всего человек, получивших микротравмы на производстве")
    micro_injured_workers_info = models.TextField(
        verbose_name="Информация о работниках, получивших микротравмы (дата, должность, возраст)")

    # Collective agreement
    trade_union_organisation = models.BooleanField(verbose_name="Наличие профсоюзной организации")
    collective_agreement = models.PositiveBigIntegerField(verbose_name="Наличие коллективного договора")
    change_agreement = models.PositiveBigIntegerField(verbose_name="Изменения в колдоговор")

    # Labor protection training
    count_of_workers = models.IntegerField(verbose_name="Количество работников, которые должны проходить обучение по охране труда", null=True)
    persnt_of_educated = models.IntegerField(verbose_name="% фактически прошедших такое обучение", null=True)
    timely_passage = models.BooleanField(verbose_name="Своевременное проведение инструктажей по охране труда", null=True)
