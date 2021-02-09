from django.test import TestCase
from django.db import models

from ..models import CursoModel


class CursoModelTest(TestCase):
    def setUp(self):
        self.obj = CursoModel()

    def test_is_instance_of_models(self):
        self.assertIsInstance(self.obj, models.Model)

    def test_has_attributes(self):
        attributes = ('nome', 'num_vagas')
        for attr in attributes:
            with self.subTest():
                self.assertTrue(hasattr(self.obj, attr))
