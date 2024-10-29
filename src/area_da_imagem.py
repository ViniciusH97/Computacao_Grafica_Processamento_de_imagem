from PIL import Image, ImageTk, ImageDraw
import numpy as np

x_inicial = None
y_inicial = None
x_final = None
y_final = None

def calcular_mediana_morango(foto):
    pixels = np.array(foto)
    r = pixels[:, :, 0].flatten()
    g = pixels[:, :, 1].flatten()
    b = pixels[:, :, 2].flatten()

    mediana_r = np.median(r)
    mediana_g = np.median(g)
    mediana_b = np.median(b)

    return mediana_r, mediana_g, mediana_b

def calcular_media_area(foto, x_inicial, y_inicial, x_final, y_final):
    media_r = 0
    media_g = 0
    media_b = 0
    total_pixels = 0

    x = x_inicial
    while x < x_final:
        y = y_inicial
        while y < y_final:
            r, g, b = foto.getpixel((x, y))
            media_r += r
            media_g += g
            media_b += b
            total_pixels += 1
            y += 1
        x += 1

    if total_pixels == 0:
        return (0, 0, 0)

    return (media_r / total_pixels, media_g / total_pixels, media_b / total_pixels)


def verificar_se_e_morango(media_area, mediana_morango, tolerancia=20):
    return (abs(media_area[0] - mediana_morango[0]) <= tolerancia and
            abs(media_area[1] - mediana_morango[1]) <= tolerancia and
            abs(media_area[2] - mediana_morango[2]) <= tolerancia)

def on_button_press(event):
    global x_inicial, y_inicial
    x_inicial, y_inicial = event.x, event.y

def on_mouse_drag(event):
    global x_final, y_final
    x_final, y_final = event.x, event.y
    draw_rectangle()

def draw_rectangle():
    img_copy = img.copy()
    draw = ImageDraw.Draw(img_copy)
    draw.rectangle([x_inicial, y_inicial, x_final, y_final], outline="red", width=2)
    img_tk = ImageTk.PhotoImage(img_copy)
    label.config(image=img_tk)
    label.image = img_tk

def on_button_release(event):
    global x_final, y_final
    x_final, y_final = event.x, event.y

    if x_inicial is not None and y_inicial is not None:
        media_area = calcular_media_area(img, min(x_inicial, x_final), min(y_inicial, y_final), max(x_inicial, x_final), max(y_inicial, y_final))
        if verificar_se_e_morango(media_area, mediana_morango):
            resultado['text'] = f"A área selecionada faz parte do morango!"
        else:
            resultado['text'] = f"A área selecionada NÃO faz parte do morango."

img = Image.open('morango_laranja.png').convert('RGB')
mediana_morango = calcular_mediana_morango(img)

