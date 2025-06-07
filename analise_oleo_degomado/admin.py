from django.contrib import admin

from analise_oleo_degomado.models import AnaliseOleoDegomado

##Ñ usar!!!
# class TipoOleoAdmin(admin.ModelAdmin):
#     list_display = ('nome', 'hora')
#     search_fields = ('nome',)

# class OleoDegomadoAdmin(admin.ModelAdmin):
#     list_display = ('umidade', 'tara', 'liquido', 'peso_amostra', 'resultado')
#     search_fields = ('umidade',)

# admin.site.register(OleoDegomado, OleoDegomadoAdmin)
# admin.site.register(TipoOleo, TipoOleoAdmin)

@admin.register(AnaliseOleoDegomado)
class AnaliseOleoDegomadoAdmin(admin.ModelAdmin):
    list_display = ['data', 'horario', 'tipo_amostra', 'peso_amostra', 'resultado']
    list_filter = ['tipo_amostra', 'data']
    search_fields = ['tipo_amostra']