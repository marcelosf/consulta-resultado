from django.db import models
from django.utils.translation import gettext as _


class CursoModel(models.Model):
    nome = models.CharField(_("nome"), max_length=254)
    num_vagas = models.IntegerField(_("Número de vagas"))
