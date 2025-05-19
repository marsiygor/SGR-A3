from django.urls import path
from . import views

urlpatterns = [
    path('', views.WasteListView.as_view(), name='waste_list'),
    path('create/', views.WasteCreateView.as_view(), name='waste_create'),
    path('<int:pk>/update/', views.WasteUpdateView.as_view(), name='waste_update'),
    path('<int:pk>/delete/', views.WasteDeleteView.as_view(), name='waste_delete'),
]
