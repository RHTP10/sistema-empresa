from django.shortcuts import render, redirect
from usuario.models import Pessoa
from usuario.forms import PessoaForm
def mostrar_formulario_cadastro(request):
  args = {'msg': ''}
  if request.method == 'POST':
    pessoa = Pessoa()
    pessoa.nome = request.POST.get('nome')
    pessoa.cpf = request.POST.get('cpf')
    pessoa.email = request.POST.get('email')
    pessoa.telefone = request.POST.get('telefone')
    pessoa.genero = request.POST.get('genero')
    pessoa.save()
    return render(request, '/login.html')
  return render(request, 'cadastrar_pessoa.html', args)

def mostrar_pessoas(request):
  pessoas = Pessoa.objects.all()
  return render(request, 'pessoas.html', {'dados': pessoas})

def login(request):
  if request.method == 'POST':
    email_formulario = request.POST.get('email')
    pessoa_banco_dados = Pessoa.objects.filter(email=email_formulario).first()
    if pessoa_banco_dados is not None:
      return mostrar_pessoas(request)
    return render(request, 'login.html', {'msg': 'Ops, não encontramos'})

  return render(request, 'login.html', {'msg': 'seja bem vindo'})

def delete(request, id):
    pessoa = Pessoa.objects.get(pk=id)

    args = {
        'pessoa': pessoa
    }

    pessoa.delete()
    return render(request, 'delete.html', args)


def update(request, id):

    pessoa = Pessoa.objects.get(pk=id)
    form = PessoaForm(request.POST or None, instance=pessoa)

    if form.is_valid():
        form.save()
        return redirect(f'../detail/{pessoa.id}')

    args = {
        'pessoa':pessoa,
        'form':form
    }
    return render(request, 'update.html', args)


def home(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/', kwargs={'msg':'Cadastrado com sucesso'})

    pessoas = reversed(Pessoa.objects.filter().all())

    args = {
        'gatinhos': pessoas,
        'form':form
    }

    return render(request, 'base.html', args)
