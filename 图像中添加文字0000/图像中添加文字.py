from PIL import Image, ImageDraw, ImageFont

def add_text(img, str):
    im = Image.open(img)
    tfont = ImageFont.truetype("C:\\WINDOWS\\Fonts\\SIMYOU.TTF",500)
    draw = ImageDraw.Draw(im)
    #　设置 文字位置 文字内容 颜色 文字大小
    draw.text((1000,1000), str, fill=(0,0,0), font=tfont)
    im.save('E:\\WNCG\\day day up\\target.jpg')

if __name__ == '__main__':
   add_text('E:\\WNCG\\day day up\\0000.JPG', 'you are so good\n图像处理')