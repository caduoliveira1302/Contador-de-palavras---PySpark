from playwright.sync_api import Playwright, sync_playwright, expect
import time
import csv

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.livestrong.com/")
    
    # Realiza a pesquisa da palavra desejada

    page.locator(".global-nav-search-and-login > .svg").click()
    page.get_by_placeholder("Search Livestrong.com").fill("whey protein")
    page.get_by_placeholder("Search Livestrong.com").press("Enter")
    time.sleep(5)

    # Acessa o primeiro artigo
    
    page.query_selector('//*[@id="app"]/div[2]/main/div/div/div[2]/div[2]/div[1]').click()
    texto = page.locator('//*[@id="app"]/div[2]/main/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/article').text_content()
    #page.goto("https://www.livestrong.com/search/?search=whey%20protein")
    #time.sleep(5)

    # Crio o csv 'livestrong.csv'

    with open('livestrong.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Artigo', 'Texto'])
        writer.writerow(['Artigo 1', texto])
    
    #Crio um laço de repetição para entrar e adicionar as informações no csv livestrong.csv
    
    for x in range(2,11):

        page.goto("https://www.livestrong.com/search/?search=whey%20protein")
        time.sleep(5)
        page.query_selector(f'//*[@id="app"]/div[2]/main/div/div/div[2]/div[2]/div[{x}]').click()
        texto = page.locator('//*[@id="app"]/div[2]/main/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/article').text_content()

        with open('livestrong.csv', 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow([f'Artigo {x}', texto])


    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
