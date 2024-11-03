import cv2
import numpy as np
import matplotlib.pyplot as plt

## AQUI CALCULA-SE A MEDIA DE COR DE UMA IMAGEM
def calcular_media_cor(imagem_path):
    imagem = cv2.imread(imagem_path)
    imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
    media_cor = np.mean(imagem.reshape(-1, 3), axis=0)
    return media_cor

padrões_morango = [
    calcular_media_cor("padrao morango/foto_morango1.png"),
    calcular_media_cor("padrao morango/foto_morango2.png"),
    calcular_media_cor("padrao morango/foto_morango3.png"),
    calcular_media_cor("padrao morango/foto_morango4.png"),
    calcular_media_cor("padrao morango/foto_morango5.png"),
    calcular_media_cor("padrao morango/foto_morango6.png"),
    calcular_media_cor("padrao morango/foto_morango7.png"),
    calcular_media_cor("padrao morango/foto_morango8.png"),
]

def cores_semparelhadas(cor1, cor2, tolerancia=40):
    distancia = np.linalg.norm(cor1 - cor2)
    return distancia < tolerancia

def colorir_morango_azul(imagem_path):
    imagem = cv2.imread(imagem_path)
    imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
    imagem_azul = imagem_rgb.copy()

    for i in range(imagem_rgb.shape[0]):
        for j in range(imagem_rgb.shape[1]):
            pixel_cor = imagem_rgb[i, j]
            if any(cores_semparelhadas(pixel_cor, padrao) for padrao in padrões_morango):
                imagem_azul[i, j] = [0, 0, 255]

    plt.subplot(1, 2, 1)
    plt.imshow(imagem_rgb)
    plt.title("Imagem Original")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(imagem_azul)
    plt.title("Morango em Azul")
    plt.axis("off")

    plt.show()

colorir_morango_azul("imagens de morango\morango-maduro-vermelho-perfeito-com-isolado-de-folha_131956-722.jpg")
