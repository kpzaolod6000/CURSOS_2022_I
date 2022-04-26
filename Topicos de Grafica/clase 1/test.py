
import numpy as np
import cv2
 
# Cargamos la imagen
imgGray = cv2.imread('./img/camera_man2.png',0)
cv2.imshow("original", imgGray)

kernel = np.ones((3,3), dtype=np.int32)  #filtro
tamX, tamY = kernel.shape
print(imgGray)
# print(kernel)

imgFiltrado = imgGray.copy()
imgFiltrado = np.array(imgFiltrado)
n,m = imgFiltrado.shape


for i in range(n - tamX + 1):
    for j in range(m - tamY + 1):
        sum = 0
        indx = 0
        for i_x in range(i,i+tamX):
            indy = 0
            for j_y in range(j,j+tamY):
                pixel = imgFiltrado[i_x][j_y] 
                sum += (pixel * kernel[indx][indy])
                indy += 1
            indx += 1
        imgFiltrado[i+1][j+1] = sum/(tamX*tamY)

print(imgFiltrado)
cv2.imshow("Filtrado", imgFiltrado)
cv2.waitKey(0)
