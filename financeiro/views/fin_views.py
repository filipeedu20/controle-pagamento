from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader
from django.shortcuts import render
from datetime import datetime
from ..models import Contas_pagar,Contas_receber,ClassificacaPg,ClassificacaRec,FormaPG,FormaRec,ClassificaPagamento



@require_http_methods(["GET","POST"])
def home(request):
	return HttpResponse("Olá, ssssssssssssssom sucesso!")

def pagamento_inserir_formaPg(request):
	template = loader.get_template('pagamento_inserir_formaPg.html')
	context = {
		'lista' : 'result',
	}
	return HttpResponse(template.render(context, request))	

#Salva despesa pagamento
def pagamento_salvar_formaPg(request):
	fp = FormaPG(nome = "teste",descricao ="testes 2")
	fp.save()
	return HttpResponse(f"{fp} Cargo cadastrado com sucesso")
#Form inserir pagamento	
def pagamento_inserir(request):
	classPg = ClassificaPagamento.objects.all()
	template = loader.get_template('pagamento_inserir.html')
	context = {
		'classPg': classPg,
	}
	return HttpResponse(template.render(context, request))

#Salva pagamento
def cadastrar_pagar(request):
	dataVencimento =datetime.strptime(request.POST['vencimento'], "%d/%m/%Y").date()
	pg = Contas_pagar.objects.insert(dataVencimento,request.POST['valor'],request.POST['descricao'],request.POST['classificacao'])
	return HttpResponse(f"{pg} cadastrado com sucesso")
	# return HttpResponse(f"{request.POST['descricao']} cadastrado com sucesso")



# Insere classe de pagamento
def pagamento_salvar_classe(request):
	pc = ClassificaPagamento(nome = request.POST['nome'],descricao = request.POST['descricao'])
	pc.save()
	return HttpResponse(f"{pc} Classe registrada com sucesso")
# Form inserir classificação 
def pagamento_inserir_classificacaoPg(request):
	template = loader.get_template('pagamento_inserir_classificacaoPg.html')
	context = {
		'lista' : 'result',
	}
	return HttpResponse(template.render(context, request))	

def pagamento_listar_classificacaoPg(request):
	result = ClassificaPagamento.objects.all()
	template = loader.get_template('pagamento_listar_classificacaoPg.html')
	context = {
		'lista' : result,
	}
	return HttpResponse(template.render(context, request))
'''
Intes de Recebimentos 
'''
def recebimento_salvar_classe(request):
	pg = ClassificacaRec(nome = request.POST['nome'],descricao = request.POST['descricao'])
	pg.save()
	return HttpResponse(f"{pg} Classe registrada com sucesso")

def recebimento_inserir_classificacaoRec(request):
	template = loader.get_template('recebimento_inserir_classificacaoRec.html')
	context = {
		'lista' : 'result',
	}
	return HttpResponse(template.render(context, request))	