from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


User = get_user_model()


def instances_count():
    return f"Новая организация ({Organisation.objects.count()})"


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

    GOLD_SIGN_CHOICES = [
        ("CONFIRMED", "Подтвержен"),
        ("MISSING", "Отсутсвует"),
        ("UNDER_CONSIDERATION", "На рассмотрении")
    ]

    # General
    opf = models.CharField(max_length=150, verbose_name="Наименование ОПФ юрлица", null=True, blank=True)
    name = models.CharField(max_length=250, verbose_name="Полное наименование организации (для ИП - ФИО)", null=True, blank=True)
    short_name = models.CharField(max_length=250, verbose_name="Краткое наименование организации", default=instances_count)
    address = models.CharField(max_length=500, verbose_name="Юридический адрес", null=True, blank=True)
    fact_address = models.CharField(max_length=500, verbose_name="Фактический адрес", null=True, blank=True)
    leader_name = models.CharField(max_length=250, verbose_name="ФИО руководителя и должность", null=True, blank=True)
    inn = models.CharField(max_length=100, verbose_name="ИНН", null=True, blank=True)
    oktmo = models.CharField(max_length=100, verbose_name="ОКТМО", null=True, blank=True)
    activity_type = models.CharField(max_length=250, verbose_name="Основной вид деятельности по ОКВЭД", null=True, blank=True)
    workers_number = models.IntegerField(verbose_name="Среднесписочная численность работников на дату проведения мониторинга — Ч (с указанием мужчин - М, женщин - Ж)", null=True, blank=True)
    leader_phone = models.CharField(max_length=50, verbose_name="Телефон руководителя", null=True, blank=True)
    official_email = models.EmailField(verbose_name="E-mail руководителя официальный", null=True, blank=True)
    name_safety_specialist = models.CharField(max_length=250, verbose_name="ФИО и должность специалиста по охране труда или ответственного за охрану труда", null=True, blank=True)
    specialist_phone = models.CharField(max_length=50, verbose_name="Телефон специалиста по охране труда", null=True, blank=True)
    specialist_email = models.EmailField(verbose_name="E-mail специалиста по охране труда официальный", null=True, blank=True)
    gold_sign = models.CharField(max_length=50, verbose_name="Золотой знак", choices=GOLD_SIGN_CHOICES, default="MISSING")
    gold_sign_date = models.DateField(verbose_name="Дата получение золотого знака", null=True, blank=True)

    # Occupation safety valuation
    is_valuation_done = models.CharField(max_length=50, verbose_name="Специальная оценка проведена", choices=ANSWER_CHOICES, null=True, blank=True)
    report_date = models.DateField(verbose_name="Дата внесения отчета СОУТ", default=timezone.now, blank=True, null=True)
    report_number = models.CharField(max_length=50, verbose_name="Номер отчета во ФГИС СОУТ", null=True, blank=True)
    workplace_number = models.IntegerField(verbose_name="Всего рабочих мест в организации", null=True, blank=True)
    workplace_number_with_valuation = models.IntegerField(verbose_name="Количество рабочих мест, на которых проведена СОУТ", null=True, blank=True)
    valuated_workplace_percent = models.CharField(max_length=50, verbose_name="% рабочих мест, охваченых СОУТ", null=True, blank=True)
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
    workers_on_danger_positions_percent = models.CharField(max_length=50, verbose_name="% рабочих на опасных местах", null=True, blank=True)

    """@property
    def valuated_workplace_percent(self):
        return self.workplace_number_with_valuation / self.workplace_number * 100

    @property
    def workers_on_danger_positions_percent(self):
        return self.class4_workers_number / self.workplace_number  * 100"""


    # Professional risks control
    is_risk_valuation_done = models.CharField(max_length=50, choices=ANSWER_CHOICES, verbose_name="Проведена оценка профессиональных рисков в области охраны труда", null=True, blank=True)
    risk_valuation_date = models.DateField(verbose_name="Дата проведения последней оценки профессиональных рисков", null=True, blank=True)

    # Working conditions
    workers_number_with_free_coveralls = models.IntegerField(verbose_name="Численность работников, получающих бесплатно спецодежду, спецобувь и другие средства индивидуальной защиты (СИЗ)– всего:", null=True, blank=True)
    average_percent_provided_coveralls = models.CharField(max_length=50, verbose_name="Средний % обеспеченности работников СИЗ", null=True, blank=True)
    workers_number_with_free_disinfectants = models.IntegerField(verbose_name="Численность работников, получающих бесплатно смывающие и обезвреживающие средства – всего:", null=True, blank=True)
    average_percent_provided_disinfectants = models.CharField(max_length=50, verbose_name="Средний % обеспечения работников смывающими средствами", null=True, blank=True)
    workers_number_with_medical_brief = models.IntegerField(verbose_name="Количество работников, подлежащих обязательным предварительным и периодическим медицинским осмотрам", null=True, blank=True)
    percent_of_workers_with_medical_brief = models.CharField(max_length=50, verbose_name="% работников, прошедших обязательные предварительные и периодические медицинские осмотры", null=True, blank=True)

    """@property
    def average_percent_provided_coveralls(self):
        return self.workers_number_with_free_coveralls / self.workplace_number  * 100

    @property
    def average_percent_provided_disinfectants(self):
        return self.workers_number_with_free_disinfectants / self.workplace_number  * 100

    @property
    def percent_of_workers_with_medical_brief(self):
        return self.workers_number_with_medical_brief / self.workplace_number  * 100"""

    # Industrial injuries
    number_of_died_workers = models.IntegerField(verbose_name="Количество погибших на производстве, чел", null=True, blank=True)
    died_workers_info = models.TextField(verbose_name="Информация о погибших работниках (дата, должность, возраст)", null=True, blank=True)
    number_of_hard_injury = models.IntegerField(verbose_name="Количество человек, получивших тяжелые травмы", null=True, blank=True)
    hard_injured_workers_info = models.TextField(verbose_name="Информация о работниках, получивших тяжелые травмы (дата, должность, возраст)", null=True, blank=True)
    number_of_group_accidents = models.IntegerField(
        verbose_name="Групповые несчастные случаи", null=True, blank=True)
    group_accidents_info = models.TextField(
        verbose_name="Информация о групповых несчастных случаях (дата, должность, возраст)", null=True, blank=True)
    number_of_light_injury = models.IntegerField(
        verbose_name="Количество человек, получивших легкие травмы", null=True, blank=True)
    light_injured_workers_info = models.TextField(
        verbose_name="Информация о работниках, получивших легкие травмы (дата, должность, возраст)", null=True, blank=True)
    number_of_micro_injury = models.IntegerField(
        verbose_name="Количество человек, получивших микротравмы", null=True, blank=True)
    micro_injured_workers_info = models.TextField(
        verbose_name="Информация о работниках, получивших микротравмы (дата, должность, возраст)", null=True, blank=True)

    # Common data
    normative_act = models.BooleanField(verbose_name="Наличие локального нормативного акта, регламентирующего систему управления охраной труда", null=True, blank=True)
    committee = models.BooleanField(verbose_name="Наличие комитета (комиссии) по охране труда", null=True, blank=True)
    count_security_workers = models.IntegerField(verbose_name="Наличие уполномоченных (доверенных) лиц по охране труда (чел.)", null=True, blank=True)
    agreement_of_security_work = models.BooleanField(verbose_name="Наличие соглашения по охране труда в организации", null=True, blank=True)
    cabinet_of_security_work = models.BooleanField(verbose_name="Наличие кабинета (уголка) охраны труда", null=True, blank=True)
    cabinet_of_first_aid = models.BooleanField(verbose_name="Наличие помещения для оказания медицинской помощи", null=True, blank=True)
    plan_of_upgrade_workers_conditions = models.BooleanField(verbose_name="Наличие плана мероприятий по улучшению и оздоровлению условий труда", null=True, blank=True)
    financing_plan = models.IntegerField(verbose_name="Объем финансирования плана мероприятий по улучшению и оздоровлению условий труда (тыс. руб.)", null=True, blank=True)
    program_of_saving_aid_of_workers = models.BooleanField(verbose_name="Наличие корпоративной программы сохранения здоровья работников", null=True, blank=True)

    # Labor protection training
    count_of_workers = models.IntegerField(verbose_name="Количество работников, которые должны проходить обучение по охране труда и проверку знаний требований охраны труда в аккредитованных образовательных организациях", null=True, blank=True)
    percent_of_educated = models.CharField(max_length=50, verbose_name="% фактически прошедших такое обучение", null=True, blank=True)
    timely_passage = models.BooleanField(verbose_name="Своевременное проведение инструктажей по охране труда", null=True, blank=True)

    """@property
    def percent_of_educated(self):
        return self.count_of_workers / self.workplace_number  * 100"""

    # Collective agreement
    trade_union_organisation = models.BooleanField(verbose_name="Наличие профсоюзной организации", null=True, blank=True)
    collective_agreement = models.CharField(max_length=100, verbose_name="Наличие коллективного договора", null=True, blank=True)
    change_agreement = models.CharField(max_length=250, verbose_name="Изменения в колдоговор", null=True, blank=True)

    def calculate_percents(self):
        try:
            self.percent_of_educated = round(self.count_of_workers / self.workplace_number  * 100)
        except:
            pass
        try:
            self.percent_of_workers_with_medical_brief = round(self.workers_number_with_medical_brief / self.workplace_number  * 100)
        except:
            pass
        try:
            self.average_percent_provided_disinfectants = round(self.workers_number_with_free_disinfectants / self.workplace_number  * 100)
        except:
            pass
        try:
            self.average_percent_provided_coveralls = round(self.workers_number_with_free_coveralls / self.workplace_number  * 100)
        except:
            pass
        try:
            self.workers_on_danger_positions_percent = round(self.class4_workers_number / self.workplace_number  * 100)
        except:
            pass
        try:
            self.valuated_workplace_percent = round(self.workplace_number_with_valuation / self.workplace_number * 100)
            print(1)
        except:
            pass
        self.save()