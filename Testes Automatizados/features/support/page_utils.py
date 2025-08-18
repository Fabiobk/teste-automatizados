#Autor: Fabio cunha Rodrigues
import base64
import json
import os
import subprocess
import time
import unittest

import allure
import behave
import behave_html_formatter
import pytz
import urllib3
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from support.ambiente import *


class PageUtils(unittest.TestCase):
    #Configurações e opções Microsoft Edge
    edge_options = webdriver.EdgeOptions()
    edge_options.add_argument('--disable-site-isolation-trials')
    edge_options.add_argument('--ignore-certifate-erros')
    edge_options.add_argument('--start-maximized')
    driver = webdriver.Edge(options=edge_options)

    def abrir_um_browser(context, base_url):
        context.driver.get(base_url)
    def limpar_browser(context):
        context.driver.delete_all_cookies()
    def fechar_browser(context):
        context.driver.quit()
    def executar_enter(context, pesquisa):
        enter = context.driver.find_element(By.XPATH, pesquisa)
        enter.send_keys(Keys.ENTER)
    def clicar_elemento_pagina(context, pesquisa):
        context.driver.find_element(By.XPATH, pesquisa).click()
    def inserir_dados_no_elemento(context, elemento, texto):
        context.driver.find_element(By.XPATH, elemento).send_keys(texto)
    
    
