from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='email')
    first_name = models.CharField(max_length=250, verbose_name='first_name')
    last_name = models.CharField(max_length=250, verbose_name='last_name', **NULLABLE)
    comment = models.TextField(**NULLABLE)

    def __str__(self):
        return f'{self.email} {self.first_name}'

    class Meta:
        verbose_name = 'client'
        verbose_name_plural = 'clients'
