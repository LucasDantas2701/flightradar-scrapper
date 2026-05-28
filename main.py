import os
from playwright.sync_api import (Playwright)
from modules.context.main import create_context
from modules.plane_scrapper.main import plane_scrapper
from modules.helicopter_scrapper.main import helicopter_scrapper
from shared.constants import URL, STATE_PATH

def run(playwright: Playwright) -> None:
    #setup browser
    browser = playwright.chromium.launch(headless=False, args=["--disable-blink-features=AutomationControlled", "--start-maximized"])
    context = browser.new_context(viewport={"width": 1366, "height": 768}, user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36", locale="pt-BR", timezone_id="America/Manaus", permissions=["geolocation"], color_scheme="dark")
    context.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    #cria contexto
    if not os.path.exists(STATE_PATH):
        create_context(browser)

    #abre o site
    context = browser.new_context(storage_state=STATE_PATH)
    page = context.new_page()
    page.goto(URL)
    page.get_by_test_id("panel-selector__settings").click()
    page.get_by_test_id("image-toggle-black_white__button").click()
    page.get_by_role("slider").first.fill("0")

    #executa as funções
    plane_scrapper(page)
    helicopter_scrapper(page)

    #fecha o browser
    context.close()
    browser.close()