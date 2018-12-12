import cv2
import numpy as np

img = cv2.imread("./mb_175897_6011 (1).jpg")
mask = np.matrix('-1 -1 -1; -1 16 -1; -1 -1 -1')
mat_sum = mask.sum()

h = img.shape[0]
w = img.shape[1]

for y in range(1, h-1):
    for x in range(1, w-1):
        img[y, x] = ((img[y-1, x-1]*mask[0, 0]+img[y, x-1]*mask[0, 1] +
                      img[y+1, x-1]*mask[0, 2]+img[y-1, x]*mask[1, 0]+img[y, x]*mask[1, 1]+img[y, x+1]*mask[1, 2] +
                      img[y-1, x+1]*mask[2, 0]+img[y, x+1]*mask[2, 1]+img[y+1, x+1]*mask[2, 2])/mat_sum)

cv2.imshow('priv', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
