# Generated by Django 4.0.4 on 2022-10-19 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CadastrarPessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Data atual')),
                ('atendente', models.CharField(choices=[('Larissa', 'Larissa'), ('Micael', 'Micael'), ('Rafael', 'Rafael')], max_length=20)),
                ('nome', models.CharField(max_length=150)),
                ('cpf', models.BigIntegerField()),
                ('telefone', models.BigIntegerField()),
                ('email', models.CharField(max_length=150)),
                ('cnpj', models.BigIntegerField()),
                ('formalizacao', models.CharField(choices=[('Pessoa Física', 'Pessoa Física'), ('MEI', 'MEI'), ('Autônomo', 'Autônomo'), ('Outro', 'Outro')], max_length=20)),
                ('setor', models.CharField(choices=[('Agropecuária', 'Agropecuária'), ('Construção', 'Construção'), ('Comércio', 'Comércio'), ('Indústria', 'Indústria'), ('Serviços', 'Serviços'), ('Tecnologia', 'Tecnologia'), ('Saúde', 'Saúde')], max_length=20)),
                ('nivel', models.CharField(choices=[('Não identificado', 'Não identificado'), ('Ideação', 'Ideação'), ('Validação', 'Validação'), ('Operação', 'Operação'), ('Tração', 'Tração'), ('Escala', 'Escala')], max_length=20)),
                ('demanda', models.CharField(choices=[('Prospecção de clientes', 'Prospecção de clientes'), ('Aceleração', 'Aceleração'), ('Confecção do protótipo', 'Confecção do protótipo'), ('Mentoria', 'Mentoria'), ('Acesso a fundos/investimentos', 'Acesso a fundos/investimentos'), ('Modelagem de negócio', 'Modelagem de negócio'), ('Capacitação do time', 'Capacitação do time'), ('Infraestrutura', 'Infraestrutura'), ('Programação/Desenvolvimento', 'Programação/Desenvolvimento'), ('Aproximação com empresas', 'Aproximação com empresas'), ('Outra', 'Outra')], max_length=50)),
            ],
        ),
    ]
