import customtkinter as cttk
from LS import LS
from LSE import LSE
from LDE import LDE
from No import No
 
 # Funções que não envolvem mudar de arquivos

def open_input_dialog():
    dialog = cttk.CTkInputDialog(text="Digite o valor do número a ser inserido: ", title="Adicionar")
    print("Valor:", dialog.get_input())

# Funcoes do canva para listas
def define_size(canvas):
    global myList
    dialog = cttk.CTkInputDialog(text="Digite o valor do tamanho da lista: ", title="Criar")
    size = int(dialog.get_input())
    myList = LS(size)

    if size > 0:
        myList.draw_sequential_list(app.canvas_in_frame2,size)
    else:
        canvas.create_text(400, 50, text="Operação Inválida.", font=("Arial", 22), tags="result_text", fill = "white")

def create_head(canvas):
    canvas.delete("result_text")
    global myList
    if list_type == 'Lista Simplesmente Encadeada':
        myList = LSE()
    elif list_type == 'Lista Duplamente Encadeada':
        myList = LDE()
    else:
        return

    dialog = cttk.CTkInputDialog(text="Digite o valor do número a ser inserido: ", title="Adicionar")
    elem = dialog.get_input()
    pos = 1
    #elem = int(elem)
    result = myList.appendList(elem, pos)
    
    if result is True:
        if list_type == 'Lista Simplesmente Encadeada':
            myList.draw_singly_linked_list(app.canvas_in_frame2)
        elif list_type == 'Lista Duplamente Encadeada':
            myList.draw_doubly_linked_list(app.canvas_in_frame2)
    else:
        canvas.create_text(400, 50, text="Operação Inválida.", font=("Arial", 22), tags="result_text", fill = "white")

def add_element(canvas):
    global myList
    canvas.delete("result_text")

    if myList.size() == 7:
        canvas.create_text(400, 50, text="A lista não pode ter mais de 7 elementos.", font=("Arial", 22), tags="result_text", fill = "white")
        return

    if myList is None:
        canvas.create_text(400, 50, text="Cabeça da lista não foi criada.", font=("Arial", 22), tags="result_text", fill = "white")
        return

    dialog = cttk.CTkInputDialog(text="Digite o valor do número a ser inserido: ", title="Adicionar")
    elem = dialog.get_input()
    dialog.destroy()
    dialog2 = cttk.CTkInputDialog(text="Digite a posição que o número deve ser inserido: ", title="Adicionar")
    pos = dialog2.get_input()

    try:
        pos = int(pos)
        elem = int(elem)
        
        result = myList.appendList(elem, pos)

        if result is True:
            if list_type == 'Lista Sequencial':
                myList.draw_sequential_list(app.canvas_in_frame2)
            elif list_type == 'Lista Simplesmente Encadeada':
                myList.draw_singly_linked_list(app.canvas_in_frame2)
            elif list_type == 'Lista Duplamente Encadeada':
                myList.draw_doubly_linked_list(app.canvas_in_frame2)
        else:
            canvas.create_text(400, 50, text="Operação Inválida.", font=("Arial", 22), tags="result_text", fill = "white")
    except ValueError:
        canvas.create_text(400, 50, text="A posição e/ou o elemento deve ser um número inteiro válido.", font=("Arial", 22), tags="result_text", fill = "white")

def remove_element(canvas):
    global myList
    canvas.delete("result_text")

    if myList is None:
        canvas.create_text(400, 50, text="Cabeça da lista não foi criada.", font=("Arial", 22), tags="result_text", fill = "white")
        return

    dialog = cttk.CTkInputDialog(text="Digite a posição do número a ser removido: ", title="Remover")
    pos = dialog.get_input()

    try:
        pos = int(pos) 
        result = myList.removeList(pos) 

        if result is True:
            if list_type == 'Lista Sequencial':
                myList.draw_sequential_list(app.canvas_in_frame2)
            elif list_type == 'Lista Simplesmente Encadeada':
                myList.draw_singly_linked_list(app.canvas_in_frame2)
            elif list_type == 'Lista Duplamente Encadeada':
                myList.draw_doubly_linked_list(app.canvas_in_frame2)
        else:
            canvas.create_text(400, 50, text="Operação Inválida.", font=("Arial", 22), tags="result_text", fill = "white")
    except ValueError:
        canvas.create_text(400, 50, text="A posição deve ser um número inteiro válido.", font=("Arial", 22), tags="result_text", fill = "white")


def search_element(canvas):
    canvas.delete("result_text") 
    
    if myList is None:
        canvas.create_text(400, 50, text="Cabeça da lista não foi criada.", font=("Arial", 22), tags="result_text", fill = "white")
        return

    dialog = cttk.CTkInputDialog(text="Digite o valor do número a ser buscado: ", title="Buscar")
    elem = dialog.get_input()

    try:
        positions = myList.position(elem)
        positions_str = ", ".join(map(str, positions))
        canvas.create_text(400, 50, text=f"O elemento {elem} foi encontrado nas posições: {positions_str}", font=("Arial", 22), tags="result_text", fill = "white")
    except ValueError as e:
        canvas.create_text(400, 50, text=str(e), font=("Arial", 22), tags="result_text", fill = "white")

def search_position(canvas):
    canvas.delete("result_text") 
    
    if myList is None:
        canvas.create_text(400, 30, text="Cabeça da lista não foi criada.", font=("Arial", 16), tags="result_text", fill = "white")
        return

    dialog = cttk.CTkInputDialog(text="Digite a posição a ser buscada: ", title="Buscar")
    pos = int(dialog.get_input())

    try:
        element = myList.element(pos)
        canvas.create_text(400, 50, text=f"O elemento na posição {pos} é: {element}", font=("Arial", 22), tags="result_text", fill = "white")
    except ValueError as e:
        canvas.create_text(400, 50, text=str(e), font=("Arial", 22), tags="result_text", fill = "white")
