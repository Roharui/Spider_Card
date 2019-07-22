
import pyautogui as pag
import cv2
import numpy
from time import sleep

x, y = (930, 32)

'''
while True:
    print(pag.position())
    sleep(1)


img = pag.screenshot('test.jpg',
 region=(x, y, 920, pag.size()[1] / 2 - 32))
 '''

a = cv2.imread('test.jpg')

cv2.imshow("ori", a)
cv2.imshow('test', a[113:113 + 15, 57:57 + 15])
cv2.waitKey(0)
cv2.destroyAllWindows()