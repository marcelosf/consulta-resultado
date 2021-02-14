from django.test import TestCase
from django.db import models

from ..models import Curso
from ..models import Participante


class CursoTest(TestCase):
    def setUp(self):
        self.obj = Curso()

    def test_is_instance_of_models(self):
        self.assertIsInstance(self.obj, models.Model)

    def test_has_attributes(self):
        attributes = ('nome', 'num_vagas')
        for attr in attributes:
            with self.subTest():
                self.assertTrue(hasattr(self.obj, attr))

    def test_data_exists(self):
        data = dict(nome='Princípios meteorologia', num_vagas=50)
        Curso.objects.create(**data)
        self.assertTrue(Curso.objects.exists())


class ParticipanteTest(TestCase):
    def setUp(self):
        self.obj = Participante()

    def test_is_instance_of_models(self):
        self.assertIsInstance(self.obj, Participante)

    def test_has_attributes(self):
        attributes = ('posicao', 'nome', 'status')
        for attr in attributes:
            with self.subTest():
                self.assertTrue(hasattr(self.obj, attr))

    def test_data_exists(self):
        curso_data = dict(nome='Princípios da Meteorologia', num_vagas=50)
        curso = Curso.objects.create(**curso_data)
        participante_data = dict(
            nome='Abreu', posicao=2, status='Aceito', curso=curso)
        Participante.objects.create(**participante_data)
        self.assertTrue(Participante.objects.exists())
