from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecordListView.as_view(), name='record_list'),
    path('create/', views.RecordCreateView.as_view(), name='record_create'),
    path('<int:pk>/update/', views.RecordUpdateView.as_view(), name='record_update'),
    path('<int:pk>/delete/', views.RecordDeleteView.as_view(), name='record_delete'),
]
