from django.urls import path

from .views import new

app_name = 'core'


urlpatterns = [
    path('', new, name='new')
]
