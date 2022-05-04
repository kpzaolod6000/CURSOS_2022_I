
import numpy as np
import cv2

def Sobel(imgTest,filterGx,filterGy):

    Img = imgTest.copy()

    n , m = imgTest.shape
    nK, mK = filterGx.shape
    pntMiddle = nK//2
    

    for i in range(n - nK + 1):
        for j in range(m - mK + 1):
            slicing = imgTest[i:i+nK, j:j+mK]
            
            multiGx = np.multiply(slicing,filterGx)
            multiGy = np.multiply(slicing,filterGy)
            Gx = pow(np.sum(multiGx),2)
            Gy = pow(np.sum(multiGy),2)
            Gxy = np.sqrt(Gx+Gy)
            
            Img[i+pntMiddle][j+pntMiddle] = Gxy
            
    return Img


imgs = ['blancoNegro.png','circuit.jpg']

imgReal = []
imgFilters = []

for img in imgs: 

    imgGray = cv2.imread('./img/'+img ,0)
    imgReal.append(imgGray)
    # cv2.imshow("original", imgGray)
    

    filterGx = np.array([[1, 0, -1],
                         [2, 0, -2],
                         [1, 0, -1]])

    filterGy = np.array([[ 1,  2,  1],
                         [ 0,  0,  0],
                         [-1, -2, -1]])

    imgFilter = Sobel(imgGray,filterGx,filterGy)
    imgFilters.append(imgFilter)
    # cv2.imshow("Sobel"+img, imgFilter)

    filename = './img/imgSobel/Sobel' + img
    cv2.imwrite(filename, imgFilter)

for i in range(len(imgReal)):
    imgReal[i] = cv2.resize(imgReal[i], dsize=(0, 0), fx=2.5, fy=2.5)
    imgFilters[i] = cv2.resize(imgFilters[i], dsize=(0, 0), fx=2.5, fy=2.5)
    im_1 = cv2.hconcat([imgReal[i], imgFilters[i]])
    cv2.imshow("Sobel"+imgs[i], im_1)


cv2.waitKey(0)
