import cv2,numpy as np

# 测试各种画图
img = cv2.imread("bg.png")
img_size = img.shape
print(img_size)
im_size_min = np.min(img_size[0:2])
print(im_size_min)
points = np.array([[910, 650], [206, 650], [458, 500], [696, 500]])
cv2.polylines(img, [points], True, color=(0, 255, 0),thickness=5)
cv2.putText(img, "12",
            (910, 650),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=0.5,
            thickness=2,
            color=(0,0,255),
            lineType=1)
cv2.imwrite('out.png',img)

img = cv2.imread("lena.png")
cv2.imwrite('lena.out.png',img[:, :, ::-1])

print(img.shape)
