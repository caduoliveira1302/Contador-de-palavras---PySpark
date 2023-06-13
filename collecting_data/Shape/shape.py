from playwright.sync_api import Playwright, sync_playwright, expect
import time


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.shape.com/search?q=whey+protein")

    # Acessa o primeiro artigo

    page.query_selector('//*[@id="mntl-card-list-items_2-0"]/div[2]/span').click()
    time.sleep(5)
    texto = page.locator('//*[@id="article-content_1-0"]').text_content()

    # Cria e adiciona o primeiro artigo ao csv

    with open('shape.txt', 'w', encoding='utf-8') as f:
        f.write('Artigo 1\n')
        f.write(texto)
    page.goto("https://www.shape.com/search?q=whey+protein")
    
    # Acessa outros artigos
    
    for x in range(1,24):

        page.goto("https://www.shape.com/search?q=whey+protein")
        page.query_selector(f'//*[@id="mntl-card-list-items_2-0-{x}"]/div[2]/span').click()
        try:
            texto = page.locator('//*[@id="article-content_1-0"]').text_content(timeout=15000)
            with open('shape.txt', 'a', encoding='utf-8') as f:
                f.write(f'Artigo {x}\n')
                f.write(texto)

                page.goto("https://www.shape.com/search?q=whey+protein")
        except:
             pass

    




    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
