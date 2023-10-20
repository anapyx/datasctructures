# -*- coding: utf-8 -*-

import customtkinter as cttk
import subprocess
import os
import webbrowser

script_directory = os.path.dirname(os.path.abspath(__file__))

app = cttk.CTk() 
app.geometry("1366x750")

app.title("Estruturas de Dados")

# criando frames
app.mainframe = cttk.CTkFrame(app, width=140, height=100, corner_radius=0)
app.mainframe.grid(row=5, column=0, columnspan=3, sticky="nsew")
#app.mainframe.grid_rowconfigure(4, weight=1)

app.selectionframe = cttk.CTkFrame(app, width=140, height=40, corner_radius=0)
app.selectionframe.grid(row=2, column=0, columnspan=3, sticky="nsew")
#app.selectionframe.grid_rowconfigure(4, weight=1)


app.grid_columnconfigure((0, 1, 2, 3), weight=1)
app.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

# fontes do app
defaultfont = cttk.CTkFont(size=20, weight='bold')
mainfont =cttk.CTkFont(family='Helvetica', size=70, weight='bold')
customFont = cttk.CTkFont(size=42, weight='bold')

# função para abrir ARQUIVO lista sequencial
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

#_____________________________________________________________________________
# função para abrir pilhas pl
def open_pl():
    app.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(current_directory)
    tela3_path = os.path.join(parent_directory,'linkedlists', 'tela3.py')

    subprocess.call(["python", tela3_path, 'Pilha'])

# função para abrir fila fl
def open_fl():
    app.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(current_directory)
    tela3_path = os.path.join(parent_directory,'linkedlists', 'tela3.py')

    subprocess.call(["python", tela3_path, 'Fila'])

# função para abrir arvores binarias de pesquisa
def open_abp():
    app.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(current_directory)
    tela3_path = os.path.join(parent_directory,'linkedlists', 'tela3.py')

    subprocess.call(["python", tela3_path, 'Arvores Binárias de Pesquisa'])


# funcao para abrir documentacao
def open_doc():
    url = "https://github.com/anapyx/list-project.git"
    webbrowser.open(url)

# botões da tela principal associados as funcoes
app.button_ls = cttk.CTkButton(app, width=350, height=80, text="Lista Sequencial", text_color='#fffdfa', font=defaultfont, command=open_ls)
app.button_ls.grid(row=3, column=0, padx=(20,0), pady=20)

app.button_lse = cttk.CTkButton(app, width=350, height=80, text="Lista Simplesmente\nEncadeada", text_color='#fffdfa', font=defaultfont, command=open_lse)
app.button_lse.grid(row=3, column=1, padx=(20,0), pady=20)

app.button_lde = cttk.CTkButton(app, width=350, height=80, text="Lista Duplamente\nEncadeada", text_color='#fffdfa', font=defaultfont, command=open_lde)
app.button_lde.grid(row=3, column=2, padx=20, pady=20)


app.button_pl = cttk.CTkButton(app, width=350, height=80, text="Pilha", text_color='#fffdfa', font=defaultfont, command=open_pl)
app.button_pl.grid(row=4, column=0, padx=(20,0), pady=(0,20))

app.button_fl = cttk.CTkButton(app, width=350, height=80, text="Fila", text_color='#fffdfa', font=defaultfont, command=open_fl)
app.button_fl.grid(row=4, column=1, padx=(20,0), pady=(0,20))

app.button_abp = cttk.CTkButton(app, width=350, height=80, text="Árvore Binária de Pesquisa", text_color='#fffdfa', font=defaultfont, command=open_abp)
app.button_abp.grid(row=4, column=2, padx=20, pady=(0,20))


app.button_doc = cttk.CTkButton(app, fg_color='#142c59', width=350, height=40, text="Documentação",font=cttk.CTkFont(size=16, weight="bold"), command=open_doc)
app.button_doc.grid(row=5, column=2, padx=20, pady=20)

# Creating label do Titulo
label = cttk.CTkLabel(master= app, text='ESTRUTURAS DE DADOS')
label.configure(width=app.winfo_screenwidth(), height=app.winfo_screenheight()/8, font=mainfont, pady=10, padx=20, corner_radius=15)
label.grid(row=0, rowspan=1, column=0, columnspan=3, padx=20, pady=20)
label.configure(fg_color='#142c59')


# Criando da selecao de tela 1
sublabel = cttk.CTkLabel(app.selectionframe, text="Selecione a estrutura de dados:")
sublabel.configure(font=cttk.CTkFont(size=20, weight='bold'))
sublabel.grid(row=0, column=0, padx=20, pady=(25,20))

# creditos
app.credits_label = cttk.CTkLabel(app.mainframe, text="Equipe: Ana Paula Cabral\n                  Bárbara Cavalcante\n    Felipe Lima\n   João Pedro", 
                                       font=cttk.CTkFont(size=16, weight="normal"),
                                       anchor="w")

app.credits_label.grid(row=0, column=0, padx=20, pady=(20, 10))

#app.state('zoomed')
app.mainloop()
