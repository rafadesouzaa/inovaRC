from django.forms import ModelForm
from app.models import CadastrarPessoa

# Create the form class.
class PessoaForm(ModelForm):
    class Meta:
        model = CadastrarPessoa
        fields = ['data', 'atendente', 'nome', 'cpf', 'telefone','email', 'cnpj', 'formalizacao', 'setor', 'nivel','demanda']

