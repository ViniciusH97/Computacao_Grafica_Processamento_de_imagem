import cv2

imagem = cv2.imread("imagens de morango/morango_laranja.png")

altura, largura, canais = imagem.shape

with open("imagens de morango/area_da_imagem.txt", "w") as arquivo:
    for i in range(altura):
        for j in range(largura):
            pixel_cor = imagem[i, j]
            arquivo.write(f"Pixel ({i}, {j}): {pixel_cor}\n")
