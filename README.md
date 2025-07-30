# 🏡 Airbnb Web Scraping e Análise de Dados

Este projeto realiza a extração (web scraping) de dados de hospedagens na plataforma Airbnb e desenvolve uma análise exploratória utilizando bibliotecas como Selenium, BeautifulSoup, Pandas e Seaborn.

---

## 📅 Sobre os dados

Os dados foram **coletados via scraping** no dia **23 de julho de 2025**, por volta das **20h (horário de Brasília)**, a partir de uma pesquisa por acomodações em **Copacabana (RJ)** para estadias **flexíveis (uma semana) durante o mês de dezembro de 2025**.

⚠️ Como o Airbnb atualiza seus anúncios com frequência, **os resultados obtidos aqui são apenas uma amostra momentânea**. Se você executar o código novamente, os dados coletados serão provavelmente diferentes.

### Desafios e Manutenção do Scraping

É importante notar que, devido à natureza dinâmica de plataformas como o Airbnb, as classes HTML utilizadas para identificar elementos na página podem ser alteradas. Durante o desenvolvimento deste projeto, foi necessária uma **atualização no script de scraping (`script/scraping.py`)** para adaptar-se a uma mudança na classe específica que capturava as avaliações dos imóveis. Essa modificação foi crucial para garantir a coleta correta e completa dos dados, permitindo a continuidade da Análise Exploratória de Dados (EDA) com informações precisas.

---

## ⚙️ Sobre o ETL (`scripts/etl_airbnb.py`)

Para tornar o processo de tratamento dos dados mais modular e reutilizável, foi criado um **script separado de ETL (Extract, Transform, Load)**.  

Esse script realiza:

- **`extract()`**: leitura do arquivo bruto `.csv` com os dados coletados.
- **`transform()`**: limpeza e transformação das colunas, como separação das notas e número de avaliações, e padronização dos preços.
- **`load()`**: exportação do novo DataFrame limpo para outro arquivo `.csv`.

Com isso, o Jupyter Notebook (`notebooks/analysis.ipynb`) fica mais focado **nas análises visuais**, e todo o pré-processamento de dados fica isolado e reutilizável no script ETL.

---

## 📁 Estrutura do Projeto

```text
airbnb_project/
├── data/             # Dados brutos (.csv)
│   └── airbnb_listings.csv
├── notebooks/        # Análises exploratórias com Jupyter
│   └── analysis.ipynb
├── reports/          # Relatórios e visualizações geradas
│   ├── images/
│   │   ├── distribuicao_precos.png
│   │   └── preco_vs_avaliacao.png
│   └── report.md
├── scripts/          # Scripts Python (scraping e ETL)
│   └── scraping.py
│   └── etl_airbnb.py
└── README.md         # Este arquivo
└── requirements.txt  # Bibliotecas necessárias para rodar o projeto

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
- Boxplot de preços por noite
- Dispersão entre preço e número de avaliações
- Exploração de títulos e descrições das acomodações

---

## 📄 Relatório final

As conclusões e insights obtidos a partir da análise estão descritos no arquivo:  /reports/report.md

---

## 📎 Observações
Este projeto tem fins educacionais.

Os dados foram coletados de forma não autenticada e pública.

Nenhuma automação de login, compra ou reserva foi realizada.