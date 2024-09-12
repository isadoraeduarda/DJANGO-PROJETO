from rest_framework import generics
from .models import Agendamento
from .serializers import AgendamentoSerializer

class AgendamentoCreateView(generics.CreateAPIView):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
    http_method_names = ['post']

class AgendamentoListView(generics.ListAPIView):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer 
    http_method_names = ['get']

class AgendamentoDetailView(generics.RetrieveAPIView):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
    lookup_field = 'id'

class AgendamentoUpdateView(generics.UpdateAPIView):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
    lookup_field = 'id'

class AgendamentoDeleteView(generics.DestroyAPIView): 
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
    lookup_field = 'id'
    http_method_names = ['delete']   

