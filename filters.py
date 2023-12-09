from PIL import Image, ImageFilter
class Filter:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class InversionFilter(Filter):
    def __init__(self):
        super().__init__("InvertionFilter", "Инвертирует цвет каждого пикселя по формуле (r, g, b) -> (255 - r, 255 - g, 255 - b)")

    def transform(self, img):
        n, m = img.size
        for i in range(n):
            for j in range(m):
                r, g, b = img.getpixel((i, j))
                r = 255 - r
                g = 255 - g
                b = 255 - b
                img.putpixel((i, j), (r, g, b))
        return img


class MirrorFilter(Filter):
    def __init__(self):
        super().__init__("MirrorFilter", "разворачиват изображение заркально")

    def transform(self, img):
        return img.transpose(Image.FLIP_LEFT_RIGHT)
        # for y in range(img.height):
        #     for x in range(img.width):
        #         pr, pg, pb = img.getpixel((img.width - x - 1, y))
        #         r, g, b = img.getpixel((x, y))
        #         img.putpixel((img.width - x - 1, y), (r, g, b))
        #         img.putpixel((x, y), (pr, pg, pb))
        # return img


class BlurFilter(Filter):
    def __init__(self):
        super().__init__("BlurFilter", "чуть-чуть блюрит изображение")

    def transform(self, img):
        return img.filter(ImageFilter.BLUR)

