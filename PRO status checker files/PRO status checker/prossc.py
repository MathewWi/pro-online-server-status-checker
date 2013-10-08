# copyright ASL97, prossc version 0.3.6
import urllib
import time, base64, os
import pspnet

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
    screen.swap()


  namelist = {}
  idname = open("idname","r").read().split("\n")

  for l in idname:
      gid = l.split(":",1)[0]
      nid = l.split(":",1)[1]
      namelist[gid] = nid

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
          time.sleep(2)
        if pad.circle:
          break
        if pad.right:
          if n != (len(itemlist) - 1):
            n += 1
            drawplayerdata(itemlist[n],datalist["game"][itemlist[n]],n+1,len(itemlist))
            time.sleep(0.5)
        if pad.left:
          if n != -1:
            n -= 1
            if n == -1:
              drawdata(datalist,n+1,len(itemlist))
              time.sleep(0.5)
            else:
              drawplayerdata(itemlist[n],datalist["game"][itemlist[n]],n+1,len(itemlist))
              time.sleep(0.5)