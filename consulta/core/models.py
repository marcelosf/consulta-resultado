from django.db import models
from django.utils.translation import gettext as _


class CursoModel(models.Model):
    nome = models.CharField(_("nome"), max_length=254)
    num_vagas = models.IntegerField(_("Número de vagas"))


class ParticipantesModel(models.Model):
    nome = models.CharField(_("Nome"), max_length=128)
    posicao = models.IntegerField(_("Posicao"))
    status = models.CharField(_("Status"), max_length=30, null=True)
    curso = models.ForeignKey('CursoModel', on_delete=models.CASCADE)
