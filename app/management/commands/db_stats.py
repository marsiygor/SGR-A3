from django.core.management.base import BaseCommand
from django.db.models import Sum
from decimal import Decimal

from records.models import Record
from categories.models import Category
from wastes.models import Waste
from sectors.models import Sector


class Command(BaseCommand):
    help = 'Mostra estatísticas detalhadas do banco de dados'

    def handle(self, *args, **options):
        self.stdout.write('=' * 50)
        self.stdout.write(self.style.SUCCESS('📊 ESTATÍSTICAS DO SISTEMA SGR'))
        self.stdout.write('=' * 50)
        
        # Contadores básicos
        total_records = Record.objects.count()
        total_categories = Category.objects.count()
        total_wastes = Waste.objects.count()
        total_sectors = Sector.objects.count()
        
        self.stdout.write(f'\n🗂️  DADOS BÁSICOS:')
        self.stdout.write(f'  • Categorias: {total_categories}')
        self.stdout.write(f'  • Tipos de resíduos: {total_wastes}')
        self.stdout.write(f'  • Setores: {total_sectors}')
        self.stdout.write(f'  • Total de registros: {total_records}')
        
        if total_records == 0:
            self.stdout.write(self.style.WARNING('\n⚠️  Nenhum registro encontrado. Execute: python manage.py populate_db'))
            return
        
        # Estatísticas de entrada/saída
        entries = Record.objects.filter(is_entry=True)
        exits = Record.objects.filter(is_entry=False)
        
        entries_count = entries.count()
        exits_count = exits.count()
        
        entries_value = entries.aggregate(total=Sum('value'))['total'] or Decimal('0')
        exits_value = exits.aggregate(total=Sum('value'))['total'] or Decimal('0')
        balance = entries_value - exits_value
        
        self.stdout.write(f'\n💰 MOVIMENTAÇÃO FINANCEIRA:')
        self.stdout.write(f'  • Entradas: {entries_count} registros - R$ {entries_value:,.2f}')
        self.stdout.write(f'  • Saídas: {exits_count} registros - R$ {exits_value:,.2f}')
        self.stdout.write(f'  • Saldo: R$ {balance:,.2f}')
        
        # Por categoria
        self.stdout.write(f'\n📁 REGISTROS POR CATEGORIA:')
        for category in Category.objects.all():
            cat_records = Record.objects.filter(category=category).count()
            if cat_records > 0:
                cat_value = Record.objects.filter(category=category).aggregate(total=Sum('value'))['total'] or Decimal('0')
                self.stdout.write(f'  • {category.name}: {cat_records} registros - R$ {cat_value:,.2f}')
        
        # Registros recentes
        self.stdout.write(f'\n📅 REGISTROS MAIS RECENTES:')
        recent_records = Record.objects.order_by('-date')[:5]
        for record in recent_records:
            action = "📥 Entrada" if record.is_entry else "📤 Saída"
            date_str = record.date.strftime('%d/%m/%Y %H:%M')
            self.stdout.write(f'  • {action}: {record.waste.name} - {record.weight}kg - R$ {record.value} ({date_str})')
        
        # Top resíduos por valor
        self.stdout.write(f'\n🏆 TOP RESÍDUOS POR MOVIMENTAÇÃO:')
        from django.db.models import Count
        top_wastes = (Record.objects
                     .values('waste__name')
                     .annotate(
                         total_records=Count('id'),
                         total_value=Sum('value')
                     )
                     .order_by('-total_value')[:5])
        
        for waste in top_wastes:
            self.stdout.write(f"  • {waste['waste__name']}: {waste['total_records']} registros - R$ {waste['total_value']:,.2f}")
        
        self.stdout.write('\n' + '=' * 50)
        self.stdout.write(self.style.SUCCESS('✅ Estatísticas geradas com sucesso!'))
