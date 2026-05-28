import pyautogui
from shared.constants import HELICOPTER
import time

helicopter = 0
capturados = set()

def helicopter_scrapper(page):
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
                        print("TOTAL:", helicopter)
                        pyautogui.dragRel(100, 0, duration=0.5)
                        time.sleep(2)
                        if helicopter >= 2:
                            break
                    else:
                        print("NÃO ENCONTROU")
                except Exception as e:
                    print("ERRO:", e)