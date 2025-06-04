from django.urls import path
from . import views

urlpatterns = [
    path('', views.WasteListView.as_view(), name='waste_list'),
    path('create/', views.WasteCreateView.as_view(), name='waste_create'),
    path('<int:pk>/detail/', views.WasteDetailView.as_view(), name='waste_detail'),
    path('<int:pk>/update/', views.WasteUpdateView.as_view(), name='waste_update'),
    path('<int:pk>/delete/', views.WasteDeleteView.as_view(), name='waste_delete'),
    path('api/by_category/<int:category_id>/', views.wastes_by_category, name='wastes_by_category'),
    path('api/<int:waste_id>/', views.waste_detail, name='waste_api_detail'),
]
