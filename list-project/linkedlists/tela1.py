# -*- coding: utf-8 -*-

import customtkinter as cttk
import subprocess
import os
import webbrowser

script_directory = os.path.dirname(os.path.abspath(__file__))

app = cttk.CTk() 
app.geometry("1100x780")

app.title("Projeto de Listas - Estrutura de dados")

# criando frames
app.mainframe = cttk.CTkFrame(app, width=140, height=140, corner_radius=0)
app.mainframe.grid(row=4, column=0, columnspan=3, sticky="nsew")
#app.mainframe.grid_rowconfigure(4, weight=1)

app.selectionframe = cttk.CTkFrame(app, width=140, height=140, corner_radius=0)
app.selectionframe.grid(row=2, column=0, columnspan=3, sticky="nsew")
#app.selectionframe.grid_rowconfigure(4, weight=1)


app.grid_columnconfigure((0, 1, 2, 3), weight=1)
app.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

# default font
defaultfont = cttk.CTkFont(size=20, weight='bold')

# custom font
customFont = cttk.CTkFont(size=42, weight='bold')

# função para abrir ARQUIVOs lista sequencial
def open_ls():
    app.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(current_directory)
    tela2_path = os.path.join(parent_directory,'linkedlists', 'tela2.py')

    subprocess.call(["python", tela2_path, 'Lista Sequencial'])

# função para abrir lse
def open_lse():
    app.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(current_directory)
    tela2_path = os.path.join(parent_directory,'linkedlists', 'tela2.py')

    subprocess.call(["python", tela2_path, 'Lista Simplesmente Encadeada'])

# função para abrir lde
def open_lde():
    app.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(current_directory)
    tela2_path = os.path.join(parent_directory,'linkedlists', 'tela2.py')

    subprocess.call(["python", tela2_path, 'Lista Duplamente Encadeada'])


# funcao para abrir documentacao
def open_doc():
    url = "https://github.com/anapyx/list-project.git"
    webbrowser.open(url)

# botões da tela um e associados as funcoes
app.button_ls = cttk.CTkButton(app, width=350, height=80, text="Lista Sequencial", font=defaultfont, command=open_ls)
app.button_ls.grid(row=3, column=0, padx=(20,0), pady=20)

app.button_lse = cttk.CTkButton(app, width=350, height=80, text="Lista Simplesmente\nEncadeada", font=defaultfont, command=open_lse)
app.button_lse.grid(row=3, column=1, padx=(20,0), pady=20)

app.button_lde = cttk.CTkButton(app, width=350, height=80, text="Lista Duplamente\nEncadeada", font=defaultfont, command=open_lde)
app.button_lde.grid(row=3, column=2, padx=20, pady=20)

app.button_doc = cttk.CTkButton(app, width=350, height=60, text="Documentação", font=defaultfont, command=open_doc)
app.button_doc.grid(row=4, column=2, padx=20, pady=20)

# Creating label do Titulo
label = cttk.CTkLabel(master= app, text='Estrutura de Dados\nAplicações de Listas', text_color='white')
label.configure(width=app.winfo_screenwidth(), height=app.winfo_screenheight()/3, font=customFont, pady=10, padx=20, corner_radius=15)
label.grid(row=0, rowspan=1, column=0, columnspan=3, padx=20, pady=20)
label.configure(fg_color='#142c59')


# Criando da selecao de tela 1
sublabel = cttk.CTkLabel(app.selectionframe, text="Selecione o tipo de lista:", text_color='white')
sublabel.configure(font=defaultfont)
sublabel.grid(row=0, column=0, padx=20, pady=(20,20))

# creditos
app.credits_label = cttk.CTkLabel(app.mainframe, text="Grupo: Ana Paula Cabral    \nBárbara Cavalcante \nFelipe Lima             \nJoão Pedro             ", 
                                       font=cttk.CTkFont(size=15, weight="bold"),
                                       anchor="w")

app.credits_label.grid(row=0, column=0, padx=20, pady=(20, 10))

app.mainloop()
