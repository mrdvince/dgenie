import time
from typing import Any

from django.core.management import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> None:

        self.stdout.write("Waiting for database to be ready...")
        conn = None

        while not conn:
            try:
                conn = connections["default"]
            except OperationalError:
                self.stdout.write("Database unavailable, waiting for 3 seconds...")
                time.sleep(3)

        self.stdout.write(self.style.SUCCESS("Successfully connected to database"))
