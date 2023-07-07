import datetime
from datetime import timedelta

import schedule

from django.core.mail import send_mail
from django.utils import timezone
from apps.clients.models import Clients
from apps.mailings.models import Mailings, MailingLog
from config import settings


def send_email(obj):
    """Sends email to all clients in the group"""
    # List for status
    status = []
    clients = Clients.objects.filter(group=obj.clients.pk)
    for client in clients:
        try:
            send_mail(
                obj.text.subject,
                obj.text.body,
                settings.EMAIL_HOST_USER,
                [client.email]
            )
        except Exception as e:
            server_response = {
                'attempt_status': 'failure',
                'response': f'Error:{str(e)}',
                'mailing': obj,
            }
            status.append(MailingLog(**server_response))
        else:
            server_response = {
                'attempt_status': 'success',
                'response': 'E-mail was sent successfully',
                'mailing': obj,
            }
            status.append(MailingLog(**server_response))
    # Create Logs for every attempt
    MailingLog.objects.bulk_create(status)


def send_mailing():
    """Decide if the email schould be sent"""
    mailings = Mailings.objects.all()
    for mailing in mailings:
        now = timezone.now()
        # If the time of email is now or passed, sends an email
        if mailing.time <= now <= mailing.end_time or mailing.time == now:
            # Changes frequency
            if mailing.frequency == 'D':
                mailing.time += timedelta(days=1)
                mailing.save()
            elif mailing.frequency == 'W':
                mailing.time += timedelta(days=7)
                mailing.save()
            elif mailing.frequency == 'M':
                mailing.time += timedelta(days=30)
                mailing.save()
            send_email(mailing)
        else:
            pass


def run_schedule():
    """Run a schedule"""
    schedule.every(60).seconds.do(send_mailing)
