import numpy
import cv2

# arr = cv2.imread("image.png")
#
# print(arr.shape)
# print(arr)

arr = numpy.array([[[255,   0,   0],
  [255, 255, 255],
  [255, 255, 255],
  [187,  41, 160]],

[[255, 255, 255],
  [255, 255, 255],
  [255, 255, 255],
  [255, 255, 255]],

[[255, 255, 255],
  [  0,   0,   150],
  [ 47, 255, 173],
  [255, 255, 255]]])

cv2.imwrite("another_image.png", arr)