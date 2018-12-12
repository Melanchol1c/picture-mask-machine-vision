import cv2
import numpy as np

img = cv2.imread("./mb_175897_6011.jpg")
kernel = np.array([[-1, -1, -1],
                   [-1, 16, -1],
                   [-1, -1, -1]], np.float32)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

dst1 = cv2.filter2D(img, -1, kernel)

cv2.imshow('priv', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
