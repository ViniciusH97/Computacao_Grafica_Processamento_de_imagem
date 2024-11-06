import cv2
import matplotlib.pyplot as plt

#verificar a versão do opencv
print(cv2.__version__)

#carregar a imagem
imagem = cv2.imread('imagem.png')
plt.imshow(imagem[:,:,::-1])
plt.show()

input("Pressione qualquer tecla para continuar...")

sr = cv2.dnn_superres.DnnSuperResImpl_create()
 
path = "models\EDSR_x4.pb"
 
sr.readModel(path)
 
sr.setModel("edsr",4)
 
result = sr.upsample(imagem)
 
# Resized image
resized = cv2.resize(imagem,dsize=None,fx=4,fy=4)
 
plt.figure(figsize=(12,8))
plt.subplot(1,3,1)
# Original image
plt.imshow(imagem[:,:,::-1])
plt.subplot(1,3,2)
# SR upscaled
plt.imshow(result[:,:,::-1])
plt.subplot(1,3,3)
# OpenCV upscaled
plt.imshow(resized[:,:,::-1])
plt.show()