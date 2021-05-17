import os
import csv
from django.conf import settings
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.forms import model_to_dict
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from graphene_django.views import GraphQLView

from .forms import CursoForm, ParticipanteForm, CursoDeleteForm
from .models import Curso, Participante
from .csv_extractor import CsvExtractor


def get_login_url():
    base_url = getattr(settings, 'BASE_URL')
    return '/' + base_url + 'accounts/login/'


@login_required(login_url=get_login_url())
def new(request):
    if request.method == 'POST':
        create(request)
    form = CursoForm()
    context = {'form': form}
    return render(request, 'new.html', context=context)


@login_required(login_url=get_login_url())
def curso_list(request, curso_id=None):
    cursos = Curso.objects.all()
    context = {'cursos': cursos, 'participantes': []}
    if curso_id:
        participantes = Participante.objects.filter(curso=curso_id)
        context['participantes'] = participantes
        context['curso_nome'] = participantes.first().curso.nome
    return render(request, 'curso_list.html', context=context)


@login_required(login_url=get_login_url())
def participante_update(request, pk):
    if request.method == 'POST':
        return update(request, pk)
    participante = Participante.objects.get(pk=pk)
    participante_dict = model_to_dict(participante)
    form = ParticipanteForm(participante_dict)
    context = {'form': form, 'participante': participante}
    return render(request, 'participante_update.html', context=context)


class PrivateGraphQL(GraphQLView):
    pass


def create(request):
    form = CursoForm(request.POST, request.FILES)
    if form.is_valid():
        curso = Curso.objects.create(**get_curso_data(form))
        file_url = storage_handler(form.cleaned_data['file'])
        participantes_attr = get_participantes_dict(file_url)
        participantes = get_participantes_objects(participantes_attr, curso.id)
        curso.participante_set.bulk_create(participantes)
        remove_files(file_url)


def update(request, pk):
    form = ParticipanteForm(request.POST)
    participante = Participante.objects.filter(pk=pk)
    if form.is_valid():
        participante.update(**form.cleaned_data)
        messages.success(
            request, 'Atualização realizada com sucesso', extra_tags='uk-alert-success')
        return redirect('core:curso_list', participante.first().curso.pk)
    messages.error(request, 'Erro ao tentar atualizar participante',
                   extra_tags='uk-alert-error')
    context = {'form': form, 'participante': participante.first()}
    return render(request, 'participante_update.html', context=context)


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


def curso_delete(request):
    if request.method == 'POST':
        form = CursoDeleteForm(request.POST)
        if form.is_valid():
            Curso.objects.filter(pk=form.cleaned_data['curso']).delete()
            messages.success(request, 'O curso foi removido.',
                             extra_tags='uk-alert-success')
    return redirect('core:curso_list')
