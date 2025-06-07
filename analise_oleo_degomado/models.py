from django.db import models

class TipoOleo(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    hora = models.DateField()

    def __str__(self):
        return self.nome


class OleoDegomado(models.Model):
    id = models.AutoField(primary_key=True)
    umidade = models.ForeignKey(TipoOleo, on_delete=models.PROTECT, related_name='umidade_tipoOleo')
    tara = models.FloatField()
    liquido = models.FloatField()
    peso_amostra = models.FloatField()
    resultado = models.FloatField()