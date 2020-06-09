from django.urls import path
from .views import fin_views as fin

urlpatterns = [
    path('home/', fin.home, name="home"),
    path('pagamento_inserir_formaPg/', fin.pagamento_inserir_formaPg, name="pagamento_inserir_formaPg"),
    path('pagamento_salvar_formaPg/', fin.pagamento_salvar_formaPg, name="pagamento_salvar_formaPg"),
    path('pagamento_inserir/', fin.pagamento_inserir, name="pagamento_inserir"),
    path('pagamento_salvar_classe/', fin.pagamento_salvar_classe, name="pagamento_salvar_classe"),
    path('cadastrar_pagar/', fin.cadastrar_pagar, name="cadastrar_pagar"),
    path('pagamento_inserir_classificacaoPg/', fin.pagamento_inserir_classificacaoPg, name="pagamento_inserir_classificacaoPg"),
    path('pagamento_listar_classificacaoPg/', fin.pagamento_listar_classificacaoPg, name="pagamento_listar_classificacaoPg"),
    # Recebimento
    path('recebimento_salvar_classe/', fin.recebimento_salvar_classe, name="recebimento_salvar_classe"),
    path('recebimento_inserir_classificacaoRec/', fin.recebimento_inserir_classificacaoRec, name="recebimento_inserir_classificacaoRec"),
]
