from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование продукта')
    price = models.IntegerField(verbose_name='Цена продукта')
    description = models.TextField(verbose_name='Описание')
    category = models.CharField(max_length=100, verbose_name='Категория')
    owner = models.ForeignKey('Users.User', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return f'{self.name} {self.category} {self.price} {self.description}'


class Version(models.Model):
    STATUS_ACTIVE = 'active'
    STATUS_INACTIVE = 'inactive'
    STATUSES = (
        (STATUS_ACTIVE, 'активна'),
        (STATUS_INACTIVE, 'неактивна'),
    )

    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    version_number = models.IntegerField(verbose_name='Номер версии')
    version_name = models.CharField(max_length=250, verbose_name='Имя версии')
    version_status = models.CharField(choices=STATUSES, default=STATUS_INACTIVE, max_length=10, verbose_name='Статус')

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'

    def __str__(self):
        return f'{self.version_number} {self.version_name} {self.version_status}'