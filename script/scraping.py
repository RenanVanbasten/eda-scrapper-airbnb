import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pandas as pd
import re

# Configurando o navegador
chrome_options = Options()
chrome_options.add_argument('window-size=1200,900')
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=chrome_options)

try:
    # Acessa a página inicial
    browser.get('https://www.airbnb.com.br')
    browser.maximize_window()
    sleep(2)

    # Aceita cookies
    browser.find_element(By.XPATH, "//button[text()='Aceitar todos']").click()
    sleep(1)

    # Scroll para ocultar alertas visuais
    browser.execute_script("window.scrollBy(0, 300);")
    sleep(1.5)
    browser.execute_script("window.scrollBy(0, -300);")
    sleep(1.5)

    # Preenche o campo de destino
    location_input = browser.find_element(By.XPATH, "//input[@id='bigsearch-query-location-input']")
    location_input.send_keys('Copacabana')
    sleep(2)

    # Abre seletor de datas
    browser.find_element(By.XPATH, "//div[text()='Insira as datas']").click()
    sleep(1)

    # Seleciona busca por datas flexíveis
    browser.find_element(By.XPATH, "//button[text()='Flexível']").click()
    sleep(1)
    browser.find_element(By.XPATH, "//label[text()='Uma semana']").click()
    sleep(1)
    browser.find_element(By.XPATH, "//button[.//span[text()='dezembro'] and .//span[text()='2025']]").click()
    sleep(1)

    # Clica no botão de busca
    search_btn = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='structured-search-input-search-button']"))
    )
    search_btn.click()
    sleep(2)

    # Fecha o pop-up "Entendi", se existir
    browser.find_element(By.XPATH, "//button[text()='Entendi']").click()
    sleep(2)

    # Coleta HTML da página
    page_html = browser.page_source
    soup = BeautifulSoup(page_html, 'html.parser')

    listings = soup.find_all('div', class_='c965t3n atm_9s_11p5wf0 atm_dz_1osqo2v dir dir-ltr')
    results = []

    if listings:
        print(f"\nEncontrados {len(listings)} resultados.")
        for card in listings:
            title = None
            subtitle = None
            rating = None
            price = None

            # Título
            title_tag = card.find('div', attrs={'data-testid': 'listing-card-title'})
            if title_tag:
                title = title_tag.text.strip()

            # Subtítulo
            subtitle_tag = card.find('span', attrs={'data-testid': 'listing-card-name'})
            if subtitle_tag:
                subtitle = subtitle_tag.text.strip()

            # Avaliação
            rating_div = card.find('div', class_='t1a9j9y7')
            if rating_div:
                rating_span = rating_div.find('span', class_='a8jt5op')
                if rating_span:
                    rating = rating_span.text.strip().replace(" de uma avaliação média de 5,", "").replace(" de 5,", "")
                else:
                    match = re.search(r'(\d,\d{2})\s*\((\d+)\)', rating_div.text.strip())
                    if match:
                        rating = f"{match.group(1)} ({match.group(2)})"
                    else:
                        rating = "N/A"

            # Preço por noite
            price_tag = card.find('span', class_='umg93v9')
            if price_tag:
                price = price_tag.text.strip()
            else:
                alt_price = card.find('span', string=lambda text: text and 'R$' in text)
                if alt_price:
                    match = re.search(r'R\$\s*([\d\.,]+)', alt_price.text)
                    if match:
                        price = match.group(0).strip()

            results.append({
                'titulo': title,
                'descricao': subtitle,
                'avaliacao': rating,
                'preco_noite': price
            })

        # Converte para DataFrame
        df = pd.DataFrame(results)
        print("\n--- Resultados ---")
        print(df.to_string())
        df.to_csv('data/airbnb_listings.csv', index=False, encoding='utf-8')
    else:
        print("\nNenhum resultado encontrado.")

except Exception as e:
    print(f"Erro: {e}")
