from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product


class Command(BaseCommand):
    help = "Create product moderator group with specific permissions"

    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name="Модератор продуктов")

        content_type = ContentType.objects.get_for_model(Product)

        can_unpublish_perm = Permission.objects.get(codename='can_unpublish_product', content_type=content_type)
        delete_perm = Permission.objects.get(codename='delete_product', content_type=content_type)

        group.permissions.add(can_unpublish_perm, delete_perm)

        self.stdout.write(self.style.SUCCESS('Successfully created/updated Модератор продуктов group.'))
