import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from . import metrics


@login_required(login_url='login')
def home(request):
    waste_record_metrics = metrics.get_waste_and_record_metrics()
    entry_exit_data = metrics.get_entry_exit_data()
    context = {
        'waste_record_metrics': waste_record_metrics,
        'entry_exit_data': json.dumps(entry_exit_data),
    }
    return render(request, 'home.html', context)
