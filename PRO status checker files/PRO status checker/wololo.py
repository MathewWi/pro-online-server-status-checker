import urllib
import time, textwrap
import HP as HTMLParser
import pspnet

def run(font, screen, image, psp2d):
  def getxmldata():
    t = urllib.urlopen("http://wololo.net/feed/").read()
    html = t.decode("utf-8").encode("utf-8").decode("ascii","ignore")
    return html

  def psplistmake(data):
    datalist = []
    rawlist = data.split("\n")
    t = []
    for l in rawlist:
      if l.startswith("\t\t<title"):
        data = l[9:-8]
        data = HTMLParser.HTMLParser().unescape(data).encode("ascii","ignore")
        t.append(data)
      elif l.startswith("\t\t<description"):
        data = l[24:-17]
        data = HTMLParser.HTMLParser().unescape(data).encode("ascii","ignore")
        t.append(data)
      if len(t) == 2:
        datalist.append((t[0],t[1]))
        t = []
    return datalist

  def getdata():
    try:
      bdata = getxmldata()
      global connected
      connected = True
      return bdata
    except:
      x = True
      times = 1
      while x == True:
        screen.clear(psp2d.Color(0,0,0))
        font.drawText(screen, 0, 0, "fail to connect (%s), retry?" % times)
        font.drawText(screen, 350, 230, "Press X to retry")
        font.drawText(screen, 350, 250, "Press Circle to exit")
        times += 1
        screen.swap()
        while True:
          pad = psp2d.Controller()
          if pad.cross:
            try:
              bdata = getxmldata()
              time.sleep(2)
              x = False
              connected = True
              return bdata
            except:
              break
          if pad.circle:
            return

  def drawdata(data):
    image.clear(psp2d.Color(0,0,0))
    screen.blit(image)
    screen.swap()
    t = 0
    textlist = textwrap.wrap(data[0],70)
    for l in textlist:
      font.drawText(image, 0, t, l)
      t += 20

    t += 20
    textlist = textwrap.wrap(data[1],70) 
    for l in textlist:
      font.drawText(image, 0, t, l)
      t += 20
    font.drawText(image, 0, 250, time.strftime("%H:%M:%S", time.localtime()))
    font.drawText(image, 350, 210, "Press Circle to exit")
    font.drawText(image, 305, 230, "Press Right for older post")
    font.drawText(image, 305, 250, "Press Left for newer post")
    screen.blit(image)
    screen.swap()

  def cb(s):
    if s >= 0:
      screen.clear(psp2d.Color(0,0,0))
      font.drawText(screen, 0, 0, 'State: %d/4' % s)
    else:
      screen.clear(psp2d.Color(0,0,0))
      font.drawText(screen, 0, 0, 'Connected')
      font.drawText(screen, 350, 250, "Press X to continue")
    screen.swap()

  if pspnet.getAPCTLState() != 4:
    pspnet.connectToAPCTL(1, cb)
    x = True
    while x == True:
      pad = psp2d.Controller()
      if pad.cross:
          x = False

  screen.clear(psp2d.Color(0,0,0))
  font.drawText(screen, 0, 0, 'Loading...')
  screen.swap()

  global connected
  connected = False

  bdata = getdata()
  data = bdata.encode("ascii","ignore")
  datalist = psplistmake(data)
  if connected == True:
    screen.clear(psp2d.Color(0,0,0))
    n = 0
    drawdata(datalist[n])   
    x = True
    while x == True:
      pad = psp2d.Controller()
      if pad.right:
        if n != 14:
          n += 1
          print(n)
          drawdata(datalist[n])
          time.sleep(0.5)
      if pad.left:
        if n != 0:
          n -= 1
          drawdata(datalist[n])
          time.sleep(0.5)
      if pad.triangle:
        bdata = getdata()
        drawdata(bdata)
        time.sleep(0.5)
      if pad.circle:
        x = False
