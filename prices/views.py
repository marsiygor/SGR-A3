from rest_framework import generics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.http import JsonResponse
from . import models, forms, serializers


class PriceListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Price
    template_name = 'prices/price_list.html'
    context_object_name = 'prices'
    permission_required = 'prices.view_price'


class PriceCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Price
    template_name = 'prices/price_form.html'
    form_class = forms.PriceForm
    success_url = reverse_lazy('price_list')
    permission_required = 'prices.add_price'


class PriceDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Price
    template_name = 'prices/price_detail.html'
    permission_required = 'prices.view_price'


class PriceUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Price
    template_name = 'prices/price_form.html'
    form_class = forms.PriceForm
    success_url = reverse_lazy('price_list')
    permission_required = 'prices.change_price'


class PriceDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Price
    template_name = 'prices/price_confirm_delete.html'
    success_url = reverse_lazy('price_list')
    permission_required = 'prices.delete_price'


class PriceCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Price.objects.all()
    serializer_class = serializers.PriceSerializer


class PriceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Price.objects.all()
    serializer_class = serializers.PriceSerializer


def price_by_category(request, category_id):
    from .models import Price
    price = Price.objects.filter(category_id=category_id).order_by('-updated_at').first()
    value = float(price.value) if price else 0
    return JsonResponse({'value': value})
