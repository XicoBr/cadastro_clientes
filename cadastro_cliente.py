import tkinter as tk
import sqlite3
import pandas as pd

# pandas é usado para exportar o banco de dados para uma planilha

# conexao = sqlite3.connect("banco_clientes2.db")

# cursor = conexao.cursor()
#
# cursor.execute('''CREATE TABLE clientes (
#     nome text,
#     sobrenome text,
#     email text,
#     telefone text)
#
# ''')
#
# conexao.commit()
#
# conexao.close()


def cadastrar_cliente():
    pass
    conexao = sqlite3.connect('banco_clientes2.db')
    cursor = conexao.cursor()
    cursor.execute(" INSERT INTO clientes VALUES(:nome, :sobrenome, :email, :telefone)",
                   {
                    'nome': entry_nome.get(),
                    'sobrenome': entry_sobrenome.get(),
                    'email': entry_email.get(),
                    'telefone': entry_telefone.get()
                   })  # o dois-pontos é uma variável
    # temporária dentro do sql, que serve para puxar as informações da interface gráfica ;
    conexao.commit()
    conexao.close()
    entry_nome.delete(0, "end")
    entry_telefone.delete(0, "end")
    entry_email.delete(0, "end")
    entry_sobrenome.delete(0, "end")


def exporta_clientes():
    conexao = sqlite3.connect('banco_clientes2.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT *, oid FROM clientes")  # oid é a chave primária
    clientes_cadastrados = cursor.fetchall()
    clientes_cadastrados = pd.DataFrame(clientes_cadastrados, columns=['nome', 'sobrenome', 'email', 'telefone',
                                                                       'id_data'])
    clientes_cadastrados.to_excel('banco_clientes5.xlsx', engine='openpyxl')

    conexao.commit()
    conexao.close()


def abrir_tabela():
    pass


janela = tk.Tk()
janela.title("Ferramenta de Cadastro de Clientes")


# Labels
label_nome = tk.Label(janela, text="Nome")
label_nome.grid(row=0, column=0, pady=10)

label_sobrenome = tk.Label(janela, text="Sobrenome")
label_sobrenome.grid(row=1, column=0, pady=10)

label_email = tk.Label(janela, text="Email")
label_email.grid(row=2, column=0, pady=10)

label_telefone = tk.Label(janela, text="Telefone")
label_telefone.grid(row=3, column=0, pady=10)

# Entrys

entry_nome = tk.Entry(janela, width=30)
entry_nome.grid(row=0, column=1, pady=10)

entry_sobrenome = tk.Entry(janela, width=30)
entry_sobrenome.grid(row=1, column=1, pady=10)

entry_email = tk.Entry(janela, width=30)
entry_email.grid(row=2, column=1, pady=10)

entry_telefone = tk.Entry(janela, width=30)
entry_telefone.grid(row=3, column=1, pady=10)

# Buttons

botao_cadastrar = tk.Button(janela, text='Cadastrar cliente', width=30, command=cadastrar_cliente)
botao_cadastrar.grid(row=4, column=0, pady=10, columnspan=2, ipadx=70)

botao_exportar = tk.Button(janela, text='Exportar base de clientes', width=30, command=exporta_clientes)
botao_exportar.grid(row=5, column=0, pady=10, columnspan=2, ipadx=70)

botao_abrir = tk.Button(janela, text='Abrir tabela', width=30, command=abrir_tabela)
botao_abrir.grid(row=6, column=0, pady=10, columnspan=2, ipadx=70)
janela.mainloop()
