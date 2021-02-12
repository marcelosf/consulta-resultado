from django import forms


class CursoForm(forms.Form):
    nome = forms.CharField(label='Nome do Curso',
                           max_length=128, required=True)
    num_vagas = forms.IntegerField(label='Número de vagas', required=True)
    file = forms.FileField(label='Arquivo Csv', required=True)
