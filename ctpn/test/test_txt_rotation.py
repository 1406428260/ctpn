from PIL import Image
from PIL import ImageFont, ImageDraw, ImageOps
import math

# 因为英文、数字、符号等ascii可见字符宽度短，所以要计算一下他的实际宽度，便于做样本的时候的宽度过宽
def caculate_text_shape(text,font):

    offsetx, offsety = font.getoffset(text)

    #获得文件的大小
    width, height=font.getsize(text)

    width = width - offsetx
    height = height - offsety

    print(height)
    return width,height

'''
(x,y)为要转的点，（pointx,pointy)为中心点，如果顺时针角度为angle

srx = (x-pointx)*cos(angle) + (y-pointy)*sin(angle)+pointx

sry = (y-pointy)*cos(angle) - (x-pointx)*sin(angle)+pointy
'''
def _rotate_one_point(xy, center, theta):
    # https://en.wikipedia.org/wiki/Rotation_matrix#In_two_dimensions
    cos_theta, sin_theta = math.cos(theta), math.sin(theta)

    cord = (
        # (xy[0] - center[0]) * cos_theta - (xy[1]-center[1]) * sin_theta + xy[0],
        # (xy[0] - center[0]) * sin_theta + (xy[1]-center[1]) * cos_theta + xy[1]
        (xy[0] - center[0]) * cos_theta - (xy[1]-center[1]) * sin_theta + center[0],
        (xy[0] - center[0]) * sin_theta + (xy[1]-center[1]) * cos_theta + center[1]

    )
    print("旋转后的坐标：")
    print(cord)
    return cord


def _rotate_points(points, center,degree):
    theta = math.radians(-degree)

    rotated_points = [_rotate_one_point(xy, center ,theta) for xy in points]

    return rotated_points


im=Image.open("bg.png")
f = ImageFont.truetype('simhei.ttf',30)

text="我爱北京天安门！~"

w,h = caculate_text_shape(text,f)

txt_img=Image.new('L', (400,100))
d = ImageDraw.Draw(txt_img)
d.text( (0,0), text,  font=f, fill=200)
center = (w//2,h//2)

degree = 10

t_img = txt_img.rotate(degree,center =center,expand=1)
d = ImageDraw.Draw(t_img)
d.text( (0,0), text,  font=f, fill=200)
d = ImageDraw.Draw(im)

x = 20
y = 20

im.paste(t_img,(x,y),mask=t_img)

p= [(x,y),
    (x+w,y),
    (x+w,y+h),
    (x,y+h)]
print(p)
d.polygon(p,outline=(150))
p = _rotate_points(p,
                   (x+center[0], y+center[1]),
                   degree)
d.polygon(p,outline=(105))

w =  im.size[0]
h  = im.size[1]
im = im.crop((0, 0, 800, 800)) # 测试一下剪裁
im.save("out.png")