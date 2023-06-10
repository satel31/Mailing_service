from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Clients(models.Model):
    email = models.EmailField(unique=True, verbose_name='email')
    name = models.CharField(max_length=250, verbose_name='first_name')
    comment = models.TextField(**NULLABLE)

    def __str__(self):
        return f'{self.email} {self.name}'

    class Meta:
        verbose_name = 'client'
        verbose_name_plural = 'clients'
