from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Adds test data to the database'

    def handle(self, *args, **kwargs):
        """Удаляем существующие данные"""
        Product.objects.all().delete()

        """Добавляем тестовые данные"""
        electronics = Category.objects.get_or_create(name="Electronics", description="Electronic items")[0]
        Product.objects.create(name="Phone", description="Iphone", category=electronics, price=150000)

        self.stdout.write(self.style.SUCCESS('Successfully added test data'))
