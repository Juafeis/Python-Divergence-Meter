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

    async def update_time(self, time, color):
        if len(time) != 6:
            raise Exception("Time must be composed by 6 numbers")
        
        hours = time[:2]
        minutes = time[2:4]
        seconds = time[4:]
    
        digit = 0
        for i, number in enumerate(time):
            pos = int(number) + digit

            if (int(number) == 0) :
                if digit == 50 or digit == 30 or digit == 10 :
                    self[pos + 9] = (0, 0, 0)
                elif digit == 40 or digit == 20 :
                    self[pos + 5] = (0, 0, 0)      

            if hours == "00" and minutes == "00" and seconds == "00":
                self[2] = (0, 0, 0)     
                self[13] = (0,0,0)
        
            self[pos - 1] = (0, 0, 0)
            self[pos] = color
            digit += 10




    @staticmethod
    def mapping(n):
        base = (5, 0, 6, 1, 7, 2, 8, 3, 9, 4)
        decenas = n // 10
        unidades = n % 10
        indice = base[unidades] + 10 * decenas
        return indice