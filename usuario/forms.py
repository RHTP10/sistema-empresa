from django import forms
from usuario.models import Pessoa

class PessoaForm(forms.ModelForm):
    class Meta:
    model = Pessoa
    fields = "__all__"