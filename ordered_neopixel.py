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

    def update_time(self, time, color):
        self.fill((0,0,0))
        if len(time) != 6:
            raise Exception("Time must be composed by 6 numbers")
        
        i = 0
        for number in time:
            self[int(number) + i] = color
            i += 10




    @staticmethod
    def mapping(n):
        base = (5, 0, 6, 1, 7, 2, 8, 3, 9, 4)
        decenas = n // 10
        unidades = n % 10
        indice = base[unidades] + 10 * decenas
        return indice