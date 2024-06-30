import tkinter as tk
import sqlite3
import pandas as pd
import openpyxl
from openpyxl import Workbook, load_workbook
import numpy
# planilha = load_workbook("banco_clientes5.xlsx")
# aba_ativa = planilha.active
# for celula in aba_ativa['C']:
#     print(celula.value)
tabela = pd.read_excel("banco_clientes5.xlsx")
# for infos in tabela:
#     print(f'{infos}', end=' ' * 5)
print()
display(tabela)
