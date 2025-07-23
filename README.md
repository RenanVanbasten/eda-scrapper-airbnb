# 🏡 Airbnb Web Scraping e Análise de Dados

Este projeto realiza a extração (web scraping) de dados de hospedagens na plataforma Airbnb e desenvolve uma análise exploratória utilizando bibliotecas como Selenium, BeautifulSoup, Pandas e Seaborn.

---

## 📅 Sobre os dados

Os dados foram **coletados via scraping** no dia **22 de julho de 2025**, por volta das **21h (horário de Brasília)**, a partir de uma pesquisa por acomodações em **Copacabana (RJ)** para estadias **flexíveis (uma semana) durante o mês de dezembro de 2025**.

⚠️ Como o Airbnb atualiza seus anúncios com frequência, **os resultados obtidos aqui são apenas uma amostra momentânea**. Se você executar o código novamente, os dados coletados serão provavelmente diferentes.

---

## 📁 Estrutura do Projeto

```text
airbnb_project/
├── data/             # Dados brutos (.csv)
│   └── airbnb_listings.csv
├── notebooks/        # Análises exploratórias com Jupyter
│   └── analysis.ipynb
├── reports/
│   ├── images/
│   │   ├── distribuicao_precos.png
│   │   └── preco_vs_avaliacao.png
│   └── report.md
├── scripts/          # Código de scraping em Python
│   └── scraping.py
└── README.md         # Este arquivo

```

## 📊 Objetivos

- Praticar técnicas de coleta de dados com `Selenium` e `BeautifulSoup`
- Criar uma base de dados local de hospedagens
- Realizar Análise Exploratória dos Dados (AED)
- Visualizar distribuição de preços, avaliações e descrições

---

## 📈 Principais análises feitas

- Quantidade de anúncios encontrados
- Distribuição de preços por noite
- Médias de avaliações dos hóspedes
- Exploração de títulos e descrições das acomodações

---

## 📄 Relatório final

As conclusões e insights obtidos a partir da análise estão descritos no arquivo:  /reports/report.md

---

## 📎 Observações
Este projeto tem fins educacionais.

Os dados foram coletados de forma não autenticada e pública.

Nenhuma automação de login, compra ou reserva foi realizada.