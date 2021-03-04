from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField


from .models import Curso, Participante


class CursoNode(DjangoObjectType):
    class Meta:
        model = Curso
        filter_fields = ['nome', 'num_vagas']
        interfaces = (relay.Node, )


class ParticipanteNode(DjangoObjectType):
    class Meta:
        model = Participante
        filter_fields = {
            'nome': ['exact', 'icontains'],
            'curso__nome': ['exact'],
        }
        interfaces = (relay.Node, )


class Query(ObjectType):
    curso = relay.Node.Field(CursoNode)
    all_cursos = DjangoFilterConnectionField(CursoNode)

    participante = relay.Node.Field(ParticipanteNode)
    all_participantes = DjangoFilterConnectionField(ParticipanteNode)
