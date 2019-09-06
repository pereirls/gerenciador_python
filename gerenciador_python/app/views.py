from django.shortcuts import render

def listar_tarefas(request):
    nomeTarefa = "Assistir semana django e python"
    return render(request,'tarefas/listar_tarefas.html', {"nome_tarefa": nomeTarefa})