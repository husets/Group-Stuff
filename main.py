from graphics import *
def levels(c):
  if c== (4,10):
    level1()
  elif c== (4,18):
    level2()
  elif c== (4,26):
    level3()
def level1():
  print("Level 1")
def level2():
  pass
def level3():
  pass
def moveAll(object,dx,dy):
  object.move(dx,dy)
def userMove():
  win=GraphWin()
  win.setCoords(0,0,50,50)
  c = Circle(Point(2,2),2)
  c.draw(win)
  while True:
    key = win.checkKey()
    if key == "w":
      moveAll(c, 0, 2)
    elif key=="d":
      moveAll(c,2,0)
    elif key=="a":
      moveAll(c,-2,0)
    elif key=="s":
      moveAll(c,0,-2)
    levels(c)
userMove()
