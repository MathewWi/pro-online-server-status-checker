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
    open(path+"/prossc.py","w").write(data1)
    open(path+"/wololo.py","w").write(data3)
    font.drawText(screen, 0, 0, "done updating prossc.py and wololo.py")
  elif data1 != data2:
    open(path+"/prossc.py","w").write(data1)
    font.drawText(screen, 0, 0, "done updating prossc.py")
  elif data3 != data4:
    open(path+"/wololo.py","w").write(data3)
    font.drawText(screen, 0, 0, "done updating wololo.py")
  else:
    font.drawText(screen, 0, 0, "prossc and wololo(add-on) is already the latest version")


  font.drawText(screen, 272, 250, "Press Circle to exit the updater")
  screen.swap()
  x = True
  while x == True:
    pad = psp2d.Controller()
    if pad.circle:
      x = False
