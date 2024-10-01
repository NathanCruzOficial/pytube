import re
import requests
from PIL import Image, ImageTk
from io import BytesIO
import color
import pytube as yt

#Valores
margem = 450

def validate_youtube_link(link):
    # Regex para validar URLs do YouTube
    youtube_regex = (
        r'(https?://)?(www\.)?'           # Protocolo opcional e 'www.' opcional
        r'(youtube|youtu|youtube-nocookie)\.(com|be)/'  # Domínios válidos do YouTube
        r'(watch\?v=|embed/|v/|.+\?v=)?'  # Formatos comuns de URLs do YouTube
        r'([^&=%\?]{11})'                 # O identificador de vídeo (11 caracteres)
    )
    # Verifica se o link corresponde ao regex e retorna True ou False
    return bool(re.match(youtube_regex, link))



def start_download(url,aviso,mode):
    if validate_youtube_link(url.get()):
        video_url = url.get()
        print(video_url)
        YtObject = yt.YouTube(video_url)
        video_info = {
            "title": YtObject.title,
            "thumbnail_url": YtObject.thumbnail_url,
            "length": YtObject.length,
            "author": YtObject.author
        }
        try:
            video = YtObject.streams.filter(file_extension=mode).get_highest_resolution()
            video.download()
            print("Download concluído!")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
        

        # if mode == "mp4":
        #     video = YtObject.streams.filter(file_extension="mp4")
        #     video.download()
        # elif mode == "mp3":
        #     video = YtObject.streams.filter(file_extension="mp3",only_audio=True)
        #     video.download()
        # else:
        #     video = YtObject.streams.filter(file_extension="mov")
        #     video.download()

    else:
        url.configure(border_color=color.red)