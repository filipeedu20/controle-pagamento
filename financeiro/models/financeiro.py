from django.db import models
from django.apps import apps
from django.utils.datastructures import MultiValueDictKeyError

class ContasPagarDAO(models.Manager):
    def insert(self,dataVencimento,valor,descricao,classificacao):
        pag = Contas_pagar(dataVencimento = dataVencimento,valor = valor,descricao = descricao,classificacao=classificacao)
        pag.save()
        return pag

class Contas_pagar(models.Model):
    dataVencimento = models.DateField(null=True)
    dataPagamento = models.DateField(null=True)
    valor = models.DecimalField(null=True, blank=True,max_digits=7, default=None, decimal_places=2)
    descricao = models.CharField(max_length=200, null=True)
    classificacao = models.ForeignKey("ClassificaPagamento",blank=True, null=True, on_delete=models.CASCADE)
    situacao = models.IntegerField(default=0)

    objects = ContasPagarDAO()

class Contas_receber(models.Model):
    dataPrevista = models.DateField(null=True)
    dataRecebimento = models.DateField(null=True)
    valor = models.DecimalField(null=True, blank=True, default=None, max_digits=7,decimal_places=2)
    descricao = models.CharField(max_length=200, null=True)
    classificacao = models.ForeignKey("ClassificacaRec",blank=True, null=True, on_delete=models.CASCADE)
    situacao = models.IntegerField(default=0)

class ClassificacaPg(models.Model):
    nome = models.CharField(max_length=100, null=True)
    descricao = models.CharField(max_length=200, null=True)

class ClassificacaPgDAO(models.Manager):   
    def insert(self, nome,descricao):
        pg = ClassificacaPg(nome = descricao,descricao=descricao)
        pg.save()
        return pg

    def editar(self, id, descricao):
        pg = ClassificacaPg.objects.get(id=id)
        pg.descricao = descricao        
        pg.save()
        return pg

    def excluir(self, id):
        pg= ClassificacaPg.objects.get(id=id)
        pg.delete()

class ClassificacaRec(models.Model):
    nome = models.CharField(max_length=100, null=True)
    descricao = models.CharField(max_length=200, null=True)

    def insert(self, descricao):
        pg = ClassificacaRec(nome = descricao,descricao=descricao)
        pg.save()
        return pg

    def editar(self, id, descricao):
        pg = ClassificacaRec.objects.get(id=id)
        pg.descricao = descricao        
        pg.save()
        return pg

    def excluir(self, id):
        pg= ClassificacaRec.objects.get(id=id)
        pg.delete()

class FormaPG(models.Model):
    nome = models.CharField(max_length=100, null=True)
    descricao = models.CharField(max_length=200, null=True)
    
    def insert(self, descricao):
        pg = FormaPG(nome = descricao,descricao=descricao)
        pg.save()
        return pg

    def editar(self, id, descricao):
        pg = FormaPG.objects.get(id=id)
        pg.descricao = descricao        
        pg.save()
        return pg

    def excluir(self, id):
        pg= FormaPG.objects.get(id=id)
        pg.delete()

class ClassificaPagamento(models.Model):
    nome = models.CharField(max_length=100, null=True)
    descricao = models.CharField(max_length=200, null=True)
    
    def insert(self, descricao):
        pg = FormaPG(nome = descricao,descricao=descricao)
        pg.save()
        return pg

    def edit(self, id, descricao):
        pg = FormaPG.objects.get(id=id)
        pg.descricao = descricao        
        pg.save()
        return pg

    def remove(self, id):
        pg= FormaPG.objects.get(id=id)
        pg.delete()

class FormaRec(models.Model):
    nome = models.CharField(max_length=100, null=True)
    descricao = models.CharField(max_length=200, null=True)


