import pyautogui as py
import ctypes as ct

# define a velocidade com a qual a automação vai proceder
tempo = 3

# coleta do usuário a primeira e a última carga a serem adicionadas as vendas
cg_inicial = int(py.prompt("Carga Inicial:"))
cg_final = int(py.prompt("Carga Final:"))

# cria uma lista com o intervalo das cargas fornecidas
lista_cargas = list(range(cg_inicial, cg_final+1))

# percorre a lista das cargas adicionando as vendas
for carga in lista_cargas:
    py.click(x=42, y=171, clicks=2)
    py.sleep(tempo)
    py.press('backspace')
    py.click(x=42, y=171, clicks=2)
    py.sleep(2)
    py.press('backspace')
    py.sleep(tempo)
    py.write(str(carga))
    py.press('enter')
    py.sleep(tempo)
    py.press('f2')
    py.sleep(tempo)
    py.click(x=558, y=336)
    py.sleep(tempo)
    py.hotkey('ctrl', 'a')
    py.sleep(tempo)
    py.press('enter')
    py.sleep(tempo)
    py.press('esc')
    py.sleep(tempo)

# mensagem final após conclusão
ct.windll.user32.MessageBoxW(None, "   Processo Concluído! \n  RD SOLUÇÕES EM T.I.", "ADICIONAR VENDAS - CARGAS PV", 0x40 | 0x0)
