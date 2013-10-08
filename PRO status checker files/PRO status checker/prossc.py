# copyright ASL97, prossc version 0.3.9
import urllib
import time, os
import pspnet

def run(font, screen, image, psp2d):
  anonname = open("anon.txt","r").read()


  def getxmldata():
    t = urllib.urlopen("http://pro.coldbird.uk.to/status/").read()
    html = t.decode("utf-8")
    return html

  def psplistmake(data):
    datalist = {}
    datalist["name"] = "prometheus online status"
    datalist["game"] = {}
    rawlist = data.split("\n")
    for l in rawlist:
      if l.startswith("<prometheus"):
        num = l.split("\"")[1]
        datalist["players"] = num
      elif l.startswith("\t<game"):
        name = l.split("\"")[1]
        num = l.split("\"")[3]
        try:
          name = namelist[name]
        except:
          pass
        datalist["game"][name] = {}
        datalist["game"][name]["players"] = num
      if l.startswith("\t\t<group"):
        group = l.split("\"")[1]
        num = l.split("\"")[3]
        if not "group" in datalist["game"][name]:
          datalist["game"][name]["group"] = {}
        if group in datalist["game"][name]["group"]:
          datalist["game"][name]["group"][group]["players"] = num
        else:
          datalist["game"][name]["group"][group] = {}
          datalist["game"][name]["group"][group]["players"]  = num
      if l.startswith("\t\t\t<user"):
        username = l[9:-7]
        if "name" in datalist["game"][name]["group"][group]:
          datalist["game"][name]["group"][group]["name"] = datalist["game"][name]["group"][group]["name"]+[username]
        else:
          datalist["game"][name]["group"][group]["name"] = [username]
    return datalist

  def makedatalist(bdata):
    data = bdata.encode("ascii","ignore")
    datalist = psplistmake(data)
    itemlist = datalist["game"].keys()
    return (datalist, itemlist)

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


  def drawdata(datalist, n,m):
    image.clear(psp2d.Color(0,0,0))
    screen.blit(image)
    screen.swap()
    font.drawText(image, 0, 0, datalist["name"]+", total player(s) : "+datalist["players"])
    t = 20
    for l in datalist["game"]:
      if len(datalist["game"][l]["players"]) > 1:
        font.drawText(image, 0, t, l+" : "+datalist["game"][l]["players"]+" players")
      else:
        font.drawText(image, 0, t, l+" : "+datalist["game"][l]["players"]+" player")
      t += 20

    font.drawText(image, 420, 0, time.strftime("%H:%M:%S", time.localtime()))
    font.drawText(image, 440, 170, "%d/%d" % (n,m))
    font.drawText(image, 350, 190, "Press Circle to exit")
    font.drawText(image, 310, 210, "Press Triangle to update")
    font.drawText(image, 300, 230, "Press Right for Next Game")
    font.drawText(image, 285, 250, "Press Left for Previous Game")
    screen.blit(image)
    screen.swap()


  def drawplayerdata(name,playerlist,n,m):
    image.clear(psp2d.Color(0,0,0))
    screen.blit(image)
    screen.swap()
    font.drawText(image, 0, 0, name+", total player(s): "+playerlist["players"])
    t = 30
    groupnames = playerlist["group"].keys()
    for l in groupnames:
      if len(playerlist["group"][l]["players"]) > 1:
        font.drawText(image, 0, t, l+" : "+playerlist["group"][l]["players"]+" players")
      else:
        font.drawText(image, 0, t, l+" : "+playerlist["group"][l]["players"]+" player")
      t += 20
      if "name" in playerlist["group"][l]:
        newlist = []
        for l in playerlist["group"][l]["name"]:
          if l.replace(" ","") == "":
            newlist.append(anonname)
          else:
            newlist.append(l)
        font.drawText(image, 0, t, ", ".join(newlist))
        t += 20

    font.drawText(image, 420, 0, time.strftime("%H:%M:%S", time.localtime()))
    font.drawText(image, 440, 170, "%d/%d" % (n,m))
    font.drawText(image, 350, 190, "Press Circle to exit")
    font.drawText(image, 310, 210, "Press Triangle to update")
    font.drawText(image, 300, 230, "Press Right for Next Game")
    font.drawText(image, 285, 250, "Press Left for Previous Game")
    screen.blit(image)
    screen.swap()

  namelist = {}
  idname = open("idname","r").read().split("\n")

  for l in idname:
      gid = l.split(":",1)[0]
      nid = l.split(":",1)[1]
      namelist[gid] = nid

  global connected
  connected = False
  global datalist
  datalist = {}
  global itemlist
  itemlist = []

  bdata = getdata()
  if connected == True:
    screen.clear(psp2d.Color(0,0,0))
    datalist, itemlist = makedatalist(bdata)
    n = -1
    drawdata(datalist,n+1,len(itemlist))
    while True:
        pad = psp2d.Controller()
        if pad.triangle:
          bdata = getdata()
          datalist, itemlist = makedatalist(bdata)
          if n == -1:
            drawdata(datalist,n+1,len(itemlist))
          else:
            drawplayerdata(itemlist[n],datalist["game"][itemlist[n]],n+1,len(itemlist))
          time.sleep(1)
        if pad.circle:
          break
        if pad.right:
          if n != (len(itemlist) - 1):
            n += 1
            drawplayerdata(itemlist[n],datalist["game"][itemlist[n]],n+1,len(itemlist))
            time.sleep(0.3)
        if pad.left:
          if n != -1:
            n -= 1
            if n == -1:
              drawdata(datalist,n+1,len(itemlist))
              time.sleep(0.3)
            else:
              drawplayerdata(itemlist[n],datalist["game"][itemlist[n]],n+1,len(itemlist))
              time.sleep(0.3)