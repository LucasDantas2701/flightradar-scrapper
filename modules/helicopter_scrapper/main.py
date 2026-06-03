import pyautogui
from shared.constants import HELICOPTER
import time
import ctypes
import os

ctypes.windll.shcore.SetProcessDpiAwareness(1)
os.makedirs("assets/img/screenshots-helicopter", exist_ok=True)

def helicopter_scrapper(page):
    helicopter = 0
    capturados = set()
    while helicopter < 3:
        for imagem in HELICOPTER:
            try:
                resultado = pyautogui.locateOnScreen(imagem, confidence=0.8)
                if resultado:
                    centro = pyautogui.center(resultado)
                    pyautogui.click(centro)
                    time.sleep(3)  # esperar painel abrir
                    codigo = page.get_by_test_id("aircraft-panel__header__callsign").inner_text().strip()
                    if not codigo:
                        time.sleep(1)
                        codigo = page.get_by_test_id("aircraft-panel__header__callsign").inner_text().strip()
                        if not codigo:
                            print("Painel sem callsign, ignorando.")
                            continue
                    partida = page.get_by_test_id("aircraft-panel__airport-departure-iata").inner_text()
                    chegada = page.get_by_test_id("aircraft-panel__airport-arrival-iata").inner_text().strip()
                    if codigo in capturados:
                        print("Já capturado:", codigo)
                        continue
                    print(f"{partida} -> {chegada} | {codigo}")
                    pyautogui.screenshot(f"assets/img/screenshots-helicopter/{codigo}.png")
                    capturados.add(codigo)
                    helicopter += 1
                    print("TOTAL:", helicopter)

                    pyautogui.dragRel(100, 0, duration=0.5)
                    time.sleep(1)

                    if helicopter >= 2:
                        break
                else:
                    print(f"NÃO ENCONTROU: {imagem}")
            except Exception as e:
                print("ERRO:", e)
        time.sleep(0.5)
