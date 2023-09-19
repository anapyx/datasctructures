import customtkinter

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("1100x780")

app.title("Projeto 1 - Estrutura de dados")

#criando frames
app.frame1 = customtkinter.CTkFrame(app, width=140, height=140, corner_radius=0)
app.frame1.grid(row=4, column=0, columnspan=3, sticky="nsew")
#app.frame1.grid_rowconfigure(4, weight=1)

app.frame2 = customtkinter.CTkFrame(app, width=140, height=140, corner_radius=0)
app.frame2.grid(row=2, column=0, columnspan=3, sticky="nsew")
#app.frame2.grid_rowconfigure(4, weight=1)


app.grid_columnconfigure((0, 1, 2, 3), weight=1)
app.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)


#default font
defaultfont = customtkinter.CTkFont(size=20, weight='bold')

#custom font
customFont = customtkinter.CTkFont(size=42, weight='bold')


#criando botões
app.button_1 = customtkinter.CTkButton(app, width=350, height=80, text="Lista Simples", font=defaultfont)
app.button_1.grid(row=3, column=0, padx=(20,0), pady=20)

app.button_2 = customtkinter.CTkButton(app, width=350, height=80, text="Lista Simplesmente\nEncadeada", font=defaultfont)
app.button_2.grid(row=3, column=1, padx=(20,0), pady=20)

app.button_3 = customtkinter.CTkButton(app, width=350, height=80, text="Lista Duplamente\nEncadeada", font=defaultfont)
app.button_3.grid(row=3, column=2, padx=20, pady=20)

app.button_5 = customtkinter.CTkButton(app, width=350, height=60, text="Documentação", font=defaultfont)
app.button_5.grid(row=4, column=2, padx=20, pady=20)


#Creating label prototype
label = customtkinter.CTkLabel(master= app, text='Estrutura de Dados\nAplicações de Listas', text_color='white')
label.configure(width=app.winfo_screenwidth(), height=app.winfo_screenheight()/3, font=customFont, pady=10, padx=20, corner_radius=15)
label.grid(row=0, rowspan=1, column=0, columnspan=3, padx=20, pady=20)
label.configure(fg_color='#142c59')
#label.place(relx=0.5, rely=0.25, anchor='center')

#criando label 2
sublabel = customtkinter.CTkLabel(app.frame2, text="Selecione o tipo de lista:", text_color='white')
sublabel.configure(font=defaultfont)
sublabel.grid(row=0, column=0, padx=20, pady=(20,20))

#nomes
app.logo_label = customtkinter.CTkLabel(app.frame1, text="Grupo: Ana Paula     \nBárbara Cavalcante \nFelipe Lima             \nJoão Pedro             ", 
                                       font=customtkinter.CTkFont(size=15, weight="bold"),
                                       anchor="w")

app.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

app.mainloop()
