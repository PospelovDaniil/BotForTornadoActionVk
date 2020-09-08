# Время работы скриншота примерно 73мс
# Область где делать скрин (771, 385) до (834, 633)
# Область поиска зеленых пикселей (47,6) до (47,263)
# Область поиска белых пикселей   (26,4) до (26,262)
# Искомый зеленый пиксель         (7,254,0) мб ошибочно
# Искомый крайний зеленый пиксель (40,229,38) мб ошибочно
# Искомый белый пиксель           (255,252,254) мб ошибочно


import pyautogui as GodFood
import time
import random


lowerGreenCoord = [0,0]
coordArrow = [0,0]
lowerGreenCoord[0] = 47


def clickRoll():
    # GodFood.moveTo(850,790, duration=0.001)
    timeSleep = random.randint(1, 7)
    timeSleep = timeSleep/1000
    time.sleep(timeSleep)
    GodFood.click()

while(1):
    time.sleep(0.0005)
    img = GodFood.screenshot(region=(771,385, 63, 265))

    # img.save(r"C:\Users\z\Pictures\ex.png")


# Определение того, что на скриншоте зеленая шкала
    pixel_47_7 = img.getpixel((47,7))
    # pixel_17_7 = img.getpixel((17,7))

    # if(((((pixel_47_7[0]-5)>-15)or((pixel_47_7[0]-5)<15))and(((pixel_47_7[1]-255)>-15)or(pixel_47_7[1]-255)<15)) and ((((pixel_17_7[0]-5)>-15)or((pixel_17_7[0]-5)<15))and(((pixel_17_7[1]-255)>-15)or(pixel_17_7[1]-255)<15)))

    check_pixel_47_7 = (pixel_47_7[0]-7, pixel_47_7[1]-254, pixel_47_7[2])

    if(((check_pixel_47_7[0] > -10)and(check_pixel_47_7[0] < 10)) and ((check_pixel_47_7[1] > -10)and(check_pixel_47_7[1] < 10))): #and ((check_pixel_47_7[2] > -10)and(check_pixel_47_7[1]< 10))
        counterY=76

        for number in range(60):#МОЖНО УСКОРИТЬ ТУТ НАЧИНАЯ ПОИСК НЕ СНИЗУ ВВЕРХ, А СВЕРХУ ВНИЗ

            chekingPixel = img.getpixel((47,counterY - number))
            chekingPixel_hadle = (chekingPixel[0]-7, chekingPixel[1]-254, chekingPixel[2])
            if (((chekingPixel_hadle[0] > -15) and (chekingPixel_hadle[0] < 15)) and ((chekingPixel_hadle[1] > -15) and (chekingPixel_hadle[1] < 15)) ): #and ((chekingPixel_hadle[2] > -10) and (chekingPixel_hadle[1] < 10))
                lowerGreenCoord[1] = counterY - number
                break
        coordArrow[1] = lowerGreenCoord[1]

        chekingPixel = img.getpixel((10, coordArrow[1]))
        chekingPixel_2 = img.getpixel((12, coordArrow[1]))
        chekingPixel_hadle = (chekingPixel[0] - 255, chekingPixel[1] - 255, chekingPixel[2]-255)
        chekingPixel_hadle_2 = (chekingPixel_2[0] - 255, chekingPixel_2[1] - 255, chekingPixel_2[2] - 255)
        if (((chekingPixel_hadle[0] > -15) and (chekingPixel_hadle[0] < 15)) or ((chekingPixel_hadle_2[0] > -15) and (chekingPixel_hadle_2[0] < 15))):
            clickRoll()
