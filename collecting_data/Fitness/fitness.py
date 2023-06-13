from playwright.sync_api import Playwright, sync_playwright, expect
import time


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.fitnessandpower.com/category/bodybuilding-supplements")
    
    page.get_by_role("link", name="Supplements", exact=True).click()
    
    page.query_selector('//*[@id="content_box"]/article[1]/header/h2/a').click()
    time.sleep(5)
    

    texto = page.locator('//*[@id="page"]/article').text_content()

    with open('Fitness.txt', 'w', encoding='utf-8') as f:
        f.write('Artigo 1\n')
        f.write(texto)


    page.goto("https://www.fitnessandpower.com/category/bodybuilding-supplements")
    
    for x in range(2,11):
    
        page.query_selector(f'//*[@id="content_box"]/article[{x}]/header/h2/a').click()
        time.sleep(5)
    
        texto = page.locator('//*[@id="page"]/article').text_content()
    
        with open('Fitness.txt', 'a', encoding='utf-8') as f:
            f.write(f'Artigo {x}\n')
            f.write(texto)
        page.goto("https://www.fitnessandpower.com/category/bodybuilding-supplements")
    
    
    
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
