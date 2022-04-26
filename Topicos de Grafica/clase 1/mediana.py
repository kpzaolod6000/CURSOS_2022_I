
import numpy as np
import cv2
from time import time
import matplotlib.pyplot as plt

def media(imgTest,kernel):

    imgFilter = imgTest.copy()

    n , m = imgTest.shape
    nK, mK = kernel.shape
    ptoMiddle = nk//2

    for i in range(n - nK + 1):
        for j in range(m - mK + 1):
            slicing = imgTest[i:i+nK, j:j+mK]
            listSlicing = np.ravel(slicing)
            sortSlicing = np.sort(listSlicing)
            
            imgFilter[i+ptoMiddle][j+ptoMiddle] = sortSlicing[(len(sortSlicing)//2)]
    return imgFilter



nKernel = [3,5,9]
imgs = ['figures.jpg',
        'zebra.jpg',
        'lenaG.png',
        'lenaS.png']

# result = []

for img in imgs:
    imgGray = cv2.imread('./img/'+ img ,0)
    cv2.imshow("original", imgGray)
    
    for nk in nKernel:
       
        kernel = np.ones((nk,nk), dtype=np.int32)  #filtro

        start_time = time()
        imgFilter = media(imgGray,kernel)
        elapsed_time = time() - start_time
        
        print('\nMediana' + str(nk) + 'x' + str(nk) + img)
        print("Tiempo transcurrido: %0.10f segundos." % (elapsed_time))

        
        cv2.imshow("Mediana " + str(nk) + "x" + str(nk), imgFilter)       
        filename = './imgResult/' + 'Mediana' + str(nk) + 'x' + str(nk) + img
        cv2.imwrite(filename, imgFilter)

cv2.waitKey(0)

