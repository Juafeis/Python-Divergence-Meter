import board
import time
import datetime
import ordered_neopixel as neopixel
import asyncio


async def main():
    pixel_pin = board.D18
    nixie_color = (255, 20, 0)
    pixels = neopixel.OrderedNeoPixel(pixel_pin, 60)
    # pixels.fill((0,0,0))
    # await asyncio.sleep(10)
    _time =  getTime()
    while(True):
        _actualTime =  getTime()

        if _actualTime != _time:
            print(_time) 
            _time =  getTime()   
            await pixels.update_time(_time, nixie_color)

    #pixels.update_color(nixie_color)


def getTime():
    return datetime.datetime.now().strftime("%H%M%S")

if __name__ == '__main__':
    asyncio.run(main())