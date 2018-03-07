# import the necessary packages
import numpy as np
import argparse
import cv2

img = cv2.imread('../test_data/data1.png', 0)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()