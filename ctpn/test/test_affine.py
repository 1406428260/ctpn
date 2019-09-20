import cv2,numpy as np


def do(img,bottom_offset, is_top_fix):

    TEN_PIX = 10
    HUNDRED_PIX = 100

    old_shape = img.shape
    height = img.shape[0]

    offset_ten_pixs = int(TEN_PIX*bottom_offset/height)
    width = int(img.shape[1] * (1 + bottom_offset / HUNDRED_PIX))

    print("new offset=%d" % offset_ten_pixs)
    print("new width=%d" % width)

    pts1 = np.float32([[0, 0], [HUNDRED_PIX, 0], [0, TEN_PIX]])  # 这就写死了，当做映射的3个点：左上角，左下角，右上角
    if is_top_fix:  # 上边固定，意味着下边往右
        pts2 = np.float32([[0, 0], [HUNDRED_PIX, 0], [offset_ten_pixs, TEN_PIX]])  # 看，只调整左下角
        M = cv2.getAffineTransform(pts1, pts2)
        img = cv2.warpAffine(img, M, (width,height))
    else:  # 下边固定，意味着上边往右
        # 得先把图往右错位，然后
        # 先右移
        print("右移")
        H = np.float32([[1, 0, bottom_offset], [0, 1, 0]])  #
        img = cv2.warpAffine(img, H, (width,height))
        # 然后固定上部，移动左下角
        pts2 = np.float32([[0, 0], [HUNDRED_PIX, 0], [-offset_ten_pixs, TEN_PIX]])  # 看，只调整左下角
        M = cv2.getAffineTransform(pts1, pts2)
        img = cv2.warpAffine(img, M, (width,height))  #

    new_shape = img.shape

    print("shape:%r=>%r" % (old_shape,new_shape))
    return img

img = cv2.imread("lena.png")
img = do(img,25,False)
cv2.imwrite("out.png",img)