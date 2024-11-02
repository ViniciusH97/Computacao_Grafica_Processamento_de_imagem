import cv2

imagem = cv2.imread("src/morango_laranja.png")

altura, largura, canais = imagem.shape

# Leitura de todos os pixels da imagem
for i in range(altura):
    for j in range(largura):
        pixel_cor = imagem[i, j]
        print(pixel_cor)
