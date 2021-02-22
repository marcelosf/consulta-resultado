import os
from django.test import TestCase
from django.shortcuts import resolve_url as r
from unittest import mock
from django.core.files import File
from pathlib import Path

from ..views import get_participantes_dict
from ..forms import CursoForm
from ..models import Curso, Participante


class ViewsTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:new'))

    def test_status_code(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template_is_rendered(self):
        self.assertTemplateUsed(self.resp, 'new.html')

    def test_main_template_is_rendered(self):
        self.assertTemplateUsed(self.resp, 'main.html')

    def test_context_has_form(self):
        form = self.resp.context.get('form')
        self.assertIsInstance(form, CursoForm)

    def test_form_has_been_rendered(self):
        fields = (
            (1, 'type="text'),
            (1, 'type="number'),
            (1, 'type="file')
        )

        for count, field in fields:
            with self.subTest():
                self.assertContains(self.resp, field, count=count)


class ViewPostTest(TestCase):
    def setUp(self):
        base_dir = Path(__file__).parent
        self.csv_path = os.path.join(base_dir, 'mock/curso.csv')
        with open(self.csv_path) as file_mock:
            data = {
                'nome': 'Curso para Professores',
                'num_vagas': 20,
                'file': file_mock
            }
            self.resp = self.client.post(r('core:new'), data)

    def test_curso_created(self):
        self.assertTrue(Curso.objects.exists())

    def test_get_participantes_dict(self):
        expected = [
            {'posicao': 1, 'nome': 'Marc Stelvan', 'status': 'Aprovado'},
            {'posicao': 2, 'nome': 'Marta Schimerman', 'status': 'Invalido'}
        ]
        resp = get_participantes_dict(self.csv_path)
        self.assertListEqual(expected, resp)

    def test_participantes_created(self):
        self.assertTrue(Participante.objects.exists())


class ListarViewTest(TestCase):
    def setUp(self):
        data = dict(nome='Princípios da meteorologia', num_vagas=50)
        participante = {'posicao': 1, 'nome': 'Alfredo', 'status': 'Aprovado'}
        curso = Curso.objects.create(**data)
        curso.participante_set.create(**participante)
        path = r('core:curso_list') + str(curso.id)
        self.resp = self.client.get(path)

    def test_status_code(self):
        self.assertEqual(200, self.resp.status_code)

    def test_render_template(self):
        self.assertTemplateUsed(self.resp, 'curso_list.html')

    def test_render_main_template(self):
        self.assertTemplateUsed(self.resp, 'main.html')

    def test_context_has_cursos(self):
        self.assertIn('cursos', self.resp.context)

    def test_curso_rendered(self):
        self.assertContains(self.resp, 'PRINCÍPIOS DA METEOROLOGIA')

    def test_participante_rendered(self):
        self.assertContains(self.resp, 'Alfredo')


class EditViewGetTest(TestCase):
    def setUp(self):
        data = dict(nome='Princípios da meteorologia', num_vagas=50)
        participante = {'posicao': 1, 'nome': 'Alfredo', 'status': 'Aprovado'}
        curso = Curso.objects.create(**data)
        participante = curso.participante_set.create(**participante)
        path = '/participante/' + str(participante.pk) + '/update'
        self.resp = self.client.get(path)

    def test_status_code(self):
        self.assertTrue(200, self.resp.status_code)

    def test_template_rendered(self):
        self.assertTemplateUsed(self.resp, 'participante_update.html')

    def test_form_is_in_context(self):
        self.assertIn('form', self.resp.context)

    def test_form_is_rendered(self):
        self.assertContains(self.resp, '<input', 4)


class EditViewTest(TestCase):
    def setUp(self):
        data = dict(nome='Princípios da meteorologia', num_vagas=50)
        participante = {'posicao': 1, 'nome': 'Alfredo', 'status': 'Aprovado'}
        curso = Curso.objects.create(**data)
        self.participante = curso.participante_set.create(**participante)

    def test_update_participante_status_code(self):
        resp = self.make_request()
        self.assertTrue(200, resp.status_code)

    def test_form_is_valid(self):
        resp = self.make_request()
        form = resp.context['form']
        self.assertTrue(form.is_valid())

    def test_update_participante_update_data(self):
        self.make_request()
        participante = Participante.objects.get(pk=self.participante.pk)
        self.assertEqual(participante.nome, 'Amália')

    def test_scrf(self):
        resp = self.make_request()
        self.assertContains(resp, 'csrfmiddlewaretoken')
    
    def make_request(self):
        data = dict(posicao=7, nome='Amália', status='Inválido')
        path = '/participante/' + str(self.participante.pk) + '/update'
        return self.client.post(path, data)

