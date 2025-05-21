from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Waste
from .forms import WasteForm
from .serializers import WasteSerializer


class WasteListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Waste
    template_name = 'wastes/waste_list.html'
    context_object_name = 'wastes'
    permission_required = 'wastes.view_waste'


class WasteCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Waste
    form_class = WasteForm
    template_name = 'wastes/waste_form.html'
    success_url = reverse_lazy('waste_list')
    permission_required = 'wastes.add_waste'


class WasteUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Waste
    form_class = WasteForm
    template_name = 'wastes/waste_form.html'
    success_url = reverse_lazy('waste_list')
    permission_required = 'wastes.change_waste'


class WasteDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Waste
    template_name = 'wastes/waste_confirm_delete.html'
    success_url = reverse_lazy('waste_list')
    permission_required = 'wastes.delete_waste'


def wastes_by_category(request, category_id):
    wastes = Waste.objects.filter(category_id=category_id)
    data = [{'id': w.id, 'name': f'{w.name}', 'weight': w.weight, 'price_per_kg': w.price_per_kg} for w in wastes]
    return JsonResponse(data, safe=False)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def waste_detail(request, waste_id):
    try:
        waste = Waste.objects.get(id=waste_id)
        serializer = WasteSerializer(waste)
        return Response(serializer.data)
    except Waste.DoesNotExist:
        return Response({'error': 'Resíduo não encontrado.'}, status=404)
