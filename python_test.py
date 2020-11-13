import board
import time
import ordered_neopixel as neopixel


def main():
    pixel_pin = board.D18
    pixels = neopixel.OrderedNeoPixel(pixel_pin, 60)
    pixels[1] = (255, 0, 0)


    pixels.update_color((0, 255, 0))
    #pixels.fill((0,255,0))





if __name__ == '__main__':
    main()