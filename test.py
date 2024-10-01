import yt_dlp

# URL do vídeo que você quer baixar
video_url = 'https://www.youtube.com/watch?v=TP4_cdeRmBk'

def download_video(url):
    ydl_opts = {
        'outtmpl': './img/%(title)s.%(ext)s',
        'format': 'best',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# URL do vídeo
download_video(video_url)
