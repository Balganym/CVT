import cv2
import numpy as np
from random import randint, uniform
import string, random
import os



def addNoise(image):    
    row,col = image.shape
    s_vs_p = 0.4
    amount = 0.01
    out = np.copy(image)
    # Salt mode
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt))
          for i in image.shape]
    out[coords] = 1

    # Pepper mode
    num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    out[coords] = 0
    return out


# def addLines(img):
#     for i in range(randint(0,2)):
#         y1 = randint(0, img.shape[0])
#         y2 = randint(0, img.shape[0])
#         cv2.line(img, (0, y1), (img.shape[1], y2), 0, 1)


def addBlur(img, kw, kh):
    return cv2.blur(img, (kw, kh))


def text_generator(chars, size = 8):
    return ''.join(random.choice(chars) for _ in range(size))


def addText(img, chars, font, size, line_size):

    text = text_generator(chars, 1)    

    cv2.putText(img, text, (0, img.shape[0]-4), font, size, (0, 0, 255), line_size, cv2.LINE_AA)

    return text

sizes = [(70,58),(40,35),(75,70),(70,70),(70,70),(50,50)]

def genSymbolImg(chars = string.ascii_uppercase + string.digits,
                font = None,
                line_size = None,
                blur = None,
                kw = None, 
                kh = None):

    if font is None:
        font = randint(0, 5)

    # if size is None:
    #     size = uniform(2.5, 3.5)

    if line_size is None:
        line_size = randint(1, 3)

    if blur is None:
        blur = randint(0, 1)

    if kw is None:
        kw = randint(3, 9)

    if kh is None:
        kh = randint(3, 9)


    genImg = np.full(sizes[font], 255, dtype= np.uint8)

    text = addText(genImg, chars, font, 3, line_size)

    if randint(0, 1):
        genImg = addNoise(genImg)
        
    # if lines:
    #     addLines(genImg)

    if blur:
        genImg = addBlur(genImg, kw, kh)


    return genImg, text



if __name__ == '__main__':

    os.chdir('test_set')
    cnt = 0
    for i in xrange(1000):
        img, text = genSymbolImg(kw = 5, kh = 5, blur = 1)
        cnt = cnt + 1
        cv2.imwrite('./'+ str(cnt) + ".jpg", img)
        # print text

        cv2.imshow("W", img)
        # k = cv2.waitKey(0)
        # if k == 27:
        #     break