import unittest, time
from selenium import webdriver
from selenium.webdriver import Edge, EdgeOptions

# def before_all(context):
    # options = EdgeOptions
    # options.add_argument('--start-maximized')
    # options.add_argument('--ignore-certificate-erros')
    # driver = webdriver.Edge(executable_path='C:/Projetos_Automacao/msedgedriver.exe', edge_options=options)
# 
def after_all(context):
    context.driver.quit()