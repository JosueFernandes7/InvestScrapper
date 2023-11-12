from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from bs4 import BeautifulSoup
from datetime import datetime
from core.settings import settings
import math

def buscaDados(tipo,nome,valor):

  total = 0
  # Configurações do navegador Firefox em modo headless
  options = FirefoxOptions()
  options.add_argument("--headless")

  # Inicializa o driver do Firefox
  driver = webdriver.Firefox(options=options)

  # Abre a página desejada
  url = f"{settings.API_BASE_URL}/{tipo}/{nome}"
  driver.get(url)

  # Localiza os elementos usando XPath
  valor_atual = driver.find_element(By.XPATH, settings.XPATH_VALOR_ATUAL)
  rendimento_mensal = driver.find_element(By.XPATH, settings.XPATH_RENDIMENTO_MENSAL)
  alteracao_atual = driver.find_element(By.XPATH, settings.XPATH_ALTERACAO_ATUAL)
  table_element = driver.find_element(By.XPATH, settings.XPATH_TABLE)

  # Extrai o HTML da tabela
  table_html = table_element.get_attribute('innerHTML')

  # Parseia o HTML usando BeautifulSoup
  soup = BeautifulSoup(table_html, 'html.parser')
  rows = soup.find_all('tr')

  # Lista para armazenar os dicionários de dividendos
  dividendos = []

  # Itera sobre as linhas da tabela
  for row in rows[1:]:  # Ignora a primeira linha (cabeçalho)
      columns = row.find_all('td')
      tipo_ganho, data, data_pagamento, valor_recebido = [col.text.strip() for col in columns]

      formato = "%d/%m/%Y"
      dataAtual = datetime.now().strftime(formato)
      # teste = datetime.strptime("20/03/2024", formato)
      data_pagamento_formatada = datetime.strptime(data_pagamento, formato)

      # se recebe o dividendo hoje entra no calculo
      if data_pagamento_formatada == dataAtual:
          dividendo = {
              "Tipo": tipo_ganho,
              "Data": data,
              "Data de Pagamento": data_pagamento,
              "Valor": float(valor_recebido.replace(",","."))
          }
          dividendos.append(dividendo)

  print(f"VALOR ATUAL: {valor_atual.text}, Alteracao Em relação ao dia anterior: {alteracao_atual.text}, Rendimento Mensal: {rendimento_mensal.text}")

  variacao = (100 + float(alteracao_atual.text.replace("%","").replace(",","."))) / 100
  total = valor * variacao

  if dividendos:
    cotas = math.floor(total / float(valor_atual.text.replace(",",".")))
    for dividendo in dividendos:
        total += cotas * dividendo["Valor"]

  return {
   "total" : round((total), 2),
   "valor_Investido" : valor,
   "mod" : round((total - valor), 2),
   "valorizacao" : rendimento_mensal.text
 }

      