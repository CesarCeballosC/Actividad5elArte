"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

# Variables globales
writer = Turtle(visible=False) 
state_taps = {'taps': 0}
car = path('car.gif')
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdef")  # Letras del alfabeto
tiles = (alphabet[:32] * 2)  # Usar las primeras 16 letras, repetidas dos veces
state = {'mark': None}
hide = [True] * 64
revealed_count = 0
game_won = False

# Se mezclan las fichas
def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4): # Se dibuja un cuadrado
        forward(50)
        left(90)
    end_fill()

# Se convierten las coordenadas (x, y) a un índice de ficha
def index(x, y):
    """Convert (x, y) coordinates to tiles index.""" 
    return int((x + 200) // 50 + ((y + 200) // 50) * 8) 



def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


# Se actualizan las fichas y se cuentan los taps
def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    global revealed_count, game_won
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]: # Si las fichas no son iguales
        state['mark'] = spot
        state_taps['taps'] += 1
    else: # Si las fichas son iguales
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        state_taps['taps'] += 1 # Se cuenta cada tap
        revealed_count += 1 # Se cuenta cada ficha revelada
        if revealed_count == 32:
            game_won = True # Se gana el juego si se revelan todas las fichas
            print("¡¡¡Ganaste!!!")
        

    # Se actualiza el contador de taps
    writer.clear() 
    writer.up()
    writer.goto(205, 210)
    writer.down()
    writer.color('black')
    writer.write(state_taps['taps'], font=('Arial', 20, 'normal'))




# Se dibuja el tablero
def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64): # Se dibujan las fichas
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]: # Se revelan las fichas
        x, y = xy(mark)
        up()
        goto(x+25 , y+5) #AL modificar esta funcion desplazamos el numero en x ,y
        color('black')
        write(tiles[mark],align='center', font=('Arial', 30, 'normal')) #Mediante el metodo align lo centramos

    if game_won: # Se muestra el mensaje de ganador
        writer.up()
        writer.goto(-75, 75)
        writer.down()
        writer.color('black')
        writer.write('¡Ganaste!', font=('Arial', 40, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(510, 480, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
