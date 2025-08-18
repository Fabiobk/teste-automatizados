# Autor: Fábio cunha rodrigues

import time

from features.support.ambiente import *
from features.support.elementos import *
from features.support.page_utils import PageUtils

page_utils = PageUtils()

class PesquisaTemperatura:
    def acessar_site_google(context):
        page_utils.abrir_um_browser(URL_GOOGLE)
    def pesquisar_temperatura(context):
        page_utils.clicar_elemento_pagina(PESQ_GOOGLE)
    def inserir_texto_no_elemento(context):
        page_utils.inserir_dados_no_elemento(PESQ_GOOGLE, DESC_PESQ_MAIRIPORA)
        time.sleep(5)
    def clicar_para_realizar_pesquisa(context):
        page_utils.executar_enter(BTN_DESC_PESQ)
        time.sleep(20)     