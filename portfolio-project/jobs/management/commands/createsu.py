from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if not User.objects.filter(username='bens').exists():
            User.objects.create_superuser(
                username='bens',
                password='django1234'
            )
        print('Superuser has been created.')