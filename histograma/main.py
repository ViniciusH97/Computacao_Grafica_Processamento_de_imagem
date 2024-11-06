import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

#mostrar a versão do OpenCV
print(cv.__version__)

#carregar a imagem
imagem = cv.imread('imagem.png')
plt.imshow(imagem[:,:,::-1])
plt.show()

imagem = cv.imread('imagem.png', cv.IMREAD_GRAYSCALE)
assert imagem is not None, "file could not be read, check with os.path.exists()"
plt.hist(imagem.ravel(),256,[0,256]); plt.show()

#Gráfico BGR

imagem = cv.imread('imagem.png')
assert imagem is not None, "file could not be read, check with os.path.exists()"
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv.calcHist([imagem],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()

# APLICAÇÃO DE MÁSCARA

#criar uma máscara
mask = np.zeros(imagem.shape[:2], np.uint8)
mask[100:300, 100:400] = 255
masked_img = cv.bitwise_and(imagem, imagem, mask=mask)

# Calcular o histograma com e sem a máscara
# verificar o terceiro argumento para a máscara

hist_full = cv.calcHist([imagem],[0],None,[256],[0,256])
hist_mask = cv.calcHist([imagem],[0],mask,[256],[0,256])

plt.subplot(221), plt.imshow(imagem, 'gray')
plt.subplot(222), plt.imshow(mask,'gray')
plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0,256])

plt.show()