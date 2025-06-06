# Generated by Django 5.2.1 on 2025-05-29 00:00

import analises.models
import datetime
import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analises', '0006_delete_configuracaorelatorio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnaliseOleoDegomado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data de Criação')),
                ('atualizado_em', models.DateTimeField(auto_now=True, null=True, verbose_name='Última Atualização')),
                ('data', models.DateField(default=django.utils.timezone.localdate, validators=[analises.models.validate_not_future_date], verbose_name='Data da Análise')),
                ('horario', models.TimeField(default=datetime.time(20, 0, 20, 526040), verbose_name='Horário da Análise')),
                ('tipo_amostra', models.CharField(choices=[('CR', 'Óleo Cru'), ('DG', 'Óleo Degomado'), ('RF', 'Óleo Refinado'), ('RS', 'Resíduo')], default='DG', max_length=2, verbose_name='Tipo de Amostra')),
                ('acidez', models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Acidez (mg KOH/g)')),
                ('umidade_oleo', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Umidade do Óleo (%)')),
                ('impurezas', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Impurezas (%)')),
                ('indice_iodo', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Índice de Iodo (g I₂/100g)')),
                ('cor', models.CharField(blank=True, max_length=10, null=True, verbose_name='Cor (Lovibond)')),
                ('resultado', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Resultado da Análise (%)')),
                ('observacoes', models.TextField(blank=True, max_length=500, null=True, verbose_name='Observações')),
            ],
            options={
                'verbose_name': 'Análise de Óleo Degomado',
                'verbose_name_plural': 'Análises de Óleo Degomado',
                'ordering': ['-data', '-horario'],
            },
        ),
        migrations.AlterField(
            model_name='analiseproteina',
            name='horario',
            field=models.TimeField(default=datetime.time(20, 0, 20, 525828), verbose_name='Horário da Análise'),
        ),
        migrations.AlterField(
            model_name='analiseumidade',
            name='horario',
            field=models.TimeField(default=datetime.time(20, 0, 20, 525236), verbose_name='Horário da Análise'),
        ),
    ]
