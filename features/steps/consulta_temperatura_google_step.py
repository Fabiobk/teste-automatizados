#Autor: Fabio cunha rodrigues
from behave import *
from features.pages.consulta_temperatura_google_pages import \
    PesquisaTemperatura

perquisa_temperatura = PesquisaTemperatura

@given(u'que eu estou no site do google')
def step_impl(context):
    perquisa_temperatura.acessar_site_google(context)

@when(u'eu pesquisar a temperatura de hoje')
def step_impl(context):
    perquisa_temperatura.pesquisar_temperatura(context)
    perquisa_temperatura.inserir_texto_no_elemento(context)
    perquisa_temperatura.clicar_para_realizar_pesquisa(context)
    
@then(u'o navedor deve traser a temperatura de hoje')
def step_impl(context):
    ...

@then(u'fecho o navegador')
def step_impl(context):
    ...