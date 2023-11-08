# *** PARA PRODUÇÃO NO REMMINA  ***
# ***   ATUALIZADO EM 26/10/2023 - BIG LINUX  ***

import pyautogui as py

# define a velocidade com a qual a automação vai proceder
quick = py.confirm('Qual a velocidade atual do sistema?', buttons = ['Rápido', 'Lento'])
if quick == 'Rápido':
    tempo = 2.5
else:
    tempo = 6

# coleta do usuário a primeira e a última carga a serem adicionadas as vendas
cg_inicial = int(py.prompt("Carga Inicial:"))
cg_final = int(py.prompt("Carga Final:"))

# cria uma lista com o intervalo das cargas fornecidas
lista_cargas = list(range(cg_inicial, cg_final+1))

# percorre a lista das cargas adicionando as vendas
for carga in lista_cargas:
    py.click(x=48, y=208, clicks=2) # campo Carga
    py.sleep(tempo)
    py.press('backspace')
    py.click(x=48, y=208, clicks=2) # campo Carga
    py.sleep(1)
    py.press('backspace')
    py.sleep(tempo)
    py.write(str(carga))
    py.press('enter')
    py.sleep(tempo)
    py.press('f2')
    py.sleep(tempo)
    py.click(x=573, y=354) # clica na tela antes do ctrl + a
    py.sleep(tempo)
    py.hotkey('ctrl', 'a')
    py.sleep(tempo)
    py.press('enter')
    py.sleep(tempo)
    py.press('esc')
    py.sleep(tempo)

# mensagem final após conclusão
py.alert("Processo concluído!")