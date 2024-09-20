from django.db import models
from loguru import logger

class Agendamento(models.Model):
    data_pagamento = models.DateField(verbose_name="Data de Pagamento")
    permite_recorrencia = models.BooleanField(default=False, verbose_name="Permitir recorrencia")
    quantidade_recorrencia = models.IntegerField(verbose_name="numero de recorrencias")
    intervalo_recorrencia = models.IntegerField(verbose_name="intervalo em dias entre as recorrências")
    status_recorrencia = models.CharField(max_length=50, verbose_name="Status")
    agencia = models.IntegerField()
    conta = models.IntegerField()
    valor_pagamento = models.IntegerField()

    def save(self, *args, **kwargs):
        logger.info('salvando registro na base de dados')
        if isinstance(self.valor_pagamento, float):
            self.valor_pagamento = int(self.valor_pagamento * 100)
        super(Agendamento, self).save(*args, **kwargs)
