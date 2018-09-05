from PIL import Image
import argparse

#命令行输入参数处理
parser = argparse.ArgumentParser()

parser.add_argument('file')     #处理的文件名
parser.add_argument('-o', '--output')   #定义输出文件命令
parser.add_argument('--width', type = int, default = 80) #输出字符画宽
parser.add_argument('--height', type = int, default = 80) #输出字符画高
args = parser.parse_args()
#获取输入的命令行参数

IMG = args.file
OUTPUT = args.output
HEIGHT = args.height
WIDTH = args.width

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
#设定想要使用的字符串集


def get_char(r, g, b, alpha = 256):
    # 将灰度值映射到设定的字符串集上 PS：如果这里的字符换成图片文件，就能做出网上很多流传的表情包的效果~
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)    #RGB值转化为灰度值

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]


if __name__ == '__main__':
    im = Image.open(IMG)    #打开图像文件
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)   #使用resize将图片大小变为要求的参数
    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))    #使用getpixel（）获得rgb进而将其用字符来代替
        txt += '\n'    #很重要！每行转化之后记得要换行

    print(txt)

    #字符画输出到文件
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else: #默认输出到output2.txt中
        with open("output2.txt",'w') as f:
            f.write(txt)