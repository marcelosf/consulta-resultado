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


def curso_list(request, curso_id=None):
    cursos = Curso.objects.all()
    context = {'cursos': cursos, 'participantes': []}
    if curso_id:
        participantes = Participante.objects.filter(curso=curso_id)
        context['participantes'] = participantes
        context['curso_nome'] = participantes.first().curso.nome
    return render(request, 'curso_list.html', context=context)

def create(request):
    form = CursoForm(request.POST, request.FILES)
    if form.is_valid():
        curso = Curso.objects.create(**get_curso_data(form))
        file_url = storage_handler(form.cleaned_data['file'])
        participantes_attr = get_participantes_dict(file_url)
        participantes = get_participantes_objects(participantes_attr, curso.id)
        curso.participante_set.bulk_create(participantes)
        remove_files(file_url)


def storage_handler(file):
    filesystem = FileSystemStorage()
    filename = filesystem.save(file.name, file)
    uploaded_file_url = filesystem.path(filename)
    return uploaded_file_url


def remove_files(path):
    os.remove(path)


def get_curso_data(form):
    valid_curso_data = {
        'nome': form.cleaned_data['nome'],
        'num_vagas': form.cleaned_data['num_vagas']
    }
    return valid_curso_data


def get_participantes_objects(participantes, curso_id):
    participantes_lsit = list()
    for attributes in participantes:
        attributes['curso_id'] = curso_id
        participantes_lsit.append(Participante(**attributes))
    return participantes_lsit


def get_participantes_dict(file, skip_first_line=True):
    extractor = CsvExtractor(file, skip_first_line)
    return extractor.get_participantes()
