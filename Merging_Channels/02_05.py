import numpy as np
import cv2

color = cv2.imread("butterfly.jpg",1)

gray = cv2.cvtColor(color, cv2.COLOR_RGB2GRAY)
cv2.imwrite("gray.png",gray)

b = color[:,:,0]
g = color[:,:,1]
r = color[:,:,2]

rgba = cv2.merge((r,g,b,g))
cv2.imwrite("rgbs.png",rgba)