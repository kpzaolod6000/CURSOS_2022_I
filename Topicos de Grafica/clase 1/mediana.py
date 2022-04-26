
import numpy as np
import cv2
from time import time
#import matplotlib.pyplot as plt

def mediana(imgTest,kernel):

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


result = []
imgReal = []


for img in imgs:
    imgGray = cv2.imread('./img/'+ img ,0)
    imgReal.append(imgGray)
    
    for nk in nKernel:
       
        kernel = np.ones((nk,nk), dtype=np.int32)  #filtro

        start_time = time()
        imgFilter = mediana(imgGray,kernel)
        elapsed_time = time() - start_time
        
        print('\nMediana' + str(nk) + 'x' + str(nk) + img)
        print("Tiempo transcurrido: %0.10f segundos." % (elapsed_time))

        
        result.append(imgFilter)
        filename = './img/imgMediana/' + 'Mediana' + str(nk) + 'x' + str(nk) + img
        cv2.imwrite(filename, imgFilter)

def concat_tile(im_list_2d):
    return cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in im_list_2d])

for i in range(len(result)):
    result[i] = cv2.resize(result[i], dsize=(0, 0), fx=0.8, fy=0.8)

for i in range(len(imgReal)):
    imgReal[i] = cv2.resize(imgReal[i], dsize=(0, 0), fx=0.8, fy=0.8)    

im_Figures = concat_tile([[imgReal[0],result[0],result[1],result[2]]])
im_Zebra   = concat_tile([[imgReal[1],result[3],result[4],result[5]]])
im_LenaG   = concat_tile([[imgReal[2],result[6],result[7],result[8]]])
im_LenaS   = concat_tile([[imgReal[3],result[9],result[10],result[11]]])



cv2.imshow("Resultados figures",im_Figures)
cv2.imshow("Resultados zebra",im_Zebra)
cv2.imshow("Resultados lenaG",im_LenaG)
cv2.imshow("Resultados lenaS",im_LenaS)


cv2.waitKey(0)

