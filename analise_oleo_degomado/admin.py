from django.contrib import admin

from analise_oleo_degomado.models import OleoDegomado, TipoOleo

class TipoOleoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'hora')
    search_fields = ('nome',)

class OleoDegomadoAdmin(admin.ModelAdmin):
    list_display = ('umidade', 'tara', 'liquido', 'peso_amostra', 'resultado')
    search_fields = ('umidade',)

admin.site.register(OleoDegomado, OleoDegomadoAdmin)
admin.site.register(TipoOleo, TipoOleoAdmin)