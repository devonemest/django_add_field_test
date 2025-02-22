from django.core.management.base import BaseCommand
from faker import Faker
from user.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        fake = Faker()

        user_count = 1000000

        for i in range(user_count):
            user = User(
                username=f'username_{i}',
                fullname=fake.name(),
                email=fake.email(),
                age=fake.random_int(min=12, max=80),
                phone=fake.phone_number(),
                country=fake.country(),
                city=fake.city(),
                bio=fake.text(),
            )
            user.save()

            if i % 10000 == 0:
                print(f'Добавлено {i} пользователей')

        print(f'✅ Генерация {user_count} пользователей завершена!')
