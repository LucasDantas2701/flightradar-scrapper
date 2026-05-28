import pyautogui
from shared.constants import PLANE
import time

plane = 0
capturados = set()

def plane_scrapper(page):
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