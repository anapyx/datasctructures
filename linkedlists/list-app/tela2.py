import customtkinter
import tkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("1100x780")

#___________________________
#variaveis que vem de fora
list_type = "Lista Duplamente Encadeada"
#___________________________


def button_function():
    print("button pressed")

app.title("Projeto 1 - Estrutura de dados")

#default font
defaultfont = customtkinter.CTkFont(size=15, weight='bold')
defaultfont2 = customtkinter.CTkFont(size=25, weight='bold')

#custom font
customFont = customtkinter.CTkFont(size=42, weight='bold')

app.grid_columnconfigure((1, 2, 3, 4, 5), weight=1)
app.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)


#criando frames
app.frame1 = customtkinter.CTkFrame(app, corner_radius=10)
app.frame1.grid(row=1, rowspan=4, column=0, padx=20, sticky="nsew")
app.frame1.grid_columnconfigure(1,weight=0)
app.frame1.grid_rowconfigure(7, weight=1)

app.frame2 = customtkinter.CTkFrame(app, width=140, height=140, corner_radius=10)
app.frame2.grid(row=1, rowspan=4, column=1, columnspan=4, padx=(0,20), sticky="nsew")
#app.frame1.grid_rowconfigure(4, weight=1)


##criando botões
app.button_1 = customtkinter.CTkButton(app.frame1, width=200, height=50, text="Elemento 1", font=defaultfont)
app.button_1.grid(row=0, column=0, padx=20, pady=(40,20))

app.button_2 = customtkinter.CTkButton(app.frame1, width=200, height=50, text="ADD", font=defaultfont)
app.button_2.grid(row=1, column=0, padx=20, pady=20)

app.button_3 = customtkinter.CTkButton(app.frame1, width=200, height=50, text="Remove", font=defaultfont)
app.button_3.grid(row=2, column=0, padx=20, pady=20)

app.button_4 = customtkinter.CTkButton(app.frame1, width=200, height=50, text="Procura\nElemento", font=defaultfont)
app.button_4.grid(row=3, column=0, padx=20, pady=20)

app.button_5 = customtkinter.CTkButton(app.frame1, width=200, height=50, text="Procura\nPosição", font=defaultfont)
app.button_5.grid(row=4, column=0, padx=20, pady=20)

app.button_5 = customtkinter.CTkButton(app.frame1, width=150, height=30, text="Gerar", font=defaultfont)
app.button_5.grid(row=7, column=0, padx=20, pady=20)


#Creating label prototype
label = customtkinter.CTkLabel(master= app, text=list_type, text_color='white')
label.configure(width=app.winfo_screenwidth(), height=100, font=customFont, pady=10, padx=20, corner_radius=10)
label.grid(row=0, column=0, columnspan=5, padx=20, pady=20)
label.configure(fg_color='#142c59')
#label.place(relx=0.5, rely=0.25, anchor='center')


app.mainloop()
