from unittest import mock
from django.core.files import File
from django.test import TestCase
from django import forms

from ..forms import CursoForm, ParticipanteForm


class FormTest(TestCase):
    def setUp(self):
        self.obj = CursoForm

    def test_is_instance_of_forms(self):
        self.assertIsInstance(self.obj(), forms.Form)

    def test_has_attributes(self):
        attributes = ('nome', 'num_vagas', 'file')
        fields = self.obj().fields.keys()
        for attr in attributes:
            with self.subTest():
                self.assertIn(attr, fields)


class ParticipanteFormTest(TestCase):
    def setUp(self):
        self.obj = ParticipanteForm

    def test_is_instance_of_forms(self):
        self.assertIsInstance(self.obj(), forms.Form)

    def test_has_attributes(self):
        attributes = ('nome', 'posicao', 'status')
        fields = self.obj().fields.keys()
        for attr in attributes:
            with self.subTest():
                self.assertIn(attr, fields)
