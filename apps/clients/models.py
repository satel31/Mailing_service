from django.db import models

from apps.users.models import User

NULLABLE = {'blank': True, 'null': True}

class Groups(models.Model):
    group_name = models.CharField(max_length=250, verbose_name='Group Name')
    description = models.TextField(verbose_name='Description', **NULLABLE)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, **NULLABLE, related_name='+')

    def __str__(self):
        return f'{self.group_name}'

    class Meta:
        verbose_name = 'group'
        verbose_name_plural = 'groups'

class Clients(models.Model):
    email = models.EmailField(unique=True, verbose_name='Email')
    name = models.CharField(max_length=250, verbose_name='Name')
    comment = models.TextField(**NULLABLE)
    group = models.ForeignKey(Groups, on_delete=models.PROTECT, verbose_name='Group')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return f'{self.email} {self.name}'

    class Meta:
        verbose_name = 'client'
        verbose_name_plural = 'clients'
