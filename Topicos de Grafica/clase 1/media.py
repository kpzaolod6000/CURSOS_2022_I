
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
            multiMatrix = np.multiply(slicing,kernel)
            sum = np.sum(multiMatrix) / (nK*mK)
            
            imgFilter[i+ptoMiddle][j+ptoMiddle] = sum
    return imgFilter



nKernel = [3,5,9]
imgs = ['figures.jpg',
        'zebra.jpg',
        'lenaG.png',
        'lenaS.png']

# result = []

for img in imgs:
    imgGray = cv2.imread('./img/'+ img ,0)
    # cv2.imshow("original", imgGray)
    
    for nk in nKernel:
       
        kernel = np.ones((nk,nk), dtype=np.int32)  #filtro

        start_time = time()
        imgFilter = media(imgGray,kernel)
        elapsed_time = time() - start_time
        
        print('\nMedia' + str(nk) + 'x' + str(nk) + img)
        print("Tiempo transcurrido: %0.10f segundos." % (elapsed_time))

        
        # cv2.imshow("Media " + str(nk) + "x" + str(nk), imgFilter)
        # result.append(imgFilter)
        
        filename = './imgResult/' + 'Media' + str(nk) + 'x' + str(nk) + img
        cv2.imwrite(filename, imgFilter)


# def concat_tile(im_list_2d):
#     return cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in im_list_2d])

# for i in range(len(result)):
#     result[i] = cv2.resize(result[i], dsize=(0, 0), fx=0.5, fy=0.5)    

# im_tile = concat_tile(result)


# cv2.imshow("Resultados",im_tile)
# cv2.imwrite('./resultadomedia.jpg', im_tile)

cv2.waitKey(0)

