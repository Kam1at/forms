from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='наименование продукта')
    price = models.IntegerField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')
    category = models.CharField(max_length=100, verbose_name='Категория')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return f'{self.name} {self.category} {self.price} {self.description}'


class Version:
    STATUS_ACTIVE = 'active'
    STATUS_INACTIVE = 'inacticve'
    STATUSES = (
        (STATUS_ACTIVE, 'активна'),
        (STATUS_INACTIVE, 'неактивна')
    )
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    version_number = models.IntegerField(verbose_name='Номер версии')
    version_name = models.CharField(max_length=250, verbose_name='Имя версии')
    version_status = models.CharField(choices=STATUSES, default=STATUS_INACTIVE, max_length=10, verbose_name='Статус')

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'

    def __str__(self):
        return f'{self.product} {self.version_number} {self.version_name} {self.version_status}'
