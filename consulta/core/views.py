from django.shortcuts import render

from .forms import CursoForm


def new(request):
    form = CursoForm()
    context = {'form': form}
    return render(request, 'new.html', context=context)
