import pandas as pd
import pyautogui as py

def clica_apaga():
    py.doubleClick()
    py.press('backspace')
    py.doubleClick()
    py.press('backspace')

def lerCargas():
    cargas = pd.read_excel(r"C:\Users\rayde\OneDrive\Ambiente de Trabalho\cargas a finalizar.xlsx") # Lê a planilha
    return cargas["Carga PV"] # Retorna a coluna "Carga PV"

def finalizarCargas(cargas_pv):
    for carga in cargas_pv:
        py.moveTo(x=40, y=166)
        clica_apaga()
        clica_apaga()
        py.write(str(carga))
        py.press('enter')
        py.sleep(3)
        py.moveTo(x=66, y=672)
        py.click()
        py.sleep(3)
        py.moveTo(x=693, y=207)
        py.sleep(3)
        py.doubleClick()
        py.hotkey('ctrl', 'c')
        py.hotkey('ctrl', 'c')
        py.hotkey('ctrl', 'c')
        py.press('tab')
        py.sleep(4)
        py.hotkey('ctrl', 'v')
        py.press('tab')
        py.sleep(4)
        py.press('tab')
        py.sleep(5)
        py.moveTo(x=563, y=588)
        py.click()
        py.sleep(12)

try:
    cargas_pv = lerCargas()
    finalizarCargas(cargas_pv)
    py.alert('CARGAS FINALIZADAS!')
except Exception as erro:
    print(f"Ocorreu uma exceção: {str(erro)}")
    py.alert('Processo interrompido!')