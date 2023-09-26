# -*- coding: utf-8 -*-

import customtkinter as cttk
import subprocess
import os
import webbrowser

script_directory = os.path.dirname(os.path.abspath(__file__))

app = cttk.CTk() 
app.geometry("1100x780")

app.title("Projeto 1 - Estrutura de dados")

# criando frames
app.frame1 = cttk.CTkFrame(app, width=140, height=140, corner_radius=0)
app.frame1.grid(row=4, column=0, columnspan=3, sticky="nsew")
#app.frame1.grid_rowconfigure(4, weight=1)

app.frame2 = cttk.CTkFrame(app, width=140, height=140, corner_radius=0)
app.frame2.grid(row=2, column=0, columnspan=3, sticky="nsew")
#app.frame2.grid_rowconfigure(4, weight=1)


app.grid_columnconfigure((0, 1, 2, 3), weight=1)
app.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

# default font
defaultfont = cttk.CTkFont(size=20, weight='bold')

# custom font
customFont = cttk.CTkFont(size=42, weight='bold')

# função para abrir lista sequencial
def open_ls():
    app.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(current_directory)
    tela2_path = os.path.join(parent_directory,'linkedlists', 'tela2.py')

    print(tela2_path)
    subprocess.call(["python", tela2_path, 'Lista Sequencial'])

# função para abrir lse
def open_lse():
    app.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(current_directory)
    tela2_path = os.path.join(parent_directory,'linkedlists', 'tela2.py')

    print(tela2_path)
    subprocess.call(["python", tela2_path, 'Lista Simplesmente Encadeada'])

# função para abrir lde
def open_lde():
    app.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(current_directory)
    tela2_path = os.path.join(parent_directory,'linkedlists', 'tela2.py')

    print(tela2_path)
    subprocess.call(["python", tela2_path, 'Lista Duplamente Encadeada'])

#def open_ls():
#    app.destroy()
#    subprocess.call(['python','list-project/linkedlists/tela2.py', 'Lista Sequencial'])
#
#def open_lse():
#    app.destroy()
#    subprocess.run(['python', 'list-project/linkedlists/tela2.py', 'Lista Simplesmente Encadeada'])
#
#def open_lde():
#    app.destroy()
#    subprocess.run(['python', 'list-project/linkedlists/tela2.py', 'Lista Duplamente Encadeada'])

# funcao para abrir documentacao
def open_doc():
    url = "https://github.com/anapyx/list-project.git"
    webbrowser.open(url)


# botões da tela um e associados as funcoes
app.button_1 = cttk.CTkButton(app, width=350, height=80, text="Lista Sequencial", font=defaultfont, command=open_ls)
app.button_1.grid(row=3, column=0, padx=(20,0), pady=20)

app.button_2 = cttk.CTkButton(app, width=350, height=80, text="Lista Simplesmente\nEncadeada", font=defaultfont, command=open_lse)
app.button_2.grid(row=3, column=1, padx=(20,0), pady=20)

app.button_3 = cttk.CTkButton(app, width=350, height=80, text="Lista Duplamente\nEncadeada", font=defaultfont, command=open_lde)
app.button_3.grid(row=3, column=2, padx=20, pady=20)

app.button_5 = cttk.CTkButton(app, width=350, height=60, text="Documentação", font=defaultfont, command=open_doc)
app.button_5.grid(row=4, column=2, padx=20, pady=20)

# Creating label do Titulo
label = cttk.CTkLabel(master= app, text='Estrutura de Dados\nAplicações de Listas', text_color='white')
label.configure(width=app.winfo_screenwidth(), height=app.winfo_screenheight()/3, font=customFont, pady=10, padx=20, corner_radius=15)
label.grid(row=0, rowspan=1, column=0, columnspan=3, padx=20, pady=20)
label.configure(fg_color='#142c59')
#label.place(relx=0.5, rely=0.25, anchor='center')

# Criando da selecao de tela 1
sublabel = cttk.CTkLabel(app.frame2, text="Selecione o tipo de lista:", text_color='white')
sublabel.configure(font=defaultfont)
sublabel.grid(row=0, column=0, padx=20, pady=(20,20))

# creditos
app.logo_label = cttk.CTkLabel(app.frame1, text="Grupo: Ana Paula     \nBárbara Cavalcante \nFelipe Lima             \nJoão Pedro             ", 
                                       font=cttk.CTkFont(size=15, weight="bold"),
                                       anchor="w")

app.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

app.mainloop()
