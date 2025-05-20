from django.urls import path
from . import views

urlpatterns = [
    path('prices/', views.PriceListView.as_view(), name='price_list'),
    path('prices/create/', views.PriceCreateView.as_view(), name='price_create'),
    path('prices/<int:pk>/update/', views.PriceUpdateView.as_view(), name='price_update'),
    path('prices/<int:pk>/delete/', views.PriceDeleteView.as_view(), name='price_delete'),
    path('api/by_category/<int:category_id>/', views.price_by_category, name='price_by_category'),
]
