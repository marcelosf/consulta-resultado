from django.urls import path

from .views import new, curso_list, participante_update

app_name = 'core'


urlpatterns = [
    path('', new, name='new'),
    path('list/<int:curso_id>', curso_list, name='curso_list'),
    path('list/', curso_list, name='curso_list'),
    path('participante/<int:pk>/update',
         participante_update, name='participante_update')
]
