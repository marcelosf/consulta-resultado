from django.urls import path

from .views import new, curso_list

app_name = 'core'


urlpatterns = [
    path('', new, name='new'),
    path('list/<int:curso_id>', curso_list, name='curso_list'),
    path('list/', curso_list, name='curso_list'),
]
