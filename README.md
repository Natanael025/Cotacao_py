# Conversor de Moedas

Este projeto consiste em um algoritmo desenvolvido em **Python** que realiza o raspamento de dados (*web scraping*) no site da Wise para capturar as cotações em tempo real de diversas moedas estrangeiras em relação ao Real Brasileiro (BRL).

## Autor

* **Autor:** Natanael Vieira
* **Data:** 28/09/2026

## Funcionalidades

* **Scraping em Tempo Real:** Consulta a cotação atualizada diretamente da plataforma Wise.
* **Múltiplas Moedas:** Suporte para consulta em lote de diversas moedas globais:
  * Euro (`EUR`)
  * Dólar Americano (`USD`)
  * Peso Mexicano (`MXN`)
  * Rúpia Indiana (`INR`)
  * Dólar Canadense (`CAD`)
  * Kwanza Angolano (`AOA`)
  * Dólar de Brunei (`BND`)
  * Iene Japonês (`JPY`)
  * Dinar Kuwaitiano (`KWD`)

## Tecnologias e Bibliotecas

* **[Python 3](https://www.python.org/)**
* **[Requests](https://requests.readthedocs.io/):** Responsável por realizar as requisições HTTP nas páginas da web.
* **[BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/):** Utilizado para extrair e navegar no HTML da página (*parsing*).

## Pré-requisitos

Certifique-se de ter o **Python 3** instalado em sua máquina.

### Instalação de Dependências

Antes de executar o script, instale as bibliotecas necessárias executando no terminal:

```bash
pip install requests beautifulsoup4
```

## Como Executar

1. **Clone o repositório ou baixe o arquivo `.py`:**
   ```bash
   git clone https://github.com/seu-usuario/conversor-cotacao-python.git
   cd conversor-cotacao-python
   ```

2. **Execute o script:**
   ```bash
   python main.py
   ```

3. **Saída Esperada:**
   O programa irá percorrer a lista de moedas e exibir no terminal o valor convertido para R$ (BRL) para cada uma delas.

---

Todos os direitos reservados &copy 2026
