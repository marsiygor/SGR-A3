from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Record
from .forms import RecordForm


class RecordListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Record
    template_name = 'records/record_list.html'
    context_object_name = 'records'
    permission_required = 'records.view_record'


class RecordCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Record
    form_class = RecordForm
    template_name = 'records/record_form.html'
    success_url = reverse_lazy('record_list')
    permission_required = 'records.add_record'


class RecordUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Record
    form_class = RecordForm
    template_name = 'records/record_form.html'
    success_url = reverse_lazy('record_list')
    permission_required = 'records.change_record'


class RecordDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Record
    template_name = 'records/record_confirm_delete.html'
    success_url = reverse_lazy('record_list')
    permission_required = 'records.delete_record'
