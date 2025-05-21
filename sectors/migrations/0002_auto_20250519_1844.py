from django.db import migrations

# Criando uma migração vazia para corrigir o erro
class Migration(migrations.Migration):
    dependencies = [
        ('sectors', '0001_initial'),
    ]

    operations = []
