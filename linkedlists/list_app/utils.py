import customtkinter

def open_input_dialog():
    dialog = customtkinter.CTkInputDialog(text="Digite o valor do número a ser inserido: ", title="Adicionar")
    print("Valor:", dialog.get_input())
