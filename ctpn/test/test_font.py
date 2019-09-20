from PIL import Image, ImageDraw, ImageFont, ImageFilter,ImageOps

import random
import numpy as np
import os,math
import logging as logger

X = 20
Y = 30
Y_OFFSET = 50

# 因为英文、数字、符号等ascii可见字符宽度短，所以要计算一下他的实际宽度，便于做样本的时候的宽度过宽
def box_shape(sentence,one_word_width):

    # 这个除2加4，是经验值，觉得英文字符是汉字的一半，然后再找补点
    half_word_width = int(one_word_width/2)# + 3

    width = 0
    for w in sentence:
        # 32~126 是 ascii的可见字符范围
        if ord(w)>=32 and ord(w)<=126:
            width+= half_word_width
        else:
            width+= one_word_width

    return width, one_word_width




# 得到一个随机大小的字体大小
def random_font_size():
    font_size = random.randint(15,25)
    return font_size

# 从目录中随机选择一种字体
def random_font(font_path="../data_generator/font/"):
    font_list = os.listdir(font_path)
    random_font = random.choice(font_list)

    return font_path + random_font


def draw_all(texts):
    # 生成一个文字图片
    img = Image.new('RGB', (800, 600), (255, 255, 255))  # 假设字是方的，宽+10，高+4个像素
    y = Y
    for text in texts:
        y += Y_OFFSET
        draw_text(text,img,y)

    img.save("out.jpg")

def draw_text(text,img,y_offset):
    draw = ImageDraw.Draw(img)

    # 随机选取字体大小、颜色、字体
    font_name = random_font()
    font_color = (0,0,0)
    font_size = random_font_size()
    print(font_name)
    font = ImageFont.truetype(font_name, font_size)

    width,height = box_shape(text,font_size)
    x1 = X
    y1 = y_offset
    x2 = x1+width
    y2 = y1+height

    draw.text((x1, y1), text , fill=font_color, font=font)  # TODO???
    # draw.rectangle((x1,y1,x2+4,y2), outline='red')

    #获得文字的offset位置
    offsetx, offsety = font.getoffset(text)
    #获得文件的大小
    width, height=font.getsize(text)
    draw.rectangle((offsetx+x1,offsety+y1,offsetx+x1+width,offsety+y1+height),
                   outline='red')


text = ["我abc",
        "我abc爱123北@#$",
        "我abc爱123北@#$京___天///",
        "我abc爱123北@#$京___天///门——，，。。！！！",
        "我abc爱123北@#$京___天///门——，，。。！！！爱123北@#$京爱123北@#$京",
        "1,1234,1123,003",
        "2018年12月13日 13:00:11",
        "我我我我我我我我我我我",
        "1111111111111111111"]
draw_all(text)

