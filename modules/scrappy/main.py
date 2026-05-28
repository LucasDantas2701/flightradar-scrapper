import os
import time
import pyautogui
from playwright.sync_api import (Playwright,sync_playwright)
from shared.constants import URL, PLANE, HELICOPTER

STATE_PATH = "assets/json/auth.json"

def run(playwright: Playwright) -> None:

    browser = playwright.chromium.launch(headless=False, args=["--disable-blink-features=AutomationControlled", "--start-maximized"])
    context = browser.new_context(viewport={"width": 1366, "height": 768}, user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36", locale="pt-BR", timezone_id="America/Manaus", permissions=["geolocation"], color_scheme="dark")
    context.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    if not os.path.exists(STATE_PATH):
        context = browser.new_context()
        page = context.new_page()
        page.goto(URL)
        try:
            page.get_by_role("button",name="Agree and close").click(timeout=3000)
        except:
            pass
        try:
            page.get_by_role("button",name="Close").click(timeout=3000)
        except:
            pass
        context.storage_state(path=STATE_PATH)
        context.close()

    context = browser.new_context(storage_state=STATE_PATH)
    page = context.new_page()
    page.goto(URL)
    page.get_by_test_id("panel-selector__settings").click()
    page.get_by_test_id("image-toggle-black_white__button").click()
    page.get_by_role("slider").first.fill("0")
    plane = 0
    helicopter = 0
    capturados = set()

    while plane < 6:
        for imagem in PLANE:
            try:
                resultado = pyautogui.locateOnScreen(imagem, confidence=0.7)
                if resultado:
                    centro = pyautogui.center(resultado)
                    pyautogui.click(centro)
                    time.sleep(1)
                    codigo = page.get_by_test_id("aircraft-panel__header__callsign").inner_text()
                    partida = page.get_by_test_id("aircraft-panel__airport-departure-iata").inner_text()
                    chegada = page.get_by_test_id("aircraft-panel__airport-arrival-iata").inner_text()
                    if not codigo:
                        continue
                    if codigo in capturados:
                        print("Já capturado:", codigo)
                        continue
                    print(f"{partida} -> {chegada} | {codigo}")
                    pyautogui.screenshot(f"assets/img/screenshots-plane/{codigo}.png")
                    capturados.add(codigo)
                    plane += 1
                    print("TOTAL:", plane)
                    pyautogui.dragRel(100, 0, duration=0.5)
                    time.sleep(2)
                    if plane >= 5:
                        print("FINALIZADO")
                        break
                else:
                    print("NÃO ENCONTROU")
            except Exception as e:
                print("ERRO:", e)


    while helicopter < 6:
        for imagem in HELICOPTER:
            try:
                resultado = pyautogui.locateOnScreen(imagem, confidence=0.7)
                if resultado:
                    centro = pyautogui.center(resultado)
                    pyautogui.click(centro)
                    time.sleep(1)
                    codigo = page.get_by_test_id("aircraft-panel__header__callsign").inner_text()
                    partida = page.get_by_test_id("aircraft-panel__airport-departure-iata").inner_text()
                    chegada = page.get_by_test_id("aircraft-panel__airport-arrival-iata").inner_text().strip()
                    if not codigo:
                        continue
                    if codigo in capturados:
                        print("Já capturado:", codigo)
                        continue
                    print(f"{partida} -> {chegada} | {codigo}")
                    pyautogui.screenshot(f"assets/img/screenshots-helicopter/{codigo}.png")
                    capturados.add(codigo)
                    helicopter += 1
                    print("TOTAL:", plane)
                    pyautogui.dragRel(100, 0, duration=0.5)
                    time.sleep(2)
                    if helicopter >= 2:
                        break
                else:
                    print("NÃO ENCONTROU")
            except Exception as e:
                print("ERRO:", e)

    context.close()
    browser.close()
