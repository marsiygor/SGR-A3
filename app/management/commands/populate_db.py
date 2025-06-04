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
    help = 'Popula o banco de dados com dados de exemplo para teste'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Limpa os dados existentes antes de popular',
        )

    def handle(self, *args, **options):
        if options['clear']:
            self.stdout.write('🗑️  Limpando dados existentes...')
            Record.objects.all().delete()
            Waste.objects.all().delete()
            Sector.objects.all().delete()
            Category.objects.all().delete()
            self.stdout.write(self.style.WARNING('Dados limpos com sucesso!'))

        self.stdout.write('🚀 Iniciando população do banco de dados...')

        # Criar categorias
        self.stdout.write('📂 Criando categorias...')
        categories_data = [
            {'name': 'Plásticos', 'description': 'Materiais plásticos recicláveis como garrafas PET, embalagens'},
            {'name': 'Metais', 'description': 'Sucatas metálicas, latas de alumínio, ferro, cobre'},
            {'name': 'Papel e Papelão', 'description': 'Papel de escritório, jornais, revistas, papelão'},
            {'name': 'Vidros', 'description': 'Garrafas de vidro, frascos, janelas quebradas'},
            {'name': 'Eletrônicos', 'description': 'Equipamentos eletrônicos, componentes, cabos'},
            {'name': 'Orgânicos', 'description': 'Restos de comida, folhas, materiais compostáveis'},
            {'name': 'Madeira', 'description': 'Móveis velhos, paletes, restos de construção'},
            {'name': 'Têxtil', 'description': 'Roupas usadas, tecidos, calçados'},
        ]

        categories = []
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            categories.append(category)
            if created:
                self.stdout.write(f'  ✅ Categoria criada: {category.name}')

        # Criar setores
        self.stdout.write('🏢 Criando setores...')
        sectors_data = [
            {'name': 'Administração', 'responsible': 'João Silva', 'location': 'Bloco A - 1º Andar'},
            {'name': 'Produção', 'responsible': 'Maria Santos', 'location': 'Galpão Principal'},
            {'name': 'Almoxarifado', 'responsible': 'Pedro Costa', 'location': 'Bloco B - Térreo'},
            {'name': 'Laboratório', 'responsible': 'Ana Oliveira', 'location': 'Bloco C - 2º Andar'},
            {'name': 'Manutenção', 'responsible': 'Carlos Mendes', 'location': 'Oficina - Subsolo'},
            {'name': 'Refeitório', 'responsible': 'Lucia Ferreira', 'location': 'Bloco A - Térreo'},
            {'name': 'Limpeza', 'responsible': 'Roberto Lima', 'location': 'Zeladoria'},
        ]

        sectors = []
        for sector_data in sectors_data:
            sector, created = Sector.objects.get_or_create(
                name=sector_data['name'],
                defaults={
                    'responsible': sector_data['responsible'],
                    'location': sector_data['location']
                }
            )
            sectors.append(sector)
            if created:
                self.stdout.write(f'  ✅ Setor criado: {sector.name}')

        # Criar resíduos
        self.stdout.write('♻️  Criando resíduos...')
        wastes_data = [
            # Plásticos
            {'name': 'Garrafas PET', 'category': 'Plásticos', 'weight_range': (0.5, 5.0), 'price_range': (1.20, 2.50)},
            {'name': 'Embalagens Plásticas', 'category': 'Plásticos', 'weight_range': (1.0, 8.0), 'price_range': (0.80, 1.80)},
            {'name': 'Sacolas Plásticas', 'category': 'Plásticos', 'weight_range': (0.3, 2.0), 'price_range': (0.50, 1.20)},
            
            # Metais
            {'name': 'Latas de Alumínio', 'category': 'Metais', 'weight_range': (2.0, 15.0), 'price_range': (4.50, 6.20)},
            {'name': 'Sucata de Ferro', 'category': 'Metais', 'weight_range': (10.0, 50.0), 'price_range': (0.30, 0.80)},
            {'name': 'Fios de Cobre', 'category': 'Metais', 'weight_range': (1.0, 10.0), 'price_range': (15.00, 25.00)},
            
            # Papel e Papelão
            {'name': 'Papel de Escritório', 'category': 'Papel e Papelão', 'weight_range': (5.0, 25.0), 'price_range': (0.40, 0.80)},
            {'name': 'Papelão', 'category': 'Papel e Papelão', 'weight_range': (3.0, 20.0), 'price_range': (0.35, 0.65)},
            {'name': 'Jornais e Revistas', 'category': 'Papel e Papelão', 'weight_range': (2.0, 12.0), 'price_range': (0.25, 0.50)},
            
            # Vidros
            {'name': 'Garrafas de Vidro', 'category': 'Vidros', 'weight_range': (5.0, 30.0), 'price_range': (0.15, 0.35)},
            {'name': 'Frascos de Conserva', 'category': 'Vidros', 'weight_range': (2.0, 15.0), 'price_range': (0.10, 0.25)},
            
            # Eletrônicos
            {'name': 'Computadores Antigos', 'category': 'Eletrônicos', 'weight_range': (8.0, 25.0), 'price_range': (5.00, 15.00)},
            {'name': 'Celulares', 'category': 'Eletrônicos', 'weight_range': (0.2, 1.0), 'price_range': (3.00, 12.00)},
            {'name': 'Cabos e Fios', 'category': 'Eletrônicos', 'weight_range': (1.0, 8.0), 'price_range': (2.00, 8.00)},
            
            # Orgânicos
            {'name': 'Restos de Comida', 'category': 'Orgânicos', 'weight_range': (5.0, 30.0), 'price_range': (0.05, 0.15)},
            {'name': 'Folhas e Galhos', 'category': 'Orgânicos', 'weight_range': (10.0, 50.0), 'price_range': (0.02, 0.08)},
            
            # Madeira
            {'name': 'Paletes de Madeira', 'category': 'Madeira', 'weight_range': (15.0, 40.0), 'price_range': (0.20, 0.60)},
            {'name': 'Móveis Velhos', 'category': 'Madeira', 'weight_range': (20.0, 80.0), 'price_range': (0.15, 0.45)},
            
            # Têxtil
            {'name': 'Roupas Usadas', 'category': 'Têxtil', 'weight_range': (2.0, 15.0), 'price_range': (0.50, 2.00)},
            {'name': 'Tecidos e Retalhos', 'category': 'Têxtil', 'weight_range': (1.0, 10.0), 'price_range': (0.30, 1.50)},
        ]

        wastes = []
        for waste_data in wastes_data:
            # Encontrar categoria
            category = next((c for c in categories if c.name == waste_data['category']), None)
            if not category:
                continue
            
            # Escolher setor aleatório
            sector = random.choice(sectors)
            
            # Gerar peso e preço aleatórios
            weight = round(random.uniform(*waste_data['weight_range']), 2)
            price_per_kg = round(random.uniform(*waste_data['price_range']), 2)
            
            waste, created = Waste.objects.get_or_create(
                name=waste_data['name'],
                defaults={
                    'category': category,
                    'sector': sector,
                    'weight': weight,
                    'price_per_kg': Decimal(str(price_per_kg))
                }
            )
            wastes.append(waste)
            if created:
                self.stdout.write(f'  ✅ Resíduo criado: {waste.name} ({waste.category.name})')

        # Criar registros
        self.stdout.write('📝 Criando registros...')
        
        # Criar registros dos últimos 3 meses
        start_date = timezone.now() - timedelta(days=90)
        current_date = start_date
        
        records_created = 0
        while current_date <= timezone.now():
            # Criar 1-5 registros por dia
            daily_records = random.randint(1, 5)
            
            for _ in range(daily_records):
                waste = random.choice(wastes)
                is_entry = random.choice([True, True, True, False])  # 75% entradas, 25% saídas
                
                # Para entradas: peso maior, para saídas: peso menor
                if is_entry:
                    weight = round(random.uniform(1.0, 20.0), 2)
                else:
                    weight = round(random.uniform(0.5, 10.0), 2)
                
                # Variação de preço ±20%
                base_price = float(waste.price_per_kg)
                price_variation = random.uniform(0.8, 1.2)
                unit_price = round(base_price * price_variation, 2)
                  # Adicionar alguma aleatoriedade na data/hora
                record_time = current_date + timedelta(
                    hours=random.randint(8, 18),
                    minutes=random.randint(0, 59)
                )
                
                record = Record.objects.create(
                    waste=waste,
                    category=waste.category,
                    weight=Decimal(str(weight)),
                    unit_price=Decimal(str(unit_price)),
                    value=Decimal(str(weight)) * Decimal(str(unit_price)),  # Calcular valor total
                    is_entry=is_entry,
                    date=record_time
                )
                records_created += 1
            
            current_date += timedelta(days=1)
        
        self.stdout.write(f'  ✅ {records_created} registros criados')

        # Estatísticas finais
        self.stdout.write('\n📊 ESTATÍSTICAS FINAIS:')
        self.stdout.write(f'  • Categorias: {Category.objects.count()}')
        self.stdout.write(f'  • Setores: {Sector.objects.count()}')
        self.stdout.write(f'  • Resíduos: {Waste.objects.count()}')
        self.stdout.write(f'  • Registros: {Record.objects.count()}')
        
        entries = Record.objects.filter(is_entry=True)
        exits = Record.objects.filter(is_entry=False)
        self.stdout.write(f'    - Entradas: {entries.count()}')
        self.stdout.write(f'    - Saídas: {exits.count()}')
        
        total_entry_value = sum(float(r.value) for r in entries)
        total_exit_value = sum(float(r.value) for r in exits)
        self.stdout.write(f'    - Valor total de entradas: R$ {total_entry_value:.2f}')
        self.stdout.write(f'    - Valor total de saídas: R$ {total_exit_value:.2f}')
        
        self.stdout.write(self.style.SUCCESS('\n🎉 Banco de dados populado com sucesso!'))
        self.stdout.write('💡 Agora você pode testar o sistema com dados realistas!')
