# Generated by Django 3.0.6 on 2020-06-09 01:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0003_classificapagamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contas_pagar',
            name='classificacao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='financeiro.ClassificaPagamento'),
        ),
    ]