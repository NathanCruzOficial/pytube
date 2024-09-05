from tkinter import PhotoImage
from turtle import down
import customtkinter as ctk
from img.ico import icon_base64 # Sua string base64 aqui
import base64
import decodificardor_base64 as dcd



#Cores
color_red = "#FF3232"
color_gray = "#3F3F3F"

#Valores
margem = 450
defalt_download_archive = str(r'C:\Users\user\Downloads')

root = ctk.CTk()
#Decodificador Base64
icon = PhotoImage(data=base64.b64decode(icon_base64))

download_icon = ctk.CTkImage(dcd.decoded_img['download'], size=(32, 32))  # Defina o tamanho que deseja
folder_icon = ctk.CTkImage(dcd.decoded_img['folder'], size=(32, 32))
ico_icon = ctk.CTkImage(dcd.decoded_img['ico'], size=(32, 32))

#Configurações da Janela principal
root._set_appearance_mode("dark")
root.iconbitmap(None)
root.iconphoto(False, icon)
root.geometry("800x500")
root.resizable(width=False, height=False)
mainframe = ctk.CTkFrame(root,400,500,fg_color=color_gray,corner_radius=0).place(x=400)

#Elementos
ctk.CTkLabel(mainframe,text="Video URL",fg_color=color_gray).place(x=margem,y=50)
url = ctk.CTkEntry(mainframe,placeholder_text="https://www.youtube.com/",width=300,height=35,corner_radius=0).place(x=margem,y=75)

ctk.CTkLabel(mainframe,text="Local",fg_color=color_gray).place(x=margem,y=125)
url = ctk.CTkEntry(mainframe,placeholder_text=defalt_download_archive,width=300,height=35,corner_radius=0).place(x=margem,y=150)

ctk.CTkButton(mainframe,image= download_icon,width=10,height=10).place(x=margem, y=450)

root.mainloop()