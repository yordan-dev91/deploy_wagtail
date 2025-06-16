from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Importa datos'

    def handle(self, *args, **options):

        self.import_superuser()

        self.stdout.write(self.style.SUCCESS('Importación de datos completada exitosamente.'))


    def import_superuser(self):
        self.stdout.write(f'Importación de super usuario')
        username    = 'admin_user'
        email       = 'admin_user@mail.com'
        password    = 'wagtailDeploy_123'

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'Superusuario "{username}" creado exitosamente.'))
        else:
            self.stdout.write(self.style.WARNING(f'El superusuario "{username}" ya existe.'))