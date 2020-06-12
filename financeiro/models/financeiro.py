from django.db import models
from django.apps import apps
from django.utils.datastructures import MultiValueDictKeyError

class ContasPagarDAO(models.Manager):
    def insert(self,dataVencimento,valor,descricao,classificacao):
        pag = Contas_pagar(dataVencimento = dataVencimento,valor = valor,descricao = descricao,classificacao_id=classificacao)
        pag.save()
        return pag

    def alterar(self,id, dataVencimento,dataPagamento,valor,situacao,descricao,classificacao):
        pag = Contas_pagar.objects.get(id=id)
        if not dataPagamento:
            dataPagamento = None
        pag.dataVencimento = dataVencimento
        pag.dataPagamento=dataPagamento
        pag.valor = valor
        pag.descricao = descricao
        pag.classificacao_id=classificacao
        pag.situacao
        pag.save()
        return pag

    def remover(self, id):
        pag = Contas_pagar.objects.get(id=id)
        pag.delete()

class Contas_pagar(models.Model):
    dataVencimento = models.DateField(null=True)
    dataPagamento = models.DateField(null=True)
    valor = models.DecimalField(null=True, blank=True,max_digits=7, default=None, decimal_places=2)
    descricao = models.CharField(max_length=200, null=True)
    classificacao = models.ForeignKey("ClassificaPagamento",blank=True, null=True, on_delete=models.SET_NULL)
    situacao = models.CharField(max_length=200,default='aberto')

    objects = ContasPagarDAO()

class ContasReceberDAO(models.Manager):
    def insert(self,dataPrevista,valor,descricao,classificacao):
        rec = Contas_receber(dataPrevista = dataPrevista,dataRecebimento = dataRecebimento,valor = valor,descricao = descricao,classificacao_id=classificacao)
        rec.save()
        return rec

    def alterar(self,id, dataPrevista,dataRecebimento,valor,situacao,descricao,classificacao):
        rec = Contas_receber.objects.get(id=id)
        if not dataRecebimento:
            dataRecebimento = None

        rec.dataRecebimento = dataRecebimento
        rec.dataPrevista=dataPrevista
        rec.valor = valor
        rec.descricao = descricao
        rec.classificacao_id=classificacao
        rec.situacao
        rec.save()
        return rec

    def remover(self, id):
        rec = Contas_receber.objects.get(id=id)
        rec.delete()

    
class Contas_receber(models.Model):
    dataPrevista = models.DateField(null=True)
    dataRecebimento = models.DateField(null=True)
    valor = models.DecimalField(null=True, blank=True, default=None, max_digits=7,decimal_places=2)
    descricao = models.CharField(max_length=200, null=True)
    classificacao = models.ForeignKey("ClassificacaRec",blank=True, null=True, on_delete=models.SET_NULL)
    situacao = models.CharField(max_length=200,default='aberto')
    objects = ContasReceberDAO()

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


