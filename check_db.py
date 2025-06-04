#!/usr/bin/env python
import os
import sys
import django

# Setup Django
sys.path.append(os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from records.models import Record
from categories.models import Category
from wastes.models import Waste
from sectors.models import Sector

print("=== DATABASE STATISTICS ===")
print(f"📊 Total records: {Record.objects.count()}")
print(f"📁 Categories: {Category.objects.count()}")
print(f"♻️ Waste types: {Waste.objects.count()}")
print(f"🏢 Sectors: {Sector.objects.count()}")

print("\n=== RECORDS BY CATEGORY ===")
for cat in Category.objects.all():
    count = Record.objects.filter(category=cat).count()
    print(f"  {cat.name}: {count} records")

print("\n=== RECENT RECORDS ===")
recent = Record.objects.order_by('-date')[:5]
for record in recent:
    action = "📥 Entrada" if record.is_entry else "📤 Saída"
    print(f"  {action}: {record.waste.name} - {record.weight}kg - R${record.value} ({record.date.strftime('%d/%m %H:%M')})")

print("\n=== FINANCIAL SUMMARY ===")
entries = Record.objects.filter(is_entry=True)
exits = Record.objects.filter(is_entry=False)
total_entry_value = sum(float(r.value) for r in entries)
total_exit_value = sum(float(r.value) for r in exits)

print(f"  💰 Total entradas: R$ {total_entry_value:,.2f}")
print(f"  💸 Total saídas: R$ {total_exit_value:,.2f}")
print(f"  📈 Saldo: R$ {total_entry_value - total_exit_value:,.2f}")
