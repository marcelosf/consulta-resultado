from django.contrib import admin

from .models import CursoModel


class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'num_vagas')


admin.site.register(CursoModel, CursoAdmin)
