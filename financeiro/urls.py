from django.urls import path
from .views import fin_views as fin

urlpatterns = [
    path("", fin.home, name="home"),
    path('pagamento_inserir_formaPg/', fin.pagamento_inserir_formaPg, name="pagamento_inserir_formaPg"),
    path('pagamento_salvar_formaPg/', fin.pagamento_salvar_formaPg, name="pagamento_salvar_formaPg"),
    path('pagamento_inserir/', fin.pagamento_inserir, name="pagamento_inserir"),
    path('pagamento_salvar_classe/', fin.pagamento_salvar_classe, name="pagamento_salvar_classe"),
    path('cadastrar_pagar/', fin.cadastrar_pagar, name="cadastrar_pagar"),
    path('pagamento_inserir_classificacaoPg/', fin.pagamento_inserir_classificacaoPg, name="pagamento_inserir_classificacaoPg"),
    path('pagamento_listar_classificacaoPg/', fin.pagamento_listar_classificacaoPg, name="pagamento_listar_classificacaoPg"),
    path('pagamento_listar_despesas/', fin.pagamento_listar_despesas, name="pagamento_listar_despesas"),
    path('pagamento_detalhar/<int:id_pagamento>', fin.pagamento_detalhar, name="pagamento_detalhar"),
    path('pagamento_salvar_alteracao/', fin.pagamento_salvar_alteracao, name="pagamento_salvar_alteracao"),
    path('pagamento_remove/<int:id_pagamento>', fin.pagamento_remove, name="pagamento_remove"),
    
    path('recebimento_listar_classificacaoRec/', fin.recebimento_listar_classificacaoRec, name="recebimento_listar_classificacaoRec"),
    path('recebimentos_listar_receitas/', fin.recebimentos_listar_receitas, name="recebimentos_listar_receitas"),
    path('pagamento_alterar/<int:id_pagamento>', fin.pagamento_alterar, name="pagamento_alterar"),
    path('pagamento_salvar_conclusao/', fin.pagamento_salvar_conclusao, name="pagamento_salvar_conclusao"),
    path('pagamento_concluir_pagamento/<int:id_pessoa>/', fin.pagamento_concluir_pagamento, name="pagamento_concluir_pagamento"),
    path('recebimento_salvar_classe/', fin.recebimento_salvar_classe, name="recebimento_salvar_classe"),
    path('recebimento_inserir_classificacaoRec/', fin.recebimento_inserir_classificacaoRec, name="recebimento_inserir_classificacaoRec"),
    path('recebimento_inserir/', fin.recebimento_inserir, name="recebimento_inserir"),
    path('recebimento_cadastro/', fin.recebimento_cadastro, name="recebimento_cadastro"),
    path('recebimento_salvar_alteracao/', fin.recebimento_salvar_alteracao, name="recebimento_salvar_alteracao"),
    path('recebimento_alterar/<int:id_pagamento>', fin.recebimento_alterar, name="recebimento_alterar"),
    path('recebimento_relatorio_periodo/', fin.recebimento_relatorio_periodo, name="recebimento_relatorio_periodo"),
    path('recebimento_gerar_rel_periodo/', fin.recebimento_gerar_rel_periodo, name="recebimento_gerar_rel_periodo"),  
     path('pagamento_relatorio_periodo/', fin.pagamento_relatorio_periodo, name="pagamento_relatorio_periodo"),
    path('pagamento_gerar_rel_periodo/', fin.pagamento_gerar_rel_periodo, name="pagamento_gerar_rel_periodo")   
]
