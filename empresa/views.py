from django.shortcuts import render, redirect
from empresa.models import Empresa
from empresa.forms import EmpresaForm

# Create your views here.
def cadastrar_empresa(request):
  args = {'msg': ''}
  if request.method == 'POST':
        empresa = Empresa()
        empresa.nome = request.POST.get('nome')
        empresa.cnpj = request.POST.get('cnpj')
        empresa.email = request.POST.get('email')
        empresa.telefone = request.POST.get('telefone')
        empresa.save()  
    return render(request, 'cadastrar_empresa.html', args)


def mostrar_empresas(request):
  empresa = Empresa.objects.all()
  return render(request, 'empresas.html', {'dados': empresa})

def delete(request, id):
    empresa = Empresa.objects.get(id=id)

    args = {
        'pessoa': empresa
    }

    empresa.delete()
    return render(request, 'delete.html', args)


def update(request):

    empresa = Empresa.objects.get(id=id)
    form = EmpresaForm(request.POST or None, instance=empresa)

    if form.is_valid():
        form.save()
        return redirect(f'../detail/{pessoa.id}')

    args = {
        'pessoa':empresa,
        'form':form
    }
    return render(request, 'update.html', args)



