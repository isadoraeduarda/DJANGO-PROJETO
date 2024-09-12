from django.urls import path
from . import views

urlpatterns = [
    path('agendamentos/', views.AgendamentoCreateView.as_view(), name='agendamento-create'),
    path('agendamentos/<int:id>/', views.AgendamentoDetailView.as_view(), name='agendamento-detail'), 
    path('agendamentos/all/', views.AgendamentoListView.as_view(), name='agendamento-list'),
    path('agendamentos/delete/<int:id>/', views.AgendamentoDeleteView.as_view(), name='agendamento-delete'),
    path('agendamentos/update/<int:id>/', views.AgendamentoUpdateView.as_view(), name='agendamento-update'),        
]