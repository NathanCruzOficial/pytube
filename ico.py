import tkinter as tk
import base64
from io import BytesIO
from PIL import Image, ImageTk
from icone_base64 import icon_base64 # Sua string base64 aqui


# Decodifique a string base64
icon_data = base64.b64decode(icon_base64)
icon_image = Image.open(BytesIO(icon_data))

# Crie o aplicativo Tkinter
root = tk.Tk()

# Converta a imagem para um formato que Tkinter possa usar
icon = ImageTk.PhotoImage(icon_image)

# Configure o ícone da janela
root.iconphoto(True, icon)

# Exemplo de widget
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

# Inicie o loop principal do Tkinter
root.mainloop()
