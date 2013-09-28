import os
import urllib
import pspnet

def run(font, screen, image, psp2d):
  def cb(s):
    if s >= 0:
      screen.clear(psp2d.Color(0,0,0))
      font.drawText(screen, 0, 0, 'State: %d/4' % s)
    else:
      screen.clear(psp2d.Color(0,0,0))
      font.drawText(screen, 0, 0, 'Connected')
    screen.swap()

  pspnet.connectToAPCTL(1, cb)
  font.drawText(screen, 350, 250, "Press X to continue")
  screen.swap()
  x = True
  while x == True:
      pad = psp2d.Controller()
      if pad.cross:
          x = False

  path = os.getcwd()
  data1 = urllib.urlopen("http://pro-online-server-status-checker.googlecode.com/git/PRO%20status%20checker%20files/PRO%20status%20checker/prossc.py").read()
  data3 = urllib.urlopen("http://pro-online-server-status-checker.googlecode.com/git/PRO%20status%20checker%20files/PRO%20status%20checker/wololo.py").read()
  screen.clear(psp2d.Color(0,0,0))
  f = open(path+"/prossc.py")
  data2 = f.read()
  f.close()
  f = open(path+"/wololo.py")
  data4 = f.read()
  f.close()
  if data1 != data2 and data3 != data4:
    font.drawText(screen, 0, 0, "updating prossc.py and wololo.py...")
    screen.swap()
    open(path+"/prossc.py","w").write(data1)
    open(path+"/wololo.py","w").write(data3)
    screen.clear(psp2d.Color(0,0,0))
    font.drawText(screen, 0, 0, "done updating prossc.py and wololo.py")
    screen.swap()
  elif data1 != data2:
    open(path+"/prossc.py","w").write(data1)
    screen.clear(psp2d.Color(0,0,0))
    font.drawText(screen, 0, 0, "done updating prossc.py")
    screen.swap()
  elif data3 != data4:
    open(path+"/wololo.py","w").write(data3)
    screen.clear(psp2d.Color(0,0,0))
    font.drawText(screen, 0, 0, "done updating wololo.py")
    screen.swap()
  else:
    font.drawText(screen, 0, 0, "prossc is already the latest version")
    screen.swap()

  font.drawText(screen, 272, 250, "Press Circle to exit the updater")
  screen.swap()
  x = True
  while x == True:
    pad = psp2d.Controller()
    if pad.circle:
      x = False

  pspnet.disconnectAPCTL()
