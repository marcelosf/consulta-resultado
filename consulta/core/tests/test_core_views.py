from django.test import TestCase
from django.shortcuts import resolve_url as r

from ..forms import CursoForm


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
