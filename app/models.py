from django.db import models





# Models para o Forms




class CadastrarPessoa(models.Model):
    data = models.DateField(verbose_name="Data atual")

    atendentes_escolhas = (
        ("Larissa", "Larissa"),
        ("Micael", "Micael"),
        ("Rafael", "Rafael"),
    )
    atendente = models.CharField(max_length=20, choices=atendentes_escolhas, blank=False, null=False)

    nome = models.CharField(max_length=150) 
    cpf = models.BigIntegerField()
    telefone = models.BigIntegerField()
    email = models.CharField(max_length=150)
    cnpj = models.BigIntegerField()

    formalizacao_escolhas = (
        ("Pessoa Física", "Pessoa Física"),
        ("MEI", "MEI"),
        ("Autônomo", "Autônomo"),
        ("ME", "ME"),
        ("Outro", "Outro"),
    )
    formalizacao = models.CharField(max_length=20, choices=formalizacao_escolhas, blank=False, null=False)

    setor_escolhas = (
        ("Agropecuária", "Agropecuária"),
        ("Construção", "Construção"),
        ("Comércio", "Comércio"),
        ("Indústria", "Indústria"),
        ("Serviços", "Serviços"),
        ("Tecnologia", "Tecnologia"),
        ("Saúde", "Saúde"),
    )
    setor = models.CharField(
        max_length=20, choices=setor_escolhas, blank=False, null=False)

    nivel_escolhas = (
        ("Não identificado", "Não identificado"),
        ("Ideação", "Ideação"),
        ("Validação", "Validação"),
        ("Operação", "Operação"),
        ("Tração", "Tração"),
        ("Escala", "Escala"),
    )
    nivel = models.CharField(
        max_length=20, choices=nivel_escolhas, blank=False, null=False)




    demanda_escolhas = (
        ("Prospecção de clientes", "Prospecção de clientes"),
        ("Aceleração", "Aceleração"),
        ("Confecção do protótipo", "Confecção do protótipo"),
        ("Mentoria", "Mentoria"),
        ("Acesso a fundos/investimentos", "Acesso a fundos/investimentos"),
        ("Modelagem de negócio", "Modelagem de negócio"),
        ("Capacitação do time", "Capacitação do time"),
        ("Infraestrutura", "Infraestrutura"),
        ("Programação/Desenvolvimento", "Programação/Desenvolvimento"),
        ("Aproximação com empresas", "Aproximação com empresas"),
        ("Outra", "Outra"),
    )

    demanda = models.CharField(
        max_length=50, choices=demanda_escolhas, blank=False, null=False)
 





  
class Dash(models.Model):
    nivel = models.CharField(max_length=150)