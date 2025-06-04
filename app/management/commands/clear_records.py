from django.core.management.base import BaseCommand
from records.models import Record


class Command(BaseCommand):
    help = 'Remove todos os registros, mantendo categorias, setores e resíduos'

    def add_arguments(self, parser):
        parser.add_argument(
            '--confirm',
            action='store_true',
            help='Confirma a operação de limpeza dos registros',
        )

    def handle(self, *args, **options):
        if not options['confirm']:
            self.stdout.write(
                self.style.WARNING(
                    '⚠️  Este comando irá remover TODOS os registros do banco de dados.\n'
                    '   Categorias, setores e resíduos serão mantidos.\n'
                    '   Para confirmar, execute: python manage.py clear_records --confirm'
                )
            )
            return

        record_count = Record.objects.count()
        
        if record_count == 0:
            self.stdout.write('ℹ️  Não há registros para remover.')
            return

        Record.objects.all().delete()
        
        self.stdout.write(
            self.style.SUCCESS(
                f'✅ {record_count} registros removidos com sucesso!\n'
                f'   Categorias, setores e resíduos foram mantidos.'
            )
        )
