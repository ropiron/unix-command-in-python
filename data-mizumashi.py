import numpy as np
import cv2

#画像変換条件
filter1 = np.array([[0, 1, 0],
                   [1, 0, 1],
                   [0, 1, 0]], np.uint8)
filter2 = np.ones((3, 3))

list_resize = [2, 3, 5, 7]
list_mosaic = [3, 5, 7, 10]
list_rotation = [45, 135, 225, 315]
list_flip = [0, 1, -1]
list_cvt1 = [0]
list_cvt2 = [0]
list_THRESH_BINARY = [50, 100, 150, 200]
list_THRESH_BINARY_INV = [50, 100, 150, 200]
list_THRESH_TRUNC = [50, 100, 150, 200]
list_THRESH_TOZERO = [50, 100, 150, 200]
list_THRESH_TOZERO_INV = [50, 100, 150, 200]
list_gauss = [11, 31, 51, 71]
list_gray = [0]
list_nois_gray = [0]
list_nois_color = [0]
list_dilate = [filter1, filter2]
list_erode = [filter1, filter2]

parameters = [list_resize, list_mosaic, list_rotation, list_flip, list_cvt1, list_cvt2, list_THRESH_BINARY, \
              list_THRESH_BINARY_INV, list_THRESH_TRUNC, list_THRESH_TOZERO, list_THRESH_TOZERO_INV, list_gauss, \
              list_gray, list_nois_gray, list_nois_color, list_dilate, list_erode]

#水増し画像の合計
list_sum =len(list_resize) + len(list_mosaic) + len(list_rotation) + len(list_flip) + len(list_cvt1) + len(list_cvt2) + \
          len(list_THRESH_BINARY) + len(list_THRESH_BINARY_INV) + len(list_THRESH_TRUNC) + len(list_THRESH_TOZERO) + \
          len(list_THRESH_TOZERO_INV) + len(list_gauss) + len(list_gray) + len(list_nois_gray) + len(list_nois_color) + \
          len(list_dilate) + len(list_erode)
print("合計：{}枚".format(list_sum))

#実行する関数のリスト
methods = np.array([lambda i: cv2.resize(img, (img.shape[1] // i, img.shape[0] // i)),
                    lambda i: cv2.resize(cv2.resize(img, (img.shape[1] // i, img.shape[0] // i)), (img.shape[1],img.shape[0])),
                    lambda i: cv2.warpAffine(img, cv2.getRotationMatrix2D(tuple(np.array([img.shape[1] / 2, img.shape[0] /2])), i, 1), (img.shape[1], img.shape[0])),
                    lambda i: cv2.flip(img, i),
                    lambda i: cv2.cvtColor(img, cv2.COLOR_BGR2LAB),
                    lambda i: cv2.bitwise_not(img),
                    lambda i: cv2.threshold(img, i, 255, cv2.THRESH_BINARY)[1],
                    lambda i: cv2.threshold(img, i, 255, cv2.THRESH_BINARY_INV)[1],
                    lambda i: cv2.threshold(img, i, 255, cv2.THRESH_TRUNC)[1],
                    lambda i: cv2.threshold(img, i, 255, cv2.THRESH_TOZERO)[1],
                    lambda i: cv2.threshold(img, i, 255, cv2.THRESH_TOZERO_INV)[1],
                    lambda i: cv2.GaussianBlur(img, (i, i), 0),
                    lambda i: cv2.imread(".pos/Screenshot from 2020-05-22 11-38-35.png", i),
                    lambda i: cv2.fastNlMeansDenoising(cv2.imread(".pos/Screenshot from 2020-05-22 11-38-35.png", i)),
                    lambda i: cv2.fastNlMeansDenoisingColored(img),
                    lambda i: cv2.dilate(img, i),
                    lambda i: cv2.erode(img, i)
                   ])

#水増し画僧の保存用関数
def save(cnv_img):
    cv2.imwrite(".pos/img" + str(num) + ".png", cnv_img)

#画像タイトル用ナンバーの初期化
num = 0

#元画像の読み込み
img = cv2.imread(".pos/Screenshot from 2020-05-22 11-38-35.png")

#画像の水増しと保存
for ind, method in enumerate(methods):
    for parameter in parameters[ind]:
        num += 1
        cnv_img = method(parameter)
        save(cnv_img)
