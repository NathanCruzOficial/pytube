import tkinter as tk
from tkinter import simpledialog, font, messagebox
from tkinter.filedialog import askdirectory
from pytube import YouTube
import moviepy.editor as mp
import os
import re

cor = "#e22e2e"

class CustomDialog(simpledialog.Dialog):
    def body(self, master):
        self.geometry("300x100")
        self.title("Mp3 Downloader")
        self.iconbitmap("./ico.ico")
        self.resizable(False, False)
        self.configure(bg=cor)
        tk.Label(master, text="Insira o link abaixo:", width=25, bg=cor, fg="white", font=font.Font(weight="bold")).grid(row=0, pady=0)
        self.entry = tk.Entry(master, width=40)
        self.entry.grid(row=1, column=0, pady=0)
        
         # Mensagem de direitos autorais
        tk.Label(master, text="© 2024 - Todos os direitos reservados.", bg=cor, fg="white", font=("Arial", 8)).grid(row=2, pady=5)
        return self.entry  # Definir foco inicial

    def buttonbox(self):
        box = tk.Frame(self, bg=cor)
        tk.Button(box, text="Download", width=10, command=self.download, bg="#ffffff", fg='black').pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(box, text="Cancel", width=10, command=self.cancel_dialog, bg="#ffffff", fg='black').pack(side=tk.LEFT, padx=5, pady=5)
        box.pack()

    def cancel_dialog(self):
        self.result = None
        self.destroy()

    def download(self):
        link = self.entry.get()
        if self.validate_youtube_link(link):
            self.result = link
            self.ok()
        else:
            messagebox.showerror(title="Erro!", message="Link do YouTube inválido.")

    def validate_youtube_link(self, link):
        # Regex para validar URLs do YouTube
        youtube_regex = (
            r'(https?://)?(www\.)?'r'(youtube|youtu|youtube-nocookie)\.(com|be)/'r'(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
        return re.match(youtube_regex, link)

    def apply(self):
        pass  # Não é necessário implementar este método

def show_custom_dialog():
    root = tk.Tk()
    root.withdraw()  # Ocultar a janela principal
    dialog = CustomDialog(root)
    return dialog.result

def clean_filename(filename):
    # Lista de caracteres inválidos para nomes de arquivos
    invalid_chars = r'<>:"/\|?*'

    # Substituir caracteres inválidos por _
    cleaned_filename = re.sub(f'[{re.escape(invalid_chars)}]', '_', filename)
    return cleaned_filename

def download_video(link, saida):
    try:
        # Cria o objeto YouTube
        yt = YouTube(link)
        video_title = yt.title
        base_filename = clean_filename(video_title)
        
        # Verifica se o nome base já existe na pasta
        counter = 1
        while True:
            diretorio = os.path.join(saida, f"{base_filename}_Download{counter:02}")
            if not os.path.exists(f"{diretorio}.mp3"):
                break
            counter += 1

        # Seleciona a stream de vídeo de maior qualidade
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        # Baixa o vídeo
        stream.download(filename=f'{diretorio}.mp4')
        
        # Converte para mp3
        video_clip = mp.VideoFileClip(f'{diretorio}.mp4')
        video_clip.audio.write_audiofile(f'{diretorio}.mp3')
        video_clip.close()

        # Remove o arquivo de vídeo mp4 após a conversão para mp3
        os.remove(f'{diretorio}.mp4')

        messagebox.showinfo(title="Concluido!", message=f"Download Concluído: {os.path.basename(diretorio)}")

    except Exception as e:
        messagebox.showerror(title="Erro!", message=f"Erro: {e}")

# Exemplo de uso
link = show_custom_dialog()

if link is not None:  # Verifica se o usuário não cancelou
    out = askdirectory()
    if out:
        download_video(link, out)
    else:
        messagebox.showerror(title="Erro!", message="Por favor, selecione um diretório válido.")
