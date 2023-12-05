from playwright.sync_api import sync_playwright
import time

while(True):
    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=False)
        pagina = navegador.new_page()

        #login no linkedin
        pagina.goto("https://br.linkedin.com/")
        pagina.fill('xpath=//*[@id="session_key"]','email@gmail.com')
        pagina.fill('xpath=//*[@id="session_password"]','SENHA')

        #acessando perfil e procurando por emprego na aba "search"
        pagina.locator('xpath=//*[@id="main-content"]/section[1]/div/div/form[1]/div[2]/button').click()
        pagina.locator('xpath=/html/body/div[5]/div[3]/div/div/div[2]/div/div/div/div[1]/div[1]/a/div[2]').click()
        pagina.fill('xpath=//*[@id="global-nav-typeahead"]/input', 'Engenheiro de dados')
        pagina.keyboard.press('Enter')

        #selecionando "vagas"
        pagina.locator('xpath=//*[@id="search-reusables__filters-bar"]/ul/li[1]/button').click()

        #selecionando nivel de experiencia "junior"
        pagina.locator('xpath=/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[4]/div/span/button').click()
        pagina.locator('xpath=/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[4]/div/div/div/div[1]/div/form/fieldset/div[1]/ul/li[3]/label').click()
        pagina.locator('xpath=/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[4]/div/div/div/div[1]/div/form/fieldset/div[2]/button[2]').click()

        time.sleep(99999); time.sleep(99999); time.sleep(99999); time.sleep(99999)
        time.sleep(99999); time.sleep(99999); time.sleep(99999); time.sleep(99999)
        time.sleep(99999); time.sleep(99999); time.sleep(99999); time.sleep(99999)
        time.sleep(99999); time.sleep(99999); time.sleep(99999); time.sleep(99999)
