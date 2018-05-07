###生成验证码
###实际上是向生成的图片上写数字
###1.每个验证码的字颜色不同
###2.随机生成字符
###3.使用画笔的draw方法将文字画到图片上
import random
from PIL import ImageDraw, Image, ImageFont
"""
1.创建一个image对象
"""
img=Image.new(mode="RGB",size=(120,30),color=(255,255,255))
"""
2.创建一个画笔对象
必须提供一个画笔对象
"""
paint=ImageDraw.Draw(img,mode="RGB")

"""
4.chr将生成的16进制转换成字符串
随机生成5个字符，每次向image上绘制一个，每个字符的颜色也是随机的
字符绘制的位置每次向后移动一些距离
"""
for i in range(5):
 text=random.choice([chr(random.randint(65,90)),str(random.randint(0,9))])
 print(chr(random.randint(65,90))+str(random.randint(0,9)))
 print(text)
 color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
 paint.text([i*24, 0], text, color)
"""
将字体画到图片上
起始位置,起始文职，颜色
"""

img.show()