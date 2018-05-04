"""
给图片添加角标
1.使用PIL库，ImageDraw，ImageFront，Image三个库
"""
from PIL import Image, ImageDraw, ImageFont


def cornImage():
    text = '1'
    width = 128
    height = 128
    image_path = '/Users/apple/Desktop/15684156.jpeg'
    ###1.打开图片
    image = Image.open(image_path)
    ###2.压缩图片
    image.thumbnail((width, height))
    ###3.绘制一个椭圆
    imageDraw = ImageDraw.Draw(image)
    imageDraw.chord(((width / 3 * 2 + 1, 0, width - 1, (width / 3))), 0, 360, (255, 0, 0))
    """
    创建字体
    """
    # imageFont = ImageFont.truetype('consola.ttf', 30, encoding='unic')
    # imageDraw.text(((width * 0.75), (width * 0.06)), text, font=imageFont)
    imageDraw.text(((width * 0.75), (width * 0.06)), text)
    image.show()
    ###5.保存图片
    image.save(image_path + '.draw', 'JPEG')
    del image


cornImage()
