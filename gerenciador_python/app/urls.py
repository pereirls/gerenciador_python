from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('listar_tarefas/admin/', listar_tarefas, name='listar_tarefas'),
]
