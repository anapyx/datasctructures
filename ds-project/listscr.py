# -*- coding: utf-8 -*-
from No import No
from LDE import LDE
from LSE import LSE
from LS import LS
import customtkinter as cttk
import subprocess
import os
import sys

cttk.set_default_color_theme("blue")

app = cttk.CTk()
app.geometry("1366x710")

if len(sys.argv) > 1:
    list_type = sys.argv[1]
else:
    list_type = "Listas"

app.title("Estruturas de Dados")

# Tela para aplicação das Listas

sys.path.insert(0, "..")

# fontes utilizadas
defaultfont = cttk.CTkFont(size=15, weight='bold')
defaultfont2 = cttk.CTkFont(size=25, weight='bold')
titulos = cttk.CTkFont(family='Helvetica', size=42, weight='bold')

# criação de frames e canvas
app.grid_columnconfigure((1, 2, 3, 4, 5), weight=1)
app.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

app.frameMenu = cttk.CTkFrame(app, corner_radius=10)
app.frameMenu.grid(row=1, rowspan=4, column=0, padx=20, sticky="nsew")
app.frameMenu.grid_columnconfigure(1, weight=0)
app.frameMenu.grid_rowconfigure(7, weight=1)

app.frameBlank = cttk.CTkFrame(app, width=140, height=140, corner_radius=10)
app.frameBlank.grid(row=1, rowspan=4, column=1,
                    columnspan=4, padx=(0, 20), sticky="nsew")

app.canvas_in_frame = cttk.CTkCanvas(app.frameBlank, width=1000, height=800)
app.canvas_in_frame.pack()
app.canvas_in_frame.configure(bg='#2b2b2b', highlightbackground='#2b2b2b')

# Funcao de percorrer entre telas
def open_AppScreen():
    app.destroy()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(current_directory)
    AppScreen_path = os.path.join(
        parent_directory, 'ds-project', 'AppScreen.py')
    subprocess.call(["python", AppScreen_path])

# Funcoes do canvas para listas

def define_size(canvas):
    global myList
    global size
    dialog = cttk.CTkInputDialog(
        text="Digite o valor do tamanho da lista: ", title="Criar")
    size = int(dialog.get_input())
    myList = LS(size)

    if size > 0 and size < 11:
        myList.draw_sequential_list(app.canvas_in_frame, size)
    elif size < 1:
        canvas.create_text(400, 50, text="Digite um valor válido.", font=(
            "Arial", 22), tags="result_text", fill="white")
    else:
        canvas.create_text(400, 50, text="A lista não pode ter mais de 10 elementos.", font=(
            "Arial", 22), tags="result_text", fill="white")
        return


def create_head(canvas):
    canvas.delete("result_text")
    global myList
    if list_type == 'Lista Simplesmente Encadeada':
        myList = LSE()
    elif list_type == 'Lista Duplamente Encadeada':
        myList = LDE()
    else:
        return

    dialog = cttk.CTkInputDialog(
        text="Digite o valor do número a ser inserido: ", title="Adicionar")
    elem = dialog.get_input()
    pos = 1
    #elem = int(elem)
    result = myList.appendList(elem, pos)

    if result is True:
        if list_type == 'Lista Simplesmente Encadeada':
            myList.draw_singly_linked_list(app.canvas_in_frame)
        elif list_type == 'Lista Duplamente Encadeada':
            myList.draw_doubly_linked_list(app.canvas_in_frame)
    else:
        canvas.create_text(400, 50, text="Operação Inválida.", font=(
            "Arial", 22), tags="result_text", fill="white")


def add_element(canvas):
    global myList
    canvas.delete("result_text")

    if list_type == 'Lista Sequencial':
        limit_size = 10
    else:
        limit_size = 6

    if myList.size() > limit_size:
        canvas.create_text(400, 50, text="A lista já está no tamanho máximo.", font=(
            "Arial", 22), tags="result_text", fill="white")
        return

    if myList is None:
        canvas.create_text(400, 50, text="Cabeça da lista não foi criada.", font=(
            "Arial", 22), tags="result_text", fill="white")
        return

    dialog = cttk.CTkInputDialog(
        text="Digite o valor do número a ser inserido: ", title="Adicionar")
    elem = dialog.get_input()
    dialog.destroy()
    dialog2 = cttk.CTkInputDialog(
        text="Digite a posição que o número deve ser inserido: ", title="Adicionar")
    pos = dialog2.get_input()

    try:
        pos = int(pos)
        elem = int(elem)

        result = myList.appendList(elem, pos)

        if result is True:
            if list_type == 'Lista Sequencial':
                myList.draw_sequential_list(app.canvas_in_frame, size)
            elif list_type == 'Lista Simplesmente Encadeada':
                myList.draw_singly_linked_list(app.canvas_in_frame)
            elif list_type == 'Lista Duplamente Encadeada':
                myList.draw_doubly_linked_list(app.canvas_in_frame)
        else:
            canvas.create_text(400, 50, text="Operação Inválida.", font=(
                "Arial", 22), tags="result_text", fill="white")
    except ValueError:
        canvas.create_text(400, 50, text="A posição e/ou o elemento deve ser um número inteiro válido.",
                           font=("Arial", 22), tags="result_text", fill="white")


def remove_element(canvas):
    global myList
    canvas.delete("result_text")

    if myList is None:
        canvas.create_text(400, 50, text="Cabeça da lista não foi criada.", font=(
            "Arial", 22), tags="result_text", fill="white")
        return

    if list_type == 'Lista Sequencial' and size < 1:
        canvas.create_text(400, 50, text="A lista não foi criada.", font=(
            "Arial", 22), tags="result_text", fill="white")
        return

    dialog = cttk.CTkInputDialog(
        text="Digite a posição do número a ser removido: ", title="Remover")
    pos = dialog.get_input()

    try:
        pos = int(pos)

        result = myList.removeList(pos)

        if result is True:
            if list_type == 'Lista Sequencial':
                myList.draw_sequential_list(app.canvas_in_frame, size)
            elif list_type == 'Lista Simplesmente Encadeada':
                myList.draw_singly_linked_list(app.canvas_in_frame)
            elif list_type == 'Lista Duplamente Encadeada':
                myList.draw_doubly_linked_list(app.canvas_in_frame)
        else:
            canvas.create_text(400, 50, text="Operação Inválida.", font=(
                "Arial", 22), tags="result_text", fill="white")
    except ValueError:
        canvas.create_text(400, 50, text="A posição deve ser um número inteiro válido.", font=(
            "Arial", 22), tags="result_text", fill="white")


def search_element(canvas):
    canvas.delete("result_text")

    if myList is None:
        canvas.create_text(400, 50, text="Cabeça da lista não foi criada.", font=(
            "Arial", 22), tags="result_text", fill="white")
        return

    dialog = cttk.CTkInputDialog(
        text="Digite o valor do número a ser buscado: ", title="Buscar")
    elem = dialog.get_input()

    try:
        positions = myList.position(elem)
        positions_str = ", ".join(map(str, positions))
        canvas.create_text(400, 50, text=f"O elemento {elem} foi encontrado nas posições: {positions_str}", font=(
            "Arial", 22), tags="result_text", fill="white")
    except ValueError as e:
        canvas.create_text(400, 50, text=str(e), font=(
            "Arial", 22), tags="result_text", fill="white")


def search_position(canvas):
    canvas.delete("result_text")

    if myList is None:
        canvas.create_text(400, 30, text="Cabeça da lista não foi criada.", font=(
            "Arial", 16), tags="result_text", fill="white")
        return

    dialog = cttk.CTkInputDialog(
        text="Digite a posição a ser buscada: ", title="Buscar")
    pos = int(dialog.get_input())

    try:
        element = myList.element(pos)
        canvas.create_text(400, 50, text=f"O elemento na posição {pos} é: {element}", font=(
            "Arial", 22), tags="result_text", fill="white")
    except ValueError as e:
        canvas.create_text(400, 50, text=str(e), font=(
            "Arial", 22), tags="result_text", fill="white")

# ---------------- TELA DE LISTAS --------------
# Botoes do menu da tela de listas

# testando tipos sem abrir a tela principal
# list_type = 'Lista Sequencial'

# Inicializa tipo de Lista
if list_type == 'Lista Sequencial':
    app.buttonSize = cttk.CTkButton(app.frameMenu, width=200, height=50, text="Definir Tamanho",
                                    font=defaultfont, command=lambda: define_size((app.canvas_in_frame)))
    app.buttonSize.grid(row=0, column=0, padx=20, pady=(40, 20))
else:
    app.buttonHead = cttk.CTkButton(app.frameMenu, width=200, height=50, text="Criar Cabeça",
                                    font=defaultfont, command=lambda: create_head((app.canvas_in_frame)))
    app.buttonHead.grid(row=0, column=0, padx=20, pady=(40, 20))

# Botões do frame
app.buttonAdd = cttk.CTkButton(app.frameMenu, width=200, height=50, text="Adicionar\nElemento",
                               font=defaultfont, command=lambda: add_element(app.canvas_in_frame))
app.buttonAdd.grid(row=1, column=0, padx=20, pady=20)

app.buttonRem = cttk.CTkButton(app.frameMenu, width=200, height=50, text="Remove",
                               font=defaultfont, command=lambda: remove_element(app.canvas_in_frame))
app.buttonRem.grid(row=2, column=0, padx=20, pady=20)

app.buttonElem = cttk.CTkButton(app.frameMenu, width=200, height=50, text="Busca pelo\nElemento",
                                font=defaultfont, command=lambda: search_element(app.canvas_in_frame))
app.buttonElem.grid(row=3, column=0, padx=20, pady=20)

app.buttonPos = cttk.CTkButton(app.frameMenu, width=200, height=50, text="Busca na\nPosição",
                               font=defaultfont, command=lambda: search_position((app.canvas_in_frame)))
app.buttonPos.grid(row=4, column=0, padx=20, pady=20)

app.buttonGoBack = cttk.CTkButton(
    app.frameMenu, width=200, height=50, text="Retornar", font=defaultfont, command=open_AppScreen)
app.buttonGoBack.grid(row=5, column=0, padx=20, pady=20)

# Titulo da tela
label = cttk.CTkLabel(master=app, text=list_type, text_color='white')
label.configure(width=app.winfo_screenwidth(), height=100,
                font=titulos, pady=10, padx=20, corner_radius=10)
label.grid(row=0, column=0, columnspan=5, padx=20, pady=20)
label.configure(fg_color='#142c59')

app.mainloop()
