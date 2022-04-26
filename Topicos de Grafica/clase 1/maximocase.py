
import numpy as np
import cv2
 

def media(imgTest,kernel):

    imgFilter = imgTest.copy()

    n , m = imgTest.shape
    nK, mK = kernel.shape
    ptoMiddle = nK//2
    
    for i in range(n - nK + 1):
        for j in range(m - mK + 1):
            slicing = imgTest[i:i+nK, j:j+mK]
            max_ = np.max(slicing)
            imgFilter[i+ptoMiddle][j+ptoMiddle] = max_
    return imgFilter

kernel = np.ones((3,3), dtype=np.int32)  #filtro
test5x5 = np.random.randint(100, size=(5,5))
print(kernel)
print(test5x5)
print(media(test5x5,kernel))