from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Sector
from .forms import SectorForm


class SectorListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Sector
    template_name = 'sectors/sector_list.html'
    context_object_name = 'sectors'
    permission_required = 'sectors.view_sector'


class SectorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Sector
    form_class = SectorForm
    template_name = 'sectors/sector_form.html'
    success_url = reverse_lazy('sector_list')
    permission_required = 'sectors.add_sector'


class SectorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Sector
    form_class = SectorForm
    template_name = 'sectors/sector_form.html'
    success_url = reverse_lazy('sector_list')
    permission_required = 'sectors.change_sector'


class SectorDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Sector
    template_name = 'sectors/sector_confirm_delete.html'
    success_url = reverse_lazy('sector_list')
    permission_required = 'sectors.delete_sector'
