from django.db import models


class Staff(models.Model):
    CHOICE_TYPE = (
        ('1', 'Полная ставка'),
        ('0.5', 'Неполная'),
    )

    name = models.CharField(max_length=50, verbose_name="ФИО")
    type = models.CharField(max_length=50, choices=CHOICE_TYPE, default='1', verbose_name="Ставка")
    character = models.TextField(max_length=100, verbose_name="Должность")
    price = models.IntegerField(verbose_name="Зарплата")
    image = models.ImageField(null=True, blank=True, upload_to="image/")

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'список сотрудников'

    def __str__(self):
        return self.name

