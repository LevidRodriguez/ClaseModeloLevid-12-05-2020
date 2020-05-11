import cv2
from google.colab.patches import cv2_imshow
def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    resized = cv2.resize(image, dim, interpolation = inter)
    return resized

# imgA = cv2.imread('DJI_0878.JPG');imgB = cv2.imread('DJI_0879.JPG')
# imgA = image_resize(imgA, 640, 480);imgB = image_resize(imgB, 640, 480)
# cv2.imwrite('newDJI_0878.JPG',imgA);cv2.imwrite('newDJI_0879.JPG',imgB)