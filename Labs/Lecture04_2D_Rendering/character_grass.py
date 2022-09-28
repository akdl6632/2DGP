from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

grass.draw_now(400,30)
character.draw_now(400,90)

x = 400
y = 90
r = 225
ck = False

while (1):
    while (not ck):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        
        if(x < 800 and y == 90):
            x = x + 2
            delay(0.01)
        elif(x == 800 and y < 600):
            y = y + 2
            delay(0.01)
        elif(y == 600 and x > 0):
            x = x - 2
            delay(0.01)
        else:
            y = y - 2
            delay(0.01)

        if(x == 400 and y == 90):
            ck = True

    while (ck):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)

        for theta in range(-90,270):
            x = 400 + r*math.cos(math.radians(theta))
            y = 315 + r*math.sin(math.radians(theta))
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            delay(0.01)

        x = 400
        y = 90
        ck = False

    
close_canvas()
