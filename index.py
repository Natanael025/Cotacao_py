# Algoritmo que pega cotação de moeda n em real e vice-versa
# Athor: Natanael Vieira
# Date: 28/09/2026

import requests # Biblioteca para entrar no site
from bs4 import BeautifulSoup # Raspa o conteúdo da página

moedas = ['eur', 'usd', 'mxn', 'inr', 'cad', 'aoa', 'bnd', 'jpy', 'kwd']

# exbindo as moedas
for moeda in moedas:
  url = f'https://wise.com/br/currency-converter/{moeda}-to-brl-rate?amount=1'
  requisicao = requests.get(url) # Tentando entrar no site
  site = BeautifulSoup(requisicao.text, 'html.parser') # pega o html do site
  divMae = site.find('div', class_='preset--light') # Acha a div que contem as informações da cotação
  # Acha as inputs com as mesmas caracteristicas
  cotacao = divMae.find_all('input', class_='form-control np-form-control np-form-control--size-auto np-input np-input--shape-rectangle')
  print(cotacao[1]['value']) # exibe a cotação atual da moeda
