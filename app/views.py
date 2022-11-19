from django.shortcuts import render,redirect
from app.forms import PessoaForm
from app.models import CadastrarPessoa
from app.models import Dash

from django.views.generic.base import View
from django.contrib.auth import update_session_auth_hash

import io

import requests








def grafico(request):
    return render(request, 'grafico.php')

def login(request):
    return render(request, 'login.html')

def home(request):
    
    return render(request, 'home.html')
    #return render(request, 'home.html')


def sobre(request):
    return render(request, 'sobre.html')


def dash(request):
    
    #Todas as cores
    cores = ['#FF0000',	'#008000',	'#0000FF',	'#FFFF00',	'#D3D3D3',	'#FFA500',	'#A020F0',	'#00FFFF',	'#836FFF',	'#B0E0E6',	'#00FF00']

    #Setor
    tiposSetor = Dash.objects.raw("SELECT 1 as id, setor, count(setor) AS qtd,  \
        '' as cor FROM app_cadastrarpessoa \
        GROUP BY setor")

    i=0
    for tipoSetor in tiposSetor:
        tipoSetor.cor = cores[i]
        i=i+1

    #Formalização
    tiposFormal = Dash.objects.raw("SELECT 1 as id, formalizacao, count(formalizacao) AS qtd,  \
        '' as cor FROM app_cadastrarpessoa \
        GROUP BY formalizacao")

    i=0
    for tipoFormal in tiposFormal:
        tipoFormal.cor = cores[i]
        i=i+1

    #Nivel
    tiposNivel = Dash.objects.raw("SELECT 1 as id, nivel, count(nivel) AS qtd,  \
        '' as cor FROM app_cadastrarpessoa \
        GROUP BY nivel")

    i=0
    for tipoNivel in tiposNivel:
        tipoNivel.cor = cores[i]
        i=i+1

    #Demanda
    tiposDemanda = Dash.objects.raw("SELECT 1 as id, demanda, count(demanda) AS qtd,  \
        '' as cor FROM app_cadastrarpessoa \
        GROUP BY demanda")

    i=0
    for tipoDemanda in tiposDemanda:
        tipoDemanda.cor = cores[i]
        i=i+1
    
    



    return render(request, 'dash.html', {'tiposNivel': tiposNivel, 'tiposFormal': tiposFormal,'tiposSetor': tiposSetor,'tiposDemanda': tiposDemanda})




# Cadastro e Consulta Pessoas

def formPessoa(request):
    data={}
    data['form'] = PessoaForm()
    return render(request,'cadastrarPessoa.html',data)

def consultaPessoa(request):
    data={}
    search = request.GET.get('search')
    if search:
        data['db'] = (CadastrarPessoa.objects.filter(nome__icontains=search ) or CadastrarPessoa.objects.filter(cpf__icontains=search ))
    else:
        data['db'] = CadastrarPessoa.objects.all
    return render(request,'consultaPessoa.html',data)

def create(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("consulta-pessoa")


# Cadastro e Consulta Atendimento

