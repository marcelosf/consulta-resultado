from django.contrib import admin

from .models import Curso, Participante


class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'num_vagas')


admin.site.register(Curso, CursoAdmin)


class PartipantesAdmin(admin.ModelAdmin):
    list_display = ('posicao', 'nome', 'status', 'curso')


admin.site.register(Participante, PartipantesAdmin)
