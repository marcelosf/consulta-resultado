from unittest import mock
from django.core.files import File
from django.test import TestCase
from django import forms

from ..forms import CursoForm, ParticipanteForm, CursoDeleteForm


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


class CursoDeleteFormTest(TestCase):
    def setUp(self):
        self.form = CursoDeleteForm

    def test_is_instance_of_forms(self):
        self.assertIsInstance(self.form(), forms.Form)

    def test_has_attribute_curso(self):
        fields = self.form().fields.keys()
        self.assertIn('curso', fields)
