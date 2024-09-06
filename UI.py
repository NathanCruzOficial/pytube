from threading import local
from tkinter import PhotoImage, filedialog, StringVar
import customtkinter as ctk
from img.ico import icon_base64 # Sua string base64 aqui
import base64
import decodificardor_base64 as dcd

#---------VARIÁVEIS-------------------------------------------------------------------------------------------------------------------------------------
root = ctk.CTk()

#Cores
color_red = "#FF3232"
color_red_select = "#FF6161"
color_gray = "#3F3F3F"

#Valores
margem = 450
defalt_download_folder = str(r'C:\Users\user\Downloads')

#---------FUNÇÕES-------------------------------------------------------------------------------------------------------------------------------------

def get_local():
    file = filedialog.askdirectory()
    local_folder.delete(0, "end")
    local_folder.insert(0, file)
    pass

#---------MAIN-------------------------------------------------------------------------------------------------------------------------------------


#Decodificador Base64
icon = PhotoImage(data=base64.b64decode(icon_base64))

download_icon = ctk.CTkImage(dcd.decoded_img['download'], size=(20, 20))
folder_icon = ctk.CTkImage(dcd.decoded_img['folder'], size=(20, 20))
ico_icon = ctk.CTkImage(dcd.decoded_img['ico'], size=(32, 32))
image_bg = ctk.CTkImage(dcd.decoded_img['image'], size=(360, 360))

#Configurações da Janela principal
root._set_appearance_mode("dark")
root.title("YoutubeLoad")
root.iconbitmap(None)
root.iconphoto(False, icon)
root.geometry("800x500")
root.resizable(width=False, height=False)
mainframe = ctk.CTkFrame(root,400,500,fg_color=color_gray,corner_radius=0).place(x=400)

#Elementos
ctk.CTkLabel(root,text="© 2024 - Desenvolvido por Nathan Cruz",text_color="#4E4E4E",font=("Arial Black", 8)).place(x=5,y=475)
ctk.CTkLabel(root, image=image_bg,text="").place(x=20,y=85)


ctk.CTkLabel(mainframe,text="Video URL",fg_color=color_gray).place(x=margem,y=50)
url = ctk.CTkEntry(mainframe,placeholder_text="https://www.youtube.com/",width=300,height=35,corner_radius=5,bg_color=color_gray).place(x=margem,y=75)

ctk.CTkLabel(mainframe,text="Local",fg_color=color_gray).place(x=margem,y=125)
local_folder = ctk.CTkEntry(mainframe,placeholder_text=defalt_download_folder,width=300-35,height=35,corner_radius=5,bg_color=color_gray)
local_folder.place(x=margem, y=150)


ctk.CTkButton(mainframe, #Donload Button
              image= download_icon,
              text="Download",
              width=300,
              height=25,
              fg_color=color_red,
              bg_color=color_gray,
              hover_color=color_red_select,
              command=None,
              font=("Arial Black", 20)
).place(x=margem, y=450)

ctk.CTkButton(mainframe, #Archive Button
              image= folder_icon,
              text="",
              width=30,
              height=35,
              fg_color=color_red,
              bg_color=color_gray,
              hover_color=color_red_select,
              command=get_local,
).place(x=margem+270, y=150)


root.mainloop()