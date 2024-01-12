import pandas as pd
import pyautogui as py

pick = pd.read_excel(r"C:\Users\rayde\OneDrive\Ambiente de Trabalho\pick retorno a movimentar.xlsx")
print(pick)

for _, row in pick.iterrows():
    produto = str(row["Produto"])
    quantidade = str(row["Quantidade"])
    py.moveTo(x=80, y=610)
    py.doubleClick()
    py.sleep(0.1)
    py.write(produto)
    py.press(['enter', 'enter'], interval=0.1)
    py.write(quantidade, interval=0.1)
    py.press(['enter', 'enter'], interval=0.1)
    py.sleep(0.4)

py.alert("Processo concluído. Por favor, confira a quantidade de volumes antes de processar o movimento de estoque.")