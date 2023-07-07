from django.db import models

from apps.clients.models import Groups, Clients

NULLABLE = {'blank': True, 'null': True}


class Mail(models.Model):
    subject = models.CharField(max_length=500, verbose_name='Subject of the e-mail')
    body = models.TextField(verbose_name='Body of the e-mail')

    class Meta:
        verbose_name = 'mail'
        verbose_name_plural = 'mails'


class Mailings(models.Model):
    FREQUENCY_CHOICES = (
        ('D', 'daily'),
        ('W', 'weekly'),
        ('M', 'monthly')
    )
    STATUS_CHOICES = (
        ('created', 'created'),
        ('running', 'running'),
        ('completed', 'completed'),
    )

    time = models.DateTimeField(**NULLABLE, verbose_name='Time of sending')
    end_time = models.DateTimeField(**NULLABLE, verbose_name='Time of the ending')
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES, verbose_name='Frequency of sending')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='created',
                              verbose_name='Status of sending')
    clients = models.ForeignKey(Groups, on_delete=models.CASCADE, verbose_name='Group of clients')
    text = models.ForeignKey(Mail, on_delete=models.CASCADE, verbose_name='Text of mailing')

    def __str__(self):
        return f'{self.time}, {self.frequency}, {self.status}, {self.clients}'

    class Meta:
        verbose_name = 'mailing'
        verbose_name_plural = 'mailings'
        ordering = ('-time',)


class MailingLog(models.Model):
    ATTEMPT_STATUS_CHOICES = (
        ('success', 'success'),
        ('failure', 'failure'),
    )

    attempt_date = models.DateTimeField(auto_now_add=True, verbose_name='Date of the last attempt')
    attempt_status = models.CharField(max_length=10, choices=ATTEMPT_STATUS_CHOICES,
                                      verbose_name='Status of the last attempt')
    response = models.TextField(**NULLABLE, verbose_name='Response of the server')
    mailing = models.ForeignKey(Mailings, default=None, on_delete=models.CASCADE, **NULLABLE, verbose_name='Mailing')

    class Meta:
        verbose_name = 'log'
        verbose_name_plural = 'logs'
        ordering = ('-attempt_date',)
