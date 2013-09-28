import os
import time
import psp2d

path = os.getcwd()

if os.path.exists(path+"/font.png"):
  font = True
else:
  font = False

if os.path.exists(path+"/prossc.png"):
  icon = True
else:
  icon = False

if os.path.exists(path+"/anon.txt"):
  anon = True
else:
  anon = False


if os.path.exists(path+"/idname"):
  gameid = True
else:
  gameid = False

if os.path.exists(path+"/wololo.py"):
  import wololo
  mwololo = True
else:
  mwololo = False

if os.path.exists(path+"/prossc.py"):
  import prossc as main
  mprossc = True
else:
  mprossc = False

if os.path.exists(path+"/update.py"):
  import update
  mupdate = True
else:
  mupdate = False

if any(l == False for l in [font,icon,anon,gameid]):
  main.make(path, font, icon, anon, gameid)


font = psp2d.Font("font.png")
screen = psp2d.Screen()
image = psp2d.Image(480, 272)

def start_menu(t, mupdate, mwololo):
  screen.clear(psp2d.Color(0,0,0))
  l = 0
  font.drawText(screen, 0, l,  "start PROSSC <--" if t == 3 else "start PROSSC")
  l += 20
  if mupdate:
    font.drawText(screen, 0, l, "check for update <--" if t == 2 else "check for update")
    l += 20
  if mwololo:
    font.drawText(screen, 0, l, "start wololo's rss reader <--" if t == 1 else "start wololo's rss reader")
    #l += 20
  font.drawText(screen, 350, 190, "Press Circle to exit")
  font.drawText(screen, 350, 210, "Press X to continue")
  font.drawText(screen, 340, 230, "Press up to select up")
  font.drawText(screen, 303, 250, "Press down to select down")
  screen.swap()

t = 3
start_menu(t, mupdate, mwololo)
while True:
  pad = psp2d.Controller()
  if pad.up:
    if t != 3:
      t+=1
      start_menu(t, mupdate, mwololo)
      time.sleep(0.5)
  if pad.down:
    if t != 1:
      t-=1
      start_menu(t, mupdate, mwololo)
      time.sleep(0.5)
  if pad.cross:
    if t == 3:
      screen.clear(psp2d.Color(0,0,0))
      main.run(font, screen, image, psp2d)
    if t == 2:
      screen.clear(psp2d.Color(0,0,0))
      update.run(font, screen, image, psp2d)
    if t == 1:
      screen.clear(psp2d.Color(0,0,0))
      wololo.run(font, screen, image, psp2d)
    start_menu(t, mupdate, mwololo)
    time.sleep(0.5)
  if pad.circle:
    break
