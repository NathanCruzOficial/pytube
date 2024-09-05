import customtkinter as ctk  # Certifique-se de que o customtkinter esteja instalado
import base64
from io import BytesIO
from PIL import Image

# img base64
from img import download, folder, ico

# Função para decodificar imagens base64
def decode_base64_to_image(base64_data):
    image_data = base64.b64decode(base64_data)
    return Image.open(BytesIO(image_data))

# Dicionário contendo as strings base64 para fácil acesso
image_sources = {
    'download': download.image_base64,
    'folder': folder.image_base64,
    'ico': ico.icon_base64
}
# Decodificar as imagens
decoded_img = {name: decode_base64_to_image(image_data) for name, image_data in image_sources.items()}
