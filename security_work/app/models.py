from django.db import models


class Organisation(models.Model):
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


    # Labor protection training
    count_of_workers = models.IntegerField(verbose_name="Количество работников, которые должны проходить обучение по охране труда", null=True)
    persnt_of_educated = models.IntegerField(verbose_name="% фактически прошедших такое обучение", null=True)
    timely_passage = models.BooleanField(verbose_name="Своевременное проведение инструктажей по охране труда", null=True)


    # Collective agreement
    trade_union_organisation = models.BooleanField(verbose_name="Наличие профсоюзной организации", null=True)
    collective_agreement = models.PositiveBigIntegerField(verbose_name="Наличие коллективного договора", null=True)
    change_agreement = models.PositiveBigIntegerField(verbose_name="Изменения в колдоговор", null=True)