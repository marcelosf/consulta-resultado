from django.test import TestCase
from django.shortcuts import resolve_url as r


class ViewsTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:new'))

    def test_status_code(self):
        self.assertEqual(200, self.resp.status_code)
