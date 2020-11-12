import sense_hat
import time 
import random

sense = sense_hat.SenseHat()

ROJO = [248, 0, 0]
VERDE = [0, 252, 0]
NEGRO = [0, 0, 0]
AMARILLO = [255, 255, 0]

colorJugador = AMARILLO
colorFondo = NEGRO
colorMuro = ROJO
colorFruta = VERDE

x = 3
y = 3
velX = 0
velY = 0

numMuros = 10
contTiempoFruta = 0
limiteTiempoFruta = 15
posXFruta = -1
posYFruta = -1
finPartida = False
velocidad = 0.5
aumentoVelocidad = 0.05

sense.clear()

for i in range(0, numMuros, 1):
  muroX = random.randint(0, 7)
  muroY = random.randint(0, 7)
  while(sense.get_pixel(muroX, muroY) == colorMuro or (muroX==3 and muroY==3)):
    muroX = random.randint(0, 7)
    muroY = random.randint(0, 7)
  sense.set_pixel(muroX, muroY, colorMuro)
  print (muroX, muroY)

while True:
  if(finPartida == False):
    # Se ha cumplido el tiempo de la fruta o aún no se ha colocado
    if(contTiempoFruta == 0):
      # Si estaba colocada la fruta, borrarla
      if(posXFruta != -1):
        sense.set_pixel(posXFruta, posYFruta, colorFondo)
      posXFruta = random.randint(0, 7)
      posYFruta = random.randint(0, 7)
      while(sense.get_pixel(posXFruta, posYFruta) != colorFondo):
        posXFruta = random.randint(0, 7)
        posYFruta = random.randint(0, 7)
      sense.set_pixel(posXFruta, posYFruta, colorFruta)
      print("Fruta colocada en "+ str(posXFruta) + ","+ str(posYFruta))
      contTiempoFruta = limiteTiempoFruta
      
    # Control del joystick
    for event in sense.stick.get_events():
      if event.action == "pressed":
        if event.direction == "up":
          velY = -1
          velX = 0
        elif event.direction == "down":
          velY = 1
          velX = 0
        elif event.direction == "left":
          velX = -1
          velY = 0
        elif event.direction == "right":
          velX = 1
          velY = 0
          
    # Preparar movimiento de la ficha
    sense.set_pixel(x, y, colorFondo)
    x += velX
    y += velY
    
    # Si la ficha está dentro de la pantalla
    if(x>=0 and x<=7 and y>=0 and y<=7):
      # Choque contra muro
      if(sense.get_pixel(x, y) == colorMuro):
        sense.clear(ROJO)
        finPartida = True
      # Se come la fruta
      elif(sense.get_pixel(x, y) == colorFruta):
        print("Fruta comida en: " + str(x) + "," + str(y))
        contTiempoFruta = 0
        #Aumento de velocidad
        velocidad -= aumentoVelocidad 
        print("Aumento de velocidad a: " + str(velocidad))
        # Animación de fruta comida
        for i in range(3):
          sense.set_pixel(x, y, colorJugador)
          time.sleep(0.1)
          sense.set_pixel(x, y, colorFruta)
          time.sleep(0.1)
      else: # MOVER LA FICHA
        sense.set_pixel(x, y, colorJugador)
    else: # Si se ha salido de la pantalla
      sense.clear(ROJO)
      finPartida = True
      
    # Esperar al siguiente movimiento de la ficha
    time.sleep(velocidad)
  else: # Fin de partida
    for event in sense.stick.get_events():
      # Reiniciar juego si se pulsa Middle
      if event.action == "pressed" and event.direction == "middle":
        finPartida = False
        sense.clear()
        x = 3
        y = 3
        velX = 0
        velY = 0
        for i in range(0, numMuros, 1):
          muroX = random.randint(0, 7)
          muroY = random.randint(0, 7)
          while(sense.get_pixel(muroX, muroY) == colorMuro or (muroX==3 and muroY==3)):
            muroX = random.randint(0, 7)
            muroY = random.randint(0, 7)
          sense.set_pixel(muroX, muroY, colorMuro)
          print (muroX, muroY)
        contTiempoFruta = 0