import logging
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator




logger = logging.getLogger(__name__)

def validate_not_future_date(value):
    """Valida que uma data não está no futuro."""
    if value > timezone.localdate():
        raise ValidationError('A data não pode estar no futuro.')


class BaseModel(models.Model):
    """
    Modelo base que contém campos e métodos comuns a todos os modelos.
    """
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação", null=True, blank=True)
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name="Última Atualização", null=True, blank=True)
    
    class Meta:
        abstract = True

class AnaliseOleoDegomado(BaseModel):
    """
    Modelo para armazenar análises de Oleo Degomado
    """
    TIPO_AMOSTRA_CHOICES = [
        ('OP', 'Óleo Produção'),
        ('OE', 'Óleo Expedição'),
    ]

    data = models.DateField(
        verbose_name="Data da Análise", 
        default=timezone.localdate,
        validators=[validate_not_future_date]
    )
    
    horario = models.TimeField(
        verbose_name="Horário da Análise",
        default=timezone.localtime().time()
    )

    tipo_amostra = models.CharField(
        max_length=2,
        choices=TIPO_AMOSTRA_CHOICES,
        verbose_name="Tipo de Amostra",
        default='OP'  # Oleo de Produção como padrão
    )

    tara = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Tara")
    liquido = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Líquido")
    peso_amostra = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Peso da Amostra")
    resultado = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Resultado")
    fator_correcao = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        blank=True, 
        null=True, 
        verbose_name="Fator de Correção",
        validators=[MinValueValidator(-1000), MaxValueValidator(1000)]
    )

    def __str__(self):
        return f"Análise de Oleo Degomado - {self.get_tipo_amostra_display()} - {self.data}"


##Ñ usar!!!
# class TipoOleo(models.Model):
#     id = models.AutoField(primary_key=True)
#     nome = models.CharField(max_length=200)
#     hora = models.DateField()

#     def __str__(self):
#         return self.nome


# class OleoDegomado(models.Model):
#     id = models.AutoField(primary_key=True)
#     umidade = models.ForeignKey(TipoOleo, on_delete=models.PROTECT, related_name='umidade_tipoOleo')
#     tara = models.FloatField()
#     liquido = models.FloatField()
#     peso_amostra = models.FloatField()
#     resultado = models.FloatField()



