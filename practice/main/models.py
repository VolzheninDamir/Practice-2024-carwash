from django.db import models

# Модель клиента
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    # Метод для подсчета количества записей (посещений) клиента
    @property
    def visit_count(self):
        return self.zapisi_set.count()  # Подсчет всех записей, связанных с клиентом


# Модель мойщика
class Moihik(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# Модель записи
class Zapisi(models.Model):
    SERVICE_CHOICES = [
        ('МОЙКА КУЗОВА', 'Мойка кузова'),
        ('ПОЛИРОВКА', 'Полировка'),
        ('ХИМЧИСТКА САЛОНА', 'Химчистка салона'),
        ('НАНЕСЕНИЕ ВОСКА', 'Нанесение воска'),
        ('УДАЛЕНИЕ РЕАГЕНТА', 'Удаление реагента'),
        ('КОМПЛЕКСНАЯ МОЙКА', 'Комплексная мойка'),
        ('ЧЕРНЕНИЕ РЕЗИНЫ', 'Чернение резины'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    moihik = models.ForeignKey(Moihik, on_delete=models.CASCADE)
    date = models.DateTimeField()
    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES)  # Добавляем выбор услуги

    def __str__(self):
        return f'{self.client} - {self.moihik} - {self.date}'
