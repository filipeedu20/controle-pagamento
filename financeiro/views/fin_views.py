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
	template = loader.get_template('pagamento_inserir_formaPg.html')
	context = {
		'lista' : 'result',
	}
	return HttpResponse(template.render(context, request))	


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

# Form inserir classificação 
def pagamento_concluir_pagamento(request):
	template = loader.get_template('pagamento_concluir_pagamento.html')
	context = {
		'lista' : 'result',
	}
	return HttpResponse(template.render(context, request))

def pagamento_salvar_conclusao(request):
	template = loader.get_template('pagamento_concluir_pagamento.html')
	context = {
		'lista' : 'result',
	}
	return HttpResponse(template.render(context, request))	

def pagamento_listar_despesas(request):
	result = Contas_pagar.objects.all()
	template = loader.get_template('pagamento_listar_despesas.html')
	context ={'lista' : result}
	return HttpResponse(template.render(context, request))

def pagamento_listar_classificacaoPg(request):
	result = ClassificaPagamento.objects.all()
	template = loader.get_template('pagamento_listar_classificacaoPg.html')
	context = {
		'lista' : result,
	}
	return HttpResponse(template.render(context, request))

def pagamento_detalhar(request, id_pagamento):
	result = Contas_pagar.objects.get(id=id_pagamento)
	template = loader.get_template('pagamento_detalhar.html')
	context = {
		'lista' : result,
	}
	return HttpResponse(template.render(context, request))

def pagamento_alterar(request, id_pagamento):
	result = Contas_pagar.objects.get(id=id_pagamento)
	classePg = ClassificaPagamento.objects.all()
	template = loader.get_template('pagamento_alterar.html')
	situacao = ['aberto','quitado']
	context = {
		'pg' : result,
		'classePg':classePg,
		'situacao':situacao
	}
	return HttpResponse(template.render(context, request))

def pagamento_salvar_alteracao(request):
	dataVencimento =datetime.strptime(request.POST['dataVencimento'], "%d/%m/%Y").date()
	dataPagamento =datetime.strptime(request.POST['dataPagamento'], "%d/%m/%Y").date()
	p = Contas_pagar.objects.alterar(request.POST['id'],dataVencimento,dataPagamento,request.POST['valor'],request.POST['situacao'],request.POST['descricao'],request.POST['classificacao'])
	return HttpResponse(f"{p.descricao} alterado com sucesso")

def pagamento_remove(request, id_pagamento):
	p = Contas_pagar.objects.remover(id_pagamento)
	return HttpResponse(f"{id_pagamento} Pagamento removido!")

'''
Itens de Recebimentos 
'''
def recebimento_salvar_classe(request):
	pg = ClassificacaRec(nome = request.POST['nome'],descricao = request.POST['descricao'])
	pg.save()
	return HttpResponse(f"{pg} Tipo de recebimento registrado com sucesso")

def recebimento_inserir_classificacaoRec(request):
	template = loader.get_template('recebimento_inserir_classificacaoRec.html')
	context = {
		'lista' : 'result',
	}
	return HttpResponse(template.render(context, request))	

#Salva conta a receber 
def recebimento_cadastro(request):
	dataPrevista = datetime.strptime(request.POST['dataPrevista'], "%d/%m/%Y").date()
	pg = Contas_receber.objects.insert(dataPrevista,request.POST['valor'],request.POST['descricao'],request.POST['classificacao'])
	return HttpResponse(f"{pg} Item cadastrado com sucesso!")

#Form inserir recebimento 
def recebimento_inserir(request):
	classRec = ClassificacaRec.objects.all()
	template = loader.get_template('recebimento_inserir.html')
	context = {
		'classRec': classRec,
	}
	return HttpResponse(template.render(context, request))

def recebimento_alterar(request, id_pagamento):
	result = Contas_receber.objects.get(id=id_pagamento)
	classRec = ClassificacaRec.objects.all()
	template = loader.get_template('recebimento_alterar.html')
	situacao = ['aberto','recebido']
	context = {
		'rec' : result,
		'classRec': classRec,
		'situacao':situacao
	}
	return HttpResponse(template.render(context, request))

def recebimento_salvar_alteracao(request):
	dataPrevista =datetime.strptime(request.POST['dataPrevista'], "%d/%m/%Y").date()
	dataRecebimento =datetime.strptime(request.POST['dataRecebimento'], "%d/%m/%Y").date()
	p = Contas_receber.objects.alterar(request.POST['id'],dataRecebimento,dataPrevista,request.POST['valor'],request.POST['situacao'],request.POST['descricao'],request.POST['classificacao'])
	return HttpResponse(f"{p.descricao} alterado com sucesso")

def recebimento_listar_classificacaoRec(request):
	result = ClassificacaRec.objects.all()
	template = loader.get_template('recebimento_listar_classificacaoRec.html')
	context = {
		'lista' : result,
	}
	return HttpResponse(template.render(context, request))


def recebimentos_listar_receitas(request):
	result = Contas_receber.objects.all()
	template = loader.get_template('recebimentos_listar_receitas.html')
	context ={'lista' : result}
	return HttpResponse(template.render(context, request))


#Relatórios 


def recebimento_relatorio_periodo(request):
	ClassRec = ClassificacaRec.objects.all()
	template = loader.get_template('recebimento_relatorio_periodo.html')
	context = {
		'ClassRec': 'ola',
        'teste':'teste'
	}
	return HttpResponse(template.render(context, request))

def recebimento_gerar_rel_periodo(request):
	data_i = datetime.strptime(request.POST['data_inicial'], "%d/%m/%Y").date()
	data_f = datetime.strptime(request.POST['data_final'], "%d/%m/%Y").date()
	dados = Contas_receber.objects.filter(dataPrevista__range=[data_i, data_f])
	total = 0; 
	recebido = "recebido"
	valor_receber = 0; 
	# Soma o valor total das transações  realizados no período 
	for rec in dados: 
		if(rec.situacao == "recebido"):
			total += rec.valor 
		else:
			valor_receber += rec.valor 
	context = {
		'itens': dados,
		'total': total,
		'valor_receber': valor_receber
	}
	template = loader.get_template('recebimento_gerar_rel_periodo.html')
	return HttpResponse(template.render(context, request))

def pagamento_relatorio_periodo(request):
	ClassRec = ClassificacaRec.objects.all()
	template = loader.get_template('pagamento_relatorio_periodo.html')
	context = {
        'teste':'teste'
	}
	return HttpResponse(template.render(context, request))

def pagamento_gerar_rel_periodo(request):
	data_i = datetime.strptime(request.POST['data_inicial'], "%d/%m/%Y").date()
	data_f = datetime.strptime(request.POST['data_final'], "%d/%m/%Y").date()
	dados = Contas_pagar.objects.filter(dataVencimento__range=[data_i, data_f])
	totalPagar = 0; 
	totalPago = 0
	valor_pagar = 0; 
	# Soma o valor total das transações  realizados no período 
	for pg in dados: 
		if(pg.situacao == "pago"):
			totalPago += pg.valor 
		else:
			totalPagar += pg.valor 
	context = {
		'itens': dados,
		'total': totalPago,
		'valor_pagar': totalPagar
	}
	template = loader.get_template('pagamento_gerar_rel_periodo.html')
	return HttpResponse(template.render(context, request))