import sense_hat
import time 
import random

sense = sense_hat.SenseHat()

x = 3
y = 3
velX = 0
velY = 0
colorJugador = [255, 255, 0]
colorFondo = [0, 0, 0]
colorMuro = [248, 0, 0] #255,0,0
colorFruta = [0, 252, 0]
numMuros = 10
contTiempoFruta = 0
limiteTiempoFruta = 15
posXFruta = -1;
posYFruta = -1;
finPartida = False

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
      print("Fruta en "+ str(posXFruta) + ","+ str(posYFruta))
      contTiempoFruta = limiteTiempoFruta
      
    if(velX != 0 or velY != 0):
      contTiempoFruta = contTiempoFruta - 1
  
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
    sense.set_pixel(x, y, colorFondo)
    x = x + velX
    y = y + velY
    if(x<0 or x>7 or y<0 or y>7):
      sense.clear((255, 0, 0))
      finPartida = True
    else:
      if(sense.get_pixel(x, y) == colorMuro):
        sense.clear((255, 0, 0))
        finPartida = True
      elif(sense.get_pixel(x, y) == colorFruta):
        contTiempoFruta = 0
      sense.set_pixel(x, y, colorJugador)
  
    time.sleep(0.5)
  else:
    for event in sense.stick.get_events():
      if event.action == "pressed":
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