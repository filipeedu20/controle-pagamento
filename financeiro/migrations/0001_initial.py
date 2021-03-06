# Generated by Django 3.0.6 on 2020-06-07 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassificacaPg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=10, null=True)),
                ('descricao', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClassificacaRec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, null=True)),
                ('descricao', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FormaPG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, null=True)),
                ('descricao', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FormaRec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, null=True)),
                ('descricao', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contas_receber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataPrevista', models.DateField(null=True)),
                ('dataRecebimento', models.DateField(null=True)),
                ('valor', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=7, null=True)),
                ('descricao', models.CharField(max_length=200, null=True)),
                ('situacao', models.IntegerField(default=0)),
                ('classificacao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='financeiro.ClassificacaRec')),
            ],
        ),
        migrations.CreateModel(
            name='Contas_pagar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataVencimento', models.DateField(null=True)),
                ('dataPagamento', models.DateField(null=True)),
                ('valor', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=7, null=True)),
                ('descricao', models.CharField(max_length=200, null=True)),
                ('situacao', models.IntegerField(default=0)),
                ('classificacao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='financeiro.ClassificacaPg')),
            ],
        ),
    ]
