import tkinter as tk
import customtkinter as cttk
from appfunctions import appfunctions

# TESTE SE DA PRA FAZER APENAS UMA JANELA QUE TRANSITA ENTRE TELAS
# EVITA O ERRO DE NO MODULE FOUND E ORGANIZA AS TELAS EM CLASSES

# Criando a janela com cttk
app = cttk.CTk() 
app.geometry("1100x780")
app.title("Estrutura de dados - Projeto de Listas")
defaultfont = cttk.CTkFont(size=20, weight='bold')
customFont = cttk.CTkFont(size=42, weight='bold')

# ?
app.grid_columnconfigure((0, 1, 2, 3), weight=1)
app.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

# -----colocar essas funcoes em appfunctions depois
def returnMainScreen():
    return
    # ativar a mudança de tela na mesma janela por tkraise() ou função similar


def changetoLS():
    return
    # mudança de tela na mesma janela para frames da LS, frame.destroy()


def changetoLSE():
    return
    # mudança de tela na mesma janela para frames da LSE, destroi main window


def changetoLDE():
    return
    # mudança de tela na mesma janela para frames da LDE, destroi main window

# funcao para abrir documentacao
def openDoc():
    url = "https://github.com/anapyx/list-project.git"
    webbrowser.open(url)


# ---------- TELAS DO APP -----------
# Colocar todos os itens da tela principal (tela1) e botoes chamando as funcoes acima
class MainScreen():
    def __init__(self,master):
        # frame de titulo
        app.mainframe = cttk.CTkFrame(app, width=140, height=140, corner_radius=0)
        app.mainframe.grid(row=4, column=0, columnspan=3, sticky="nsew")
        # frame de selecao de listas
        app.selectionframe = cttk.CTkFrame(app, width=140, height=140, corner_radius=0)
        app.selectionframe.grid(row=2, column=0, columnspan=3, sticky="nsew")

    # Creating label do Titulo
    title = cttk.CTkLabel(master= app, text='Estrutura de Dados\nAplicações de Listas', text_color='white')
    title.configure(width=app.winfo_screenwidth(), height=app.winfo_screenheight()/3, font=customFont, pady=10, padx=20, corner_radius=15)
    title.grid(row=0, rowspan=1, column=0, columnspan=3, padx=20, pady=20)
    title.configure(fg_color='#142c59')
    #title.place(relx=0.5, rely=0.25, anchor='center')

    # Criando da selecao de tela 1
    selection = cttk.CTkLabel(app.frame2, text="Selecione o tipo de lista:", text_color='white')
    selection.configure(font=defaultfont)
    selection.grid(row=0, column=0, padx=20, pady=(20,20))

        # creditos
    app.credits = cttk.CTkLabel(app.frame1, text="Grupo: Ana Paula     \nBárbara Cavalcante \nFelipe Lima             \nJoão Pedro             ", 
                                        font=cttk.CTkFont(size=15, weight="bold"),
                                        anchor="w")

    app.credits.grid(row=0, column=0, padx=20, pady=(20, 10))

    # botões da tela um e associados as funcoes
    app.buttonLS = cttk.CTkButton(app, width=350, height=80, text="Lista Sequencial", font=defaultfont, command=changetoLS)
    app.buttonLS.grid(row=3, column=0, padx=(20,0), pady=20)

    app.buttonLSE = cttk.CTkButton(app, width=350, height=80, text="Lista Simplesmente\nEncadeada", font=defaultfont, command=changetoLSE)
    app.buttonLSE.grid(row=3, column=1, padx=(20,0), pady=20)

    app.buttonLDE = cttk.CTkButton(app, width=350, height=80, text="Lista Duplamente\nEncadeada", font=defaultfont, command=changetoLDE)
    app.buttonLDE.grid(row=3, column=2, padx=20, pady=20)

    app.buttonDoc = cttk.CTkButton(app, width=350, height=60, text="Documentação",   font=defaultfont, command=openDoc)
    app.buttonDoc.grid(row=4, column=2, padx=20, pady=20)
    

class lsWindow():
    def __init__(self):
        app.frame1 = cttk.CTkFrame(app, corner_radius=10)
        app.frame1.grid(row=1, rowspan=4, column=0, padx=20, sticky="nsew")
        app.frame1.grid_columnconfigure(1, weight=0)
        app.frame1.grid_rowconfigure(7, weight=1)  

        app.frame2 = cttk.CTkFrame(app, width=140, height=140, corner_radius=10)
        app.frame2.grid(row=1, rowspan=4, column=1, columnspan=4, padx=(0, 20), sticky="nsew")

        app.grid_columnconfigure((1, 2, 3, 4, 5), weight=1)
        app.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

    defaultfont = cttk.CTkFont(size=15, weight='bold')
    defaultfont2 = cttk.CTkFont(size=25, weight='bold')

    app.sizebutton = cttk.CTkButton(app.frame1, width=200, height=50, text="Definir Tamanho", font=defaultfont, command= lambda: define_size((app.canvas_in_frame2)))
    app.sizebutton.grid(row=0, column=0, padx=20, pady=(40, 20))

    # continua...




app.mainloop()
