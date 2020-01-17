from django.shortcuts import render, redirect
from empresa.models import Empresa
from empresa.forms import EmpresaForm

# Create your views here.
def cadastrar_empresa(request):
    print('Entrei')
    args = {'msg': ''}
    if request.method == 'POST':
        empresa = Empresa()
        empresa.nome = request.POST.get('nome')
        empresa.endereco = request.POST.get('endereco')
        empresa.email = request.POST.get('email')
        empresa.telefone = request.POST.get('telefone')
        empresa.cnpj = request.POST.get('cnpj')
        print('Peguei os dados')
        empresa.save()
        print('Salvei os dados')  
    return render(request, 'cadastrar_empresa.html', args)
 

def mostrar_empresas(request):
    empresa = Empresa.objects.all()
    return render(request, 'empresas.html', {'dados': empresa})

def delete_empresa(request, id):
    empresa = Empresa.objects.get(pk=id)

    args = {
        'empresa': empresa
    }

    empresa.delete()
    return render(request, 'delete_empresa.html', args)


def update_empresa(request, id):

    empresa = Empresa.objects.get(pk=id)
    form = EmpresaForm(request.POST or None, instance=empresa)

    if form.is_valid():
        form.save()
        return redirect(f'../detail/{pessoa.id}')

    args = {
        'empresa':empresa,
        'form':form
    }
    return render(request, 'update_empresa.html', args)



