import os
import csv
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from .forms import CursoForm
from .models import Curso, Participante
from .csv_extractor import CsvExtractor


def new(request):
    if request.method == 'POST':
        create(request)
    form = CursoForm()
    context = {'form': form}
    return render(request, 'new.html', context=context)


def create(request):
    form = CursoForm(request.POST, request.FILES)
    if form.is_valid():
        CursoModel.objects.create(**get_curso_data(form))


def get_curso_data(form):
    valid_curso_data = {
        'nome': form.cleaned_data['nome'],
        'num_vagas': form.cleaned_data['num_vagas']
    }
    return valid_curso_data


def get_participantes_dict(file, skip_first_line=True):
    extractor = CsvExtractor(file, skip_first_line)
    return extractor.get_participantes()
