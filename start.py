#!/usr/bin/env python3
# coding: utf-8

# Importa os módulos necessários
import subprocess

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Configurações do Chrome para rodar em modo headless
chrome_options = Options()
# Adiciona argumento para garantir que o Chrome rode sem interface gráfica
chrome_options.add_argument("--headless")
# Adiciona argumento recomendado como parte das configurações para o modo headless
chrome_options.add_argument("--disable-gpu")

# Executa o comando 'whereis' para encontrar o caminho do chromedriver
result = subprocess.run(["whereis", "chromedriver"], capture_output=True, text=True)

# Extrai o caminho do output
paths = result.stdout.split()
# Atribui o caminho encontrado para a variável, se disponível
path_to_chromedriver = paths[1] if len(paths) > 1 else None

# Verifica se o caminho para o chromedriver foi encontrado
if path_to_chromedriver:
    # Cria um objeto Service com o caminho para o chromedriver
    service = Service(executable_path=path_to_chromedriver)

    # Inicializa o navegador com as opções definidas
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Exemplo de uso: abrir uma página web (Google)
    driver.get("https://www.google.com")
    # Imprime o título da página no console
    print(driver.title)

    # Fecha o navegador
    driver.quit()
else:
    # Mensagem de erro se o caminho para o chromedriver não for encontrado
    print("O caminho para o chromedriver não foi encontrado.")
