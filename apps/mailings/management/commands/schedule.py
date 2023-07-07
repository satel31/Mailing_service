import time

import schedule
from django.core.management import BaseCommand

from apps.mailings.services import run_schedule


class Command(BaseCommand):
    def handle(self, *args, **options):
        run_schedule()
        while True:
            schedule.run_pending()
            time.sleep(1)
