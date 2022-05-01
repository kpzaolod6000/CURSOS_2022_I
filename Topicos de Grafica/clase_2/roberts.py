
import numpy as np
import cv2

def Roberts(imgTest,filterGx,filterGy):

    Img = imgTest.copy()

    n , m = imgTest.shape
    nK, mK = filterGx.shape
  
    for i in range(1,n - nK + 1):
        for j in range(1,m - mK + 1):
            slicing = imgTest[i:i+nK, j:j+mK]
            
            multiGx = np.multiply(slicing,filterGx)
            multiGy = np.multiply(slicing,filterGy)
            
            Gx = pow(np.sum(multiGx),2)
            Gy = pow(np.sum(multiGy),2)
            Gxy = np.sqrt(Gx+Gy)
            
            Img[i][j] = Gxy
    return Img


imgs = ['blancoNegro.png','circuit.jpg']
imgReal = []
imgFilters = []

for img in imgs: 

    imgGray = cv2.imread('./img/'+img ,0)
    imgReal.append(imgGray)
    # cv2.imshow("original", imgGray)
    

    filterGx = np.array([[1, 0],
                        [0,-1]])

    filterGy = np.array([[ 0,1],
                        [-1,0]])

    imgFilter = Roberts(imgGray,filterGx,filterGy)
    imgFilters.append(imgFilter)
    # cv2.imshow("Roberts"+img, imgFilter)

    filename = './img/imgRoberts/roberts' + img
    cv2.imwrite(filename, imgFilter)



for i in range(len(imgReal)):
    imgReal[i] = cv2.resize(imgReal[i], dsize=(0, 0), fx=2.5, fy=2.5)
    imgFilters[i] = cv2.resize(imgFilters[i], dsize=(0, 0), fx=2.5, fy=2.5)
    im_1 = cv2.hconcat([imgReal[i], imgFilters[i]])
    cv2.imshow("Roberts"+imgs[i], im_1)
cv2.waitKey(0)
