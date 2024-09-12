from rest_framework import serializers
from .models import Agendamento

class AgendamentoSerializer(serializers.ModelSerializer):
    valor_pagamento = serializers.FloatField(write_only=False) 
    class Meta:
        model = Agendamento
        fields = "__all__"

    def validate_quantidade_recorrencia(self, value):
        if value < 0:
            raise serializers.ValidationError("A quantidade deve ser um número positivo.")
        return value
    
    def validate_status_recorrencia(self, value):
        allowed_statuses = ['pendente', 'concluído', 'cancelado']
        if value not in allowed_statuses:
            raise serializers.ValidationError(f"O status deve ser um dos seguintes: {', '.join(allowed_statuses)}.")
        return value
    
    def validate(self, data):
        data['valor_pagamento'] = int(data['valor_pagamento'])
        if not data['permite_recorrencia'] and data['quantidade_recorrencia'] > 0:
            raise serializers.ValidationError("Como nao é permitido ter recorrencia, a quantidade de recorrencia nao pode ser maior que 0")
        return data