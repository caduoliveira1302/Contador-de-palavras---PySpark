from playwright.sync_api import Playwright, sync_playwright, expect
import time


def run(playwright: Playwright) -> None:
    
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.muscleandfitness.com/", timeout=90000)
    page.locator(".icon").click()
    page.get_by_placeholder("Start typing to search…").click()
    page.get_by_placeholder("Start typing to search…").fill("whey protein")
    page.get_by_role("search", name="Type and press Enter to search").get_by_role("button", name="Search").click()
    
    # Criei uma exeção por conta de um banner da página
    
    try:
        page.get_by_role("button", name="I don't want to be cut; close the dialog").click()
    except:
        pass    
    
    # Entro no primeiro artigo
    
    page.query_selector('//*[@id="ae-main-content"]/div/div/div[1]/div/article[1]/div/h3').click()
    texto = page.locator('//*[@id="page-box"]/div[1]/div[1]/div[2]/div/div[3]').text_content()
    
    # Crio o csv 'MuscleandFitness.csv'

    with open('muscleandfitness.txt', 'w', encoding='utf-8') as f:
        f.write('Artigo 1\n')
        f.write(texto)
    # Crio um laço de repetição para entrar e adicionar as informações no csv MuscleandFitness

    for x in range(2,11):

        page.goto("https://www.muscleandfitness.com/search/?search=whey+protein")
        time.sleep(10)
        page.query_selector(f'//*[@id="ae-main-content"]/div/div/div[1]/div/article[{x}]/div/h3').click()
        texto = page.locator('//*[@id="page-box"]/div[1]/div[1]/div[2]/div/div[3]').text_content()
        
        with open('muscleandfitness.txt', 'a', encoding='utf-8') as f:
            f.write(f'Artigo {x}\n')
            f.write(texto)
    
    
    # ---------------------
    context.close()
    browser.close()

 


with sync_playwright() as playwright:
    run(playwright)