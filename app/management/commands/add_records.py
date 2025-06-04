from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from decimal import Decimal
import random
from datetime import timedelta

from categories.models import Category
from sectors.models import Sector
from wastes.models import Waste
from records.models import Record


class Command(BaseCommand):
    help = 'Adiciona mais registros ao banco de dados existente'

    def add_arguments(self, parser):
        parser.add_argument(
            '--days',
            type=int,
            default=7,
            help='Número de dias de registros para adicionar (padrão: 7)',
        )
        parser.add_argument(
            '--records-per-day',
            type=int,
            default=5,
            help='Número máximo de registros por dia (padrão: 5)',
        )

    def handle(self, *args, **options):
        days = options['days']
        max_records_per_day = options['records_per_day']
        
        # Verificar se temos dados básicos
        if not Category.objects.exists():
            self.stdout.write(self.style.ERROR('❌ Nenhuma categoria encontrada. Execute: python manage.py populate_db primeiro'))
            return
            
        if not Waste.objects.exists():
            self.stdout.write(self.style.ERROR('❌ Nenhum resíduo encontrado. Execute: python manage.py populate_db primeiro'))
            return

        self.stdout.write(f'📝 Adicionando registros para os próximos {days} dias...')
        
        wastes = list(Waste.objects.all())
        start_date = timezone.now()
        records_created = 0
        
        for day in range(days):
            current_date = start_date + timedelta(days=day)
            daily_records = random.randint(1, max_records_per_day)
            
            for _ in range(daily_records):
                waste = random.choice(wastes)
                is_entry = random.choice([True, True, True, False])  # 75% entradas
                
                # Peso aleatório
                if is_entry:
                    weight = round(random.uniform(1.0, 20.0), 2)
                else:
                    weight = round(random.uniform(0.5, 10.0), 2)
                
                # Preço com variação
                base_price = float(waste.price_per_kg)
                price_variation = random.uniform(0.8, 1.2)
                unit_price = round(base_price * price_variation, 2)
                
                # Data/hora aleatória
                record_time = current_date + timedelta(
                    hours=random.randint(8, 18),
                    minutes=random.randint(0, 59)
                )
                
                Record.objects.create(
                    waste=waste,
                    category=waste.category,
                    weight=Decimal(str(weight)),
                    unit_price=Decimal(str(unit_price)),
                    value=Decimal(str(weight)) * Decimal(str(unit_price)),
                    is_entry=is_entry,
                    date=record_time
                )
                records_created += 1
        
        self.stdout.write(f'  ✅ {records_created} novos registros criados')
        
        # Estatísticas atualizadas
        total_records = Record.objects.count()
        entries = Record.objects.filter(is_entry=True).count()
        exits = Record.objects.filter(is_entry=False).count()
        
        self.stdout.write('\n📊 ESTATÍSTICAS ATUALIZADAS:')
        self.stdout.write(f'  • Total de registros: {total_records}')
        self.stdout.write(f'    - Entradas: {entries}')
        self.stdout.write(f'    - Saídas: {exits}')
        
        self.stdout.write(self.style.SUCCESS(f'\n🎉 {records_created} registros adicionados com sucesso!'))
