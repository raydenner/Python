import pandas as pd
import pyautogui as py

def realizar_clicar_sono(x, y, clicks=2, intervalo=4):
    py.click(x=x, y=y, clicks=clicks)
    py.sleep(intervalo)

def inativar_itens_sem_saldo():
    for produto in tabela['Código']:
        realizar_clicar_sono(249, 169)
        py.press('backspace')
        py.write(str(produto))
        py.sleep(5)
        py.press('enter')
        py.sleep(4)
        realizar_clicar_sono(102, 66) # Editar
        py.moveTo(x=288, y=548) # Necessário mover; clicando não seleciona
        py.click() # Carrega PDA
        py.sleep(2)
        realizar_clicar_sono(156, 66) # Gravar checkbox
        py.sleep(4)

try:
    tabela = pd.read_excel(r"C:\Users\rayde\OneDrive\Ambiente de Trabalho\itens a inativar.xlsx")
    inativar_itens_sem_saldo()

except py.FailSafeException:
    py.alert("Processo Abortado!")

finally:
    py.alert("   Processo Concluído! \n   RD Soluções em Software")
