# copyright ASL97, menu version 0.1.4
import os
import time
import psp2d, pspnet
def make(path, font, icon, anon, gameid):
  if font == False:
    data = base64.b64decode("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")
    open(path+"/font.png","wb").write(data)

  if icon == False:
    data = base64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAJAAAABQAQMAAADMYG5PAAAABlBMVEX///8AAABVwtN+AAAAAWJLR0QAiAUdSAAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB90JAxIIJw+gILMAAAJNSURBVDjLrdQxb9NAFADgSyORoVIsxNIhikECCaSKJUNAinRDByQWhv4AInWomKjUKZLVsxpmzAIj/hnA0rgNogOoFmKgUx0RFQ8gJeEEsfH5Hncpsc9nRiIrtj+9OO/e8z0EpQ/639Qvk12mO7hE+FqZbCJPB8lEHIMFtVcMeepQXxx4Qch3NOKbgaM9ixM30IgBfumq9FMkhRo1lUYGcLS7odK+CbAVzlRyXeC9IFHJEXexH6vUj0xI/cIPp3s14D6FzzkxawtgOOR2TqQDE5EJQzk1LXAk9XJCPTAgJZGIXdK3mK/KhWKPZMueRR/EArjxLCcan1Vl59wko2R81hVX1PQymo/EnwJN0AhnJXzSYABRrfLezMhtJAmwOvnbgUXOr+l40YGPOb0ZhyKxNv6U090w9ICh9Ss5JaGPSLSCWklO/slNArwiH7l8C4/qRNBuctTOyGuKLPmMnlQympiytSltbuav7+BQ1mfegQc5LTo0tW5XM0oZRGKdURWRJbFH8JaIYg6sLIpXoL4NdMZZFgUDvrctisYgJ1GI4wlMLzNlDzHwfRihq0UK4HynqlAKzulD+G0oxG/trxmiJipVUesxgErwar0lvkOVOO4ORFMLRLqGo+1t6wvUNGJ+REmRouPkKy5SbN/7pUWBXeOWRs99NtWnyYT1zyVd7PsDSeNTw5YlvNjkHUmjNfJCo3gHm0NtMv3Aq55G1EWeWaT50xuBRvCOlOg74EAjdgnrURG6jjWK7yOiT0y+URqifFYmWh61aZnYvwbyHwEY8T4U0+kXAAAAAElFTkSuQmCC")
    open(path+"/prossc.png","wb").write(data)

  if anon == False:
    open(path+"/anon.txt","w").write("prinny")

  if gameid == False:
    idname = ["ULES01580:Pro Evolution Soccer 2013","UCES00855:SOCOM: U.S. Navy SEALs Tactical Strike","UCES01250:Motorstorm Artic Edge","NPJH90338:God Eater 2 Demo","ULES01355:F1 2009","NPJH50443:Final Fantasy Type-0","ULJM06161:World Soccer Winning Eleven 2013"]
    open(path+"/idname","w").write("\n".join(idname))

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

if any(l == False for l in [font,icon,anon,gameid]):
  make(path, font, icon, anon, gameid)

modr = {}
if os.path.exists(path+"/prossc.py"):
  import prossc as main
  modr["prossc"] = True
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

def cb(s):
  if s >= 0:
    screen.clear(psp2d.Color(0,0,0))
    font.drawText(screen, 0, 0, 'State: %d/4' % s)
  else:
    screen.clear(psp2d.Color(0,0,0))
    font.drawText(screen, 0, 0, 'Connected')
    image = psp2d.Image("prossc.png")  
    screen.blit(image, dx=120, dy=102, dw=242, blend=True)
    font.drawText(screen, 350, 250, "Press X to continue")
    image = psp2d.Image(480, 272)
    image.clear(psp2d.Color(0,0,0))
  screen.swap()

pspnet.connectToAPCTL(1, cb)
x = True
while x == True:
  pad = psp2d.Controller()
  if pad.cross:
    x = False
    time.sleep(0.5)

screen.clear(psp2d.Color(0,0,0))
font.drawText(screen, 0, 0, 'Loading...')
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
      time.sleep(0.3)
  if pad.down:
    if t != q:
      t+=1
      start_menu(t, modt)
      time.sleep(0.3)
  if pad.cross:
    screen.clear(psp2d.Color(0,0,0))
    font.drawText(screen, 0, 0, 'Loading...')
    screen.swap()
    if "prossc" in modt:
      if t == modt.index("prossc"):
        screen.clear(psp2d.Color(0,0,0))
        main.run(font, screen, image, psp2d)
    if "update" in modt:
      if t == modt.index("update"):
        screen.clear(psp2d.Color(0,0,0))
        p,w = update.run(font, screen, image, psp2d)
        if p and modr["prossc"] == True:
          reload(main)
        elif p:
          import prossc as main
          modr["prossc"] = True
          modt = sorted([t for (t,l) in modr.items() if l == True])
          t = 0
          q = len(modt)-1
          start_menu(t, modt)
        if w and modr["wololo"] == True:
          reload(wololo)
        elif w:
          import wololo
          modr["wololo"] = True
          modt = sorted([t for (t,l) in modr.items() if l == True])
          t = 0
          q = len(modt)-1
          start_menu(t, modt)
    if "wololo" in modt:
      if t == modt.index("wololo"):
        screen.clear(psp2d.Color(0,0,0))
        wololo.run(font, screen, image, psp2d)
      start_menu(t, modt)
      time.sleep(0.3)
  if pad.circle:
    break
