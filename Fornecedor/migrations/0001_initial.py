# Generated by Django 4.0.5 on 2022-06-12 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=100)),
                ('CPF_CNPJ', models.CharField(max_length=100)),
                ('Endereço', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Telefone', models.CharField(max_length=100)),
            ],
        ),
    ]
