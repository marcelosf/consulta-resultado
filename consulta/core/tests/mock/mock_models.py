from ...models import Curso


def make_curso():
    data = dict(nome='Princípios da meteorologia', num_vagas=50)
    participante = {'posicao': 1, 'nome': 'Alfredo', 'status': 'Aprovado'}
    curso = Curso.objects.create(**data)
    participante = curso.participante_set.create(**participante)

    return {'participante': participante, 'curso': curso}
