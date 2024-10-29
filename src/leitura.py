from PIL import Image, ImageShow
import numpy as np

def calcular_media(foto):
    largura, altura = foto.size
    media = 0
    for x in range(largura):
        for y in range(altura):
            r, g, b = foto.getpixel((x, y))
            media += r + g + b
    return media / (largura * altura * 3)

def calcular_desvio_padrao(fotos):
    medias = [calcular_media(foto) for foto in fotos]
    return np.std(medias)

def processar_imagem(img, media_referencia, desvio_padrao_referencia):
    largura, altura = img.size
    nova_imagem = Image.new('RGB', (largura, altura))
    limite_inferior = media_referencia - desvio_padrao_referencia
    limite_superior = media_referencia + desvio_padrao_referencia

    for x in range(largura):
        for y in range(altura):
            r, g, b = img.getpixel((x, y))
            
            if (r > 150 and g < 100 and b < 100):
                nova_imagem.putpixel((x, y), (r, g, b))
            elif (r < 100 and g > 100 and b < 100):  
                nova_imagem.putpixel((x, y), (0, 0, 0))
            else:
                nova_imagem.putpixel((x, y), (0, 0, 0))

    return nova_imagem

foto1 = Image.open('padrao morango/foto_morango1.png').convert('RGB')
foto2 = Image.open('padrao morango/foto_morango2.png').convert('RGB')
foto3 = Image.open('padrao morango/foto_morango3.png').convert('RGB')

medias = [calcular_media(foto1), calcular_media(foto2), calcular_media(foto3)]
desvio_padrao = calcular_desvio_padrao([foto1, foto2, foto3])
media_referencia = np.mean(medias)

print('Média da foto1: ', medias[0])
print('Média da foto2: ', medias[1])
print('Média da foto3: ', medias[2])
print('Desvio padrão: ', desvio_padrao)

img = Image.open('strawberries-3359755-1920-1-.webp').convert('RGB')
img_processada = processar_imagem(img, media_referencia, desvio_padrao)

ImageShow.show(img_processada)
