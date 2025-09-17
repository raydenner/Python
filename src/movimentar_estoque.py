import pandas as pd
import pyautogui as py

pick = pd.read_excel(r"/home/ray/Py/Python/data/pick_devolucoes.xlsx")
pick.info()

for _, row in pick.iterrows():
    produto = str(row["Produto"])
    quantidade = str(row["Quantidade"])
    py.moveTo(x=71, y=656) # campo Produto
    py.doubleClick()
    py.sleep(0.1)
    py.write(produto)
    py.press(['enter', 'enter'], interval=0.1)
    py.write(quantidade, interval=0.1)
    py.press(['enter', 'enter'], interval=0.1)
    py.sleep(0.4)

py.alert("Inserção concluída. Confira a quantidade de volumes antes de processar o movimento de estoque.")
