from django.urls import path
from . import views

urlpatterns = [
    path('sectors/', views.SectorListView.as_view(), name='sector_list'),
    path('sectors/create/', views.SectorCreateView.as_view(), name='sector_create'),
    path('sectors/<int:pk>/update/', views.SectorUpdateView.as_view(), name='sector_update'),
    path('sectors/<int:pk>/delete/', views.SectorDeleteView.as_view(), name='sector_delete'),
]
