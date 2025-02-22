from django.core.management.base import BaseCommand
import random
from dummies.models import Dummies


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        dummies_count = 1000000

        for i in range(dummies_count):
            name = f'Dummy {i + 1}'
            height = random.uniform(150.0, 190.0)
            weight = random.uniform(50.0, 100.0)

            Dummies.objects.create(name=name, height=height, weight=weight)

            if i % 10000 == 0:
                print(f'Добавлено {i} dummies')

        print(f'✅ Генерация {dummies_count} dummies завершена!')
