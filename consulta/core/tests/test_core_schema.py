import json
from django.test import TestCase
from graphene_django import DjangoObjectType
from graphene.test import Client
from graphene import ObjectType

from .mock import mock_models

from ..schemas import CursoNode, Query
from ...schema import schema


class CursoNodeTest(TestCase):
    def setUp(self):
        self.node = CursoNode

    def test_curso_node_instance(self):
        self.assertIsInstance(self.node(), DjangoObjectType)


class QueryTest(TestCase):
    def setUp(self):
        self.query = Query

    def test_query_instance(self):
        self.assertIsInstance(self.query(), ObjectType)


class QueryRequestTest(TestCase):
    def setUp(self):
        self.data = mock_models.make_curso()
        self.client = Client(schema=schema)

    def test_query_curso(self):
        query = '''{allCursos {edges {node {nome}}}}'''
        nome = self.data.get('curso').nome

        expected = {'data': {'allCursos': {
            'edges': [{'node': {'nome': nome}}]}
        }}

        resp = self.client.execute(query)
        self.assertEqual(resp, expected)

    def test_query_participantes(self):
        query = '''{allParticipantes{edges{node{nome}}}}'''
        nome = self.data.get('participante').nome

        expected = {'data': {'allParticipantes': {
            'edges': [{'node': {'nome': nome}}]}}}

        resp = self.client.execute(query)
        self.assertEqual(resp, expected)
