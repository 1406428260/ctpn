# 这个是为了测试split，把不规则四边形切成小的GT的代码
import cv2
import numpy as np
from shapely.geometry import Polygon

IGNORE_WIDTH = 3

def _p(msg,obj):
    print(msg,end='')
    print(obj)


def pickTopLeft(poly):
    # 按照第一列，也就是x，进行排序，从小到大排，最左面在前面
    idx = np.argsort(poly[:, 0])
    # 比较最左面的第2个点的y>第1个点的y
    if poly[idx[0], 1] < poly[idx[1], 1]:
        s = idx[0] # 找到左上角，也就是用最靠左面的2个点，找那个最上面的点，s是对应的point的行号
    else:
        s = idx[1]

    # 返回的是
    print("poly[(%d, %d, %d, %d),:]" % (s, (s + 1) % 4, (s + 2) % 4, (s + 3) % 4))
    return poly[(s, (s + 1) % 4, (s + 2) % 4, (s + 3) % 4), :]


def shrink_poly(poly, r=16):
    # y = kx + b
    x_min = int(np.min(poly[:, 0]))
    x_max = int(np.max(poly[:, 0]))

    k1 = (poly[1][1] - poly[0][1]) / (poly[1][0] - poly[0][0])
    b1 = poly[0][1] - k1 * poly[0][0]

    k2 = (poly[2][1] - poly[3][1]) / (poly[2][0] - poly[3][0])
    b2 = poly[3][1] - k2 * poly[3][0]

    res = []

    start = int((x_min // 16) * 16) # 原来代码是int((x_min // 16 + 1) * 16)
    end = x_max #int((x_max // 16) * 16)

    if (start + 16 - x_min) <= IGNORE_WIDTH:
        print("左面的框太小，忽略从往右的下一个位置开始：%d" % (start + 16 - x_min))
        start = start + 16
    else:
        print("左面的框合适，和16分割距离：%d" % (start + 16 - x_min) )

    # 之前的代码，用来切左面的的一小部分
    # p = x_min
    # # 第一个点，x是p
    # res.append([p,
    #             int(k1 * p + b1),
    #             start - 1,
    #             int(k1 * (p + 15) + b1),
    #             start - 1,
    #             int(k2 * (p + 15) + b2),
    #             p,
    #             int(k2 * p + b2)])

    for p in range(start, end + 1, r):
        # 2019.4.7 我给改成了收紧，让小框紧紧的包裹住大框的右侧边缘
        # 后来觉得自作聪明了，因为，这样会让右面出现一个特别窄的小框
        # 左面这样倒也罢了，毕竟是因为没办法，因为要和16像素对齐，must be aligned with 16pxs
        # 可右面，你还整这么窄，不是自我zuo么？！
        # 赶紧去掉
        # if (end-p) < 16:  <-----之前自作聪明的修改，打脸啊
        #     right = end
        # else:
        # 2019.5.10 再次修改，右面不是直接+16，而是看，如果我和end的距离2个像素内，那么这个GT框我就不算了
        #     right = p + 16
        right = p + 15
        if (end - p) <= IGNORE_WIDTH:
            print("右框宽度太小，右框不要：%d" % (end - p))
            continue
        else:
            print("右框宽度太小合适，保留：%d" % (end - p))

        # 左上，右上，右下，坐下 => [x1,y1,x2,y2,x3,y3,x4,y4]
        res.append([p,                      # 上方的x1
                    int(k1 * p + b1),       # 上方的y1

                    right,               # 上方的x2
                    int(k1 * (right) + b1),# 上方的y2

                    right,               # 下方的x3
                    int(k2 * (right) + b2),# 下方的y3

                    p,                      # 下方的x4
                    int(k2 * p + b2)])      # 下方的y4
    # 返回了一堆的16宽度的上下线截出的小4变形，注意，不是矩形噢！！！
    return np.array(res, dtype=np.int).reshape([-1, 8])

def do_one(p,img):

    _p("原始点:",p)

    # 画出来他
    cv2.polylines(img, [p], True, color=(255, 0 , 0),thickness=2)

    p = Polygon(p).convex_hull  # 返回最小凸包点
    _p("最小凸包点:",p)

    p = p.exterior
    _p("外环坐标exterior:",p)

    p = np.array(p.coords)
    _p("外环坐标coords:",p)

    p = p[:4]
    _p("只取前4个p[:4]",p)

    p = p[::-1]
    _p("[::-1]倒过来",p)

    idx = np.argsort(p[:, 0])
    _p("p[:,0]的argsort按照第1列(X)排序",idx)


    p = pickTopLeft(p)
    _p("pickTopLeft之后",p)

    res = shrink_poly(p)

    res = res.reshape([-1, 4, 2])
    for r in res:
        # 画出来他
        # print(r.shape)
        cv2.polylines(img, [r], True, color=(0, 255, 0), thickness=1)

        x_min = np.min(r[:, 0])
        y_min = np.min(r[:, 1])
        x_max = np.max(r[:, 0])
        y_max = np.max(r[:, 1])

        cv2.rectangle(img,
                      (x_min, y_min),
                      (x_max, y_max),
                      color=(0, 0, 255), # Red
                      thickness=1)



img = np.ones([600,600],dtype=np.uint8)
img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
img[:, :, 0] = 255
img[:, :, 1] = 255
img[:, :, 2] = 255

# 自己造一个诡异的四边形
p1 = np.array([[50,100], [250, 85], [235, 235], [75,290]])
p2 = np.array([[420,100], [500, 125], [585, 280], [270,350]])

do_one(p1,img)
do_one(p2,img)

cv2.imwrite('out.jpg', img)
