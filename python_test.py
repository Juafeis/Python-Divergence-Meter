import board
import time
import datetime
import ordered_neopixel as neopixel


def main():
    pixel_pin = board.D18
    nixie_color = (255, 20, 0)
    pixels = neopixel.OrderedNeoPixel(pixel_pin, 60)
    #pixels[3] = nixie_color
    while(True):
        _time = datetime.datetime.now().strftime("%H%M%S")
        pixels.update_time(_time, nixie_color)
        time.sleep(1)


    #pixels.update_color(nixie_color)


if __name__ == '__main__':
    main()