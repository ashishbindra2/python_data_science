from cv2 import (imread, rectangle,
                 imwrite, imshow, waitKey, resizeWindow, namedWindow, WINDOW_NORMAL)

#  cv2.rectangle(image, start_point, end_point, color, thickness)
# image: The image on which to draw the rectangle.
# start_point: The coordinates of the top-left corner of the rectangle (x, y).
# end_point: The coordinates of the bottom-right corner of the rectangle (x + width, y + height).
# color: The color of the rectangle. This is given in BGR format, for example, (255, 0, 0) for blue.
# thickness: The thickness of the rectangle's border. If you set it to -1, it will fill the rectangle

img = imread('./I1.png')
x = 400
y = 700
h = 300
w = 450

abc = img[y:y + h, x:x + w]

imwrite('./I2.png', abc)
rectangle(img, (x, y), (x + w, y + h), (222, 0, 0, 222), 5)

namedWindow("Resized_Window", WINDOW_NORMAL)
resizeWindow("Resized_Window", 1300, 800)
imshow("Resized_Window", img)

waitKey(0)
