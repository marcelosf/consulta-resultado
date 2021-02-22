from django import forms


class CursoForm(forms.Form):
    nome = forms.CharField(label='Nome do Curso',
                           max_length=128, required=True)
    num_vagas = forms.IntegerField(label='Número de vagas', required=True)
    file = forms.FileField(label='Arquivo Csv', required=True)


class ParticipanteForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=128, required=True)
    posicao = forms.IntegerField(label='Posicao', required=True)
    status = forms.CharField(label='Status', max_length=30, required=True)
