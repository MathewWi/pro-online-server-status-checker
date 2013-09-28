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

modr = {}
if os.path.exists(path+"/prossc.py"):
  import prossc as main
  modr["prossc"] = True
  if any(l == False for l in [font,icon,anon,gameid]):
    main.make(path, font, icon, anon, gameid)
else:
  modr["prossc"] = False

if os.path.exists(path+"/update.py"):
  import update
  modr["update"] = True
else:
  modr["update"] = False

if os.path.exists(path+"/wololo.py"):
  import wololo
  modr["wololo"] = True
else:
  modr["wololo"] = False

font = psp2d.Font("font.png")
screen = psp2d.Screen()
image = psp2d.Image(480, 272)

def start_menu(t, modt):
  screen.clear(psp2d.Color(0,0,0))
  l = 0
  for a in modt:
    if a == "prossc":
      font.drawText(screen, 0, l, "start PROSSC <--" if t == modt.index("prossc") else "start PROSSC")
      l += 20
    if a == "update":
      font.drawText(screen, 0, l, "check for update <--" if t == modt.index("update") else "check for update")
      l += 20
    if a == "wololo":
      font.drawText(screen, 0, l, "start wololo's rss reader <--" if t == modt.index("wololo") else "start wololo's rss reader")
      l += 20
  font.drawText(screen, 350, 190, "Press Circle to exit")
  font.drawText(screen, 350, 210, "Press X to continue")
  font.drawText(screen, 340, 230, "Press up to select up")
  font.drawText(screen, 303, 250, "Press down to select down")
  screen.swap()

modt = sorted([t for (t,l) in modr.items() if l == True])
t = 0
q = len(modt)-1
start_menu(t, modt)
while True:
  pad = psp2d.Controller()
  if pad.up:
    if t != 0:
      t-=1
      start_menu(t, modt)
      time.sleep(0.5)
  if pad.down:
    if t != q:
      t+=1
      start_menu(t, modt)
      time.sleep(0.5)
  if pad.cross:
    if t == modt.index("prossc"):
      screen.clear(psp2d.Color(0,0,0))
      main.run(font, screen, image, psp2d)
    if t == modt.index("update"):
      screen.clear(psp2d.Color(0,0,0))
      p,w = update.run(font, screen, image, psp2d)
      if p:
        reload(p)
      if w:
        reload(w)
    if t == modt.index("wololo"):
      screen.clear(psp2d.Color(0,0,0))
      wololo.run(font, screen, image, psp2d)
    start_menu(t, modt)
    time.sleep(0.5)
  if pad.circle:
    break
