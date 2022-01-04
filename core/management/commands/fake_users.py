from django.core.management import BaseCommand
from faker import Faker

from core.models import User


class Command(BaseCommand):
    help = "Generate fake users"

    def handle(self, *args, **options):
        fake = Faker()
        for i in range(10):
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password="",
                first_name=fake.first_name(),
                last_name=fake.last_name(),
            )
            user.set_password("password")
            user.save()
