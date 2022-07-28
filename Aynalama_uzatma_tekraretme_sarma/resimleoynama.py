import cv2
import numpy as np

resim = cv2.imread("valo.jpg")


#Reflect = yansıtmak.
resmiaynalama = cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_REFLECT)

#Replicate = tekrarlamak.
resmiuzatma = cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_REPLICATE)

#Wrap = paketlemek.
resmitekrar = cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_WRAP)

#Constant = devamlı.
resmisarma = cv2.copyMakeBorder(resim,100,100,100,100, cv2.BORDER_CONSTANT)

#resmi sarma işlemini ekranda göster.
cv2.imshow("sarma", resmisarma)


cv2.waitKey(0)
cv2.destroyAllWindows()