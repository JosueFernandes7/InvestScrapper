from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options as FirefoxOptions

options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

driver.get("https://statusinvest.com.br/acoes/petr4")
elem = driver.find_element(By.XPATH, "/html/body/main/div[3]/div/div[1]/div[2]/div[7]/div/div[2]/table")
soup = BeautifulSoup(elem.get_attribute('innerHTML'),  'html.parser').find_all('td')

vetLinha = []
linha = []
i = 1
for l in soup:
    if (i >= 1 and i <= 4):
        linha.append(l.string)
        i = i + 1
    else:
        vetLinha.append(linha)
        linha = []   
        linha.append(l.string)     
        i = 2 

data_inicio = "08/2023";
for aux in vetLinha:
    data_formatada = aux[1].split("/")[1] + "/" + aux[1].split("/")[2]
    if (data_formatada == data_inicio): 
        print(aux)