import neopixel

class OrderedNeoPixel(neopixel.NeoPixel):

    def __setitem__(self, key, value):
        i_pixel = self.mapping(key)
        super().__setitem__(i_pixel, value)

    def __getitem__(self, key):
        i_pixel = self.mapping(key)
        return super().__getitem__(i_pixel)

    def update_color(self, color):
        for i, pixel in enumerate(self):
            if pixel != [0, 0, 0]:
                self[i] = color

    @staticmethod
    def mapping(n):
        base = (5, 0, 6, 1, 7, 2, 8, 3, 9, 4)
        decenas = n // 10
        unidades = n % 10
        indice = base[unidades] + 10 * decenas
        return indice