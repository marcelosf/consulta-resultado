from django.contrib import admin

from .models import CursoModel, ParticipantesModel


class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'num_vagas')


admin.site.register(CursoModel, CursoAdmin)


class PartipantesAdmin(admin.ModelAdmin):
    list_display = ('posicao', 'nome', 'status', 'curso')


admin.site.register(ParticipantesModel, PartipantesAdmin)
