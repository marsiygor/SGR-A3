# 🗂️ Sistema de Gestão de Resíduos (SGR)

## 📋 Comandos Personalizados

### 🚀 Populando o Banco de Dados

Para popular o banco de dados com dados de exemplo, use os seguintes comandos:

#### 1. Comando Principal - Popular Banco Completo
```powershell
python manage.py populate_db --clear
```

**O que faz:**
- ✅ Limpa todos os dados existentes (quando usado com `--clear`)
- ✅ Cria 8 categorias de resíduos (Plásticos, Metais, Papel, etc.)
- ✅ Cria 7 setores (Administração, Produção, Laboratório, etc.)
- ✅ Cria 20 tipos diferentes de resíduos
- ✅ Gera aproximadamente 260 registros dos últimos 3 meses
- ✅ Balanceia 75% entradas e 25% saídas

**Opções:**
- `--clear`: Remove dados existentes antes de popular

#### 2. Comando Adicional - Adicionar Mais Registros
```powershell
python manage.py add_records --days 7 --records-per-day 5
```

**O que faz:**
- ✅ Adiciona registros aos dados existentes (não remove nada)
- ✅ Gera registros para os próximos X dias
- ✅ Mantém proporção realista de entradas/saídas

**Opções:**
- `--days`: Número de dias de registros (padrão: 7)
- `--records-per-day`: Máximo de registros por dia (padrão: 5)

### 📊 Exemplos de Uso

**Primeira vez - Popular tudo:**
```powershell
cd "c:\Users\Marsi\OneDrive\Documentos\.vscode\Estudos\SGR"
python manage.py populate_db --clear
```

**Adicionar mais dados:**
```powershell
# Adicionar 1 semana de registros
python manage.py add_records --days 7

# Adicionar 1 mês com mais atividade
python manage.py add_records --days 30 --records-per-day 8

# Adicionar apenas alguns registros de hoje
python manage.py add_records --days 1 --records-per-day 3
```

### 🎯 Dados Gerados

#### Categorias (8):
- 🍶 **Plásticos**: Garrafas PET, Embalagens, Sacolas
- 🔩 **Metais**: Alumínio, Ferro, Cobre  
- 📄 **Papel e Papelão**: Papel de escritório, Papelão, Jornais
- 🍾 **Vidros**: Garrafas, Frascos
- 💻 **Eletrônicos**: Computadores, Celulares, Cabos
- 🌱 **Orgânicos**: Restos de comida, Folhas
- 🪵 **Madeira**: Paletes, Móveis velhos
- 👕 **Têxtil**: Roupas, Tecidos

#### Setores (7):
- 🏢 **Administração** - João Silva (Bloco A)
- 🏭 **Produção** - Maria Santos (Galpão Principal)
- 📦 **Almoxarifado** - Pedro Costa (Bloco B)
- 🔬 **Laboratório** - Ana Oliveira (Bloco C)
- 🔧 **Manutenção** - Carlos Mendes (Oficina)
- 🍽️ **Refeitório** - Lucia Ferreira (Bloco A)
- 🧹 **Limpeza** - Roberto Lima (Zeladoria)

#### 3. Comando Adicional - Limpar Apenas Registros
```powershell
python manage.py clear_records --confirm
```

**O que faz:**
- ✅ Remove TODOS os registros de entrada/saída
- ✅ Mantém categorias, setores e resíduos intactos
- ✅ Útil para resetar apenas os dados de movimentação

**Segurança:**
- Exige confirmação com `--confirm` para evitar exclusões acidentais

#### 4. Comando de Estatísticas - Ver Status do Banco
```powershell
python manage.py db_stats
```

**O que faz:**
- ✅ Mostra estatísticas detalhadas do banco de dados
- ✅ Resumo financeiro (entradas, saídas, saldo)
- ✅ Registros por categoria
- ✅ Top resíduos por movimentação
- ✅ Registros mais recentes

### 🔄 Outros Comandos Úteis

```powershell
# Ver comandos disponíveis
python manage.py help

# Executar servidor
python manage.py runserver

# Criar superusuário
python manage.py createsuperuser

# Ver migrações
python manage.py showmigrations

# Aplicar migrações
python manage.py migrate
```

### 🌐 Acessando o Sistema

Após popular o banco:
1. **Dashboard**: http://127.0.0.1:8000/
2. **Categorias**: http://127.0.0.1:8000/categories/list/
3. **Setores**: http://127.0.0.1:8000/sectors/
4. **Resíduos**: http://127.0.0.1:8000/wastes/
5. **Registros**: http://127.0.0.1:8000/records/

### 📈 Funcionalidades Disponíveis

- ✅ **Dashboard interativo** com gráficos clicáveis
- ✅ **Gestão completa** de categorias, setores, resíduos e registros
- ✅ **Validação de estoque** (não permite saídas sem estoque)
- ✅ **Cálculo automático** de preços e valores
- ✅ **Relatórios visuais** com Chart.js
- ✅ **Interface responsiva** com Bootstrap

---

💡 **Dica**: Execute `python manage.py populate_db --clear` sempre que quiser resetar completamente os dados de teste!
