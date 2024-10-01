from tkinter import PhotoImage, dialog, filedialog, StringVar
import customtkinter as ctk
from img.ico import icon_base64 # Sua string base64 aqui
import base64
import decodificardor_base64 as dcd
import core
import color

#---------VARIÁVEIS-------------------------------------------------------------------------------------------------------------------------------------
root = ctk.CTk()

#Valores
margem = 450
defalt_download_folder = str(r'C:\Users\user\Downloads')

#---------FUNÇÕES-------------------------------------------------------------------------------------------------------------------------------------

def get_local():
    file = filedialog.askdirectory()
    local_folder.delete(0, "end")
    local_folder.insert(0, file)
    pass

def star_download(url,mode):
    download_button.configure(state="disable",fg_color=color.gray_light)
    core.start_download(url,aviso,mode)
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
mainframe = ctk.CTkFrame(root,400,500,fg_color=color.gray,corner_radius=0).place(x=400)

#Elementos
ctk.CTkLabel(root,text="© 2024 - Desenvolvido por Nathan Cruz",text_color="#4E4E4E",font=("Arial Black", 8)).place(x=5,y=475)
ctk.CTkLabel(root, image=image_bg,text="").place(x=20,y=85)

aviso = ctk.CTkLabel(mainframe,text="Url Inválido",fg_color=color.gray,bg_color=color.gray,text_color=color.red,height=10)
ctk.CTkLabel(mainframe,text="Video URL",fg_color=color.gray,bg_color=color.gray).place(x=margem,y=50)
url = ctk.CTkEntry(mainframe,placeholder_text="https://www.youtube.com/",width=300,height=35,corner_radius=5,bg_color=color.gray)
url.place(x=margem,y=75)

tumbnailframe = ctk.CTkFrame(mainframe,300,125,corner_radius=0)
tumbnailframe.place(x=margem,y=275)

# image_path = r"img\ico.ico"
# image_pil = Image.open(image_path)
# tumbnailimgfile = ctk.CTkImage(light_image=image_pil,dark_image=image_pil,size=(110, 110))
# tumbnailimg = label_img = ctk.CTkLabel(tumbnailframe, image=tumbnailimgfile, text="")
# tumbnailimg.place(x=10, y=10)
# tumbnailtitle = label_img = ctk.CTkLabel(tumbnailframe, text="downlaod")

ctk.CTkLabel(mainframe,text="Local",fg_color=color.gray,bg_color=color.gray).place(x=margem,y=125)
local_folder = ctk.CTkEntry(mainframe,placeholder_text=defalt_download_folder,width=300-35,height=35,corner_radius=5,bg_color=color.gray)
local_folder.place(x=margem, y=150)

ctk.CTkLabel(mainframe,text="Modo",fg_color=color.gray).place(x=margem,y=200)
mode = ctk.CTkOptionMenu(mainframe,
                         values=["mp3","mp4","mov"],
                         width=145,
                         height=30,
                         dropdown_font=("Arial Black", 13),
                         fg_color=color.red,
                         bg_color=color.gray,
                         button_color=color.red,
                         font=("Arial Black", 16),
                         button_hover_color=color.red_select
                         )
mode.place(x=margem,y=225)

feedback = ctk.CTkLabel(mainframe,text="",fg_color=color.gray,bg_color=color.gray)

download_button = ctk.CTkButton(mainframe, #Donload Button
              image= download_icon,
              text="Download",
              width=300,
              height=50,
              fg_color=color.red,
              bg_color=color.gray,
              
              hover_color=color.red_select,
              command=lambda:star_download(url,mode),
              font=("Arial Black", 20)
)
download_button.place(x=margem, y=425)

ctk.CTkButton(mainframe, #Archive Button
              image= folder_icon,
              text="",
              width=30,
              height=35,
              fg_color=color.red,
              bg_color=color.gray,
              hover_color=color.red_select,
              command=get_local,
).place(x=margem+270, y=150)

loadbar = ctk.CTkProgressBar(mainframe,
                             corner_radius=0,
                             progress_color=color.red,
                             width=400)
loadbar.place(x=400,y=495)

root.mainloop()