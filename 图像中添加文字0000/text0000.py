from PIL import Image, ImageDraw, ImageFont

im=Image.open("E:\\WNCG\\day day up\\0000.JPG")
draw=ImageDraw.Draw(im)
newfont=ImageFont.truetype("C:\\WINDOWS\\Fonts\\SIMYOU.TTF", 100)
draw.text((1000,1000),u'you are so good!',fill="red",font=newfont)
im.show()
im.save('E:\\WNCG\\day day up\\target.jpg')