from django.db import models

# Create your models here.
class Organisation(models.Model):

    # collective agreement
    trade_union_organisation = models.BooleanField(verbose_name="Наличие профсоюзной организации")
    collective_agreement = models.PositiveBigIntegerField(verbose_name="Наличие коллективного договора")
    change_agreement = models.PositiveBigIntegerField(verbose_name="Изменения в колдоговор")