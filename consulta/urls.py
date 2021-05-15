"""consulta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings

from graphene_django.views import GraphQLView

from consulta.core.views import PrivateGraphQL

base_url = getattr(settings, 'BASE_URL')

next_page = base_url + '/accounts/login/'

login_view = auth_views.LoginView.as_view(template_name='login.html')
logout_view = auth_views.LogoutView.as_view(next_page=next_page)

urlpatterns = [
    path(base_url + 'admin/', admin.site.urls),
    path(base_url + 'accounts/login/', login_view, name='login'),
    path(base_url + 'accounts/logout/', logout_view, name='logout'),
    path(base_url, include('consulta.core.urls')),
    path('api/graphql/', PrivateGraphQL.as_view(graphiql=True)),
]
