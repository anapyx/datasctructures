import customtkinter
import tkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("1100x780")

def button_function():
    print("button pressed")

app.title("Projeto 1 - Estrutura de dados")

#criando frames
app.frame1 = customtkinter.CTkFrame(app, width=140, height=140, corner_radius=0)
app.frame1.grid(row=4, column=0, columnspan=4, sticky="nsew")
#app.frame1.grid_rowconfigure(4, weight=1)

app.frame2 = customtkinter.CTkFrame(app, width=140, height=140, corner_radius=0)
app.frame2.grid(row=2, column=0, columnspan=4, sticky="nsew")
#app.frame2.grid_rowconfigure(4, weight=1)


app.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
app.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

#app.logo_label = customtkinter.CTkLabel(app.frame1, text="CustomTkinter", font=customtkinter.CTkFont(size=20, weight="bold"))
#app.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

#default font
defaultfont = customtkinter.CTkFont(size=15, weight='bold')
defaultfont2 = customtkinter.CTkFont(size=25, weight='bold')

#custom font
customFont = customtkinter.CTkFont(size=42, weight='bold')


#criando botões
app.button_1 = customtkinter.CTkButton(app, width=300, height=80, text="Lista Simples", font=defaultfont)
app.button_1.grid(row=3, column=0, padx=20, pady=20)

app.button_2 = customtkinter.CTkButton(app, width=300, height=80, text="Lista Simplesmente\nEncadeada", font=defaultfont)
app.button_2.grid(row=3, column=1, padx=20, pady=20)

app.button_3 = customtkinter.CTkButton(app, width=300, height=80, text="Lista Duplamente\nEncadeada", font=defaultfont)
app.button_3.grid(row=3, column=2, padx=20, pady=20)

app.button_4 = customtkinter.CTkButton(app, width=300, height=80, text="Lista Duplamente\nEncadeada Circular", font=defaultfont)
app.button_4.grid(row=3, column=3, padx=20, pady=20)

app.button_5 = customtkinter.CTkButton(app, width=300, height=60, text="Documentação", font=defaultfont)
app.button_5.grid(row=4, column=3, padx=20, pady=20)


#Creating label prototype
label = customtkinter.CTkLabel(master= app, text='Estrutura de Dados\nAplicações de Listas', text_color='white')
label.configure(width=app.winfo_screenwidth(), height=app.winfo_screenheight()/3, font=customFont, pady=10, padx=20, corner_radius=15)
label.grid(row=0, rowspan=1, column=0, columnspan=4, padx=20, pady=20)
label.configure(fg_color='#142c59')
#label.place(relx=0.5, rely=0.25, anchor='center')

#criando label 2
sublabel = customtkinter.CTkLabel(app.frame2, text="Selecione o tipo de lista:", text_color='white')
sublabel.configure(font=defaultfont2)
sublabel.grid(row=0, column=0, padx=20, pady=(20,20))

app.mainloop()
