from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.utils import timezone
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
    
    def form_valid(self, form):
        form.instance.date = form.instance.date or timezone.now()
        return super().form_valid(form)


class RecordUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Record
    form_class = RecordForm
    template_name = 'records/record_form.html'
    success_url = reverse_lazy('record_list')
    permission_required = 'records.change_record'
    
    def form_valid(self, form):
        form.instance.date = form.instance.date or timezone.now()
        return super().form_valid(form)


class RecordDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Record
    template_name = 'records/record_confirm_delete.html'
    success_url = reverse_lazy('record_list')
    permission_required = 'records.delete_record'


class RecordDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Record
    template_name = 'records/record_detail.html'
    context_object_name = 'record'
    permission_required = 'records.view_record'
