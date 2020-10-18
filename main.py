from graphics import *
def moveAll(object,dx,dy):
  object.move(dx,dy)
def userMove():
    win = GraphWin()
    c = Circle(Point(100,100),20)
    c.draw(win)
    while True:
      key = win.checkKey()
      if key == "w":
        moveAll(c, 0, -20)
      elif key=="d":
        moveAll(c,20,0)
      elif key=="a":
        moveAll(c,-20,0)
      elif key=="s":
        moveAll(c,0,20)
userMove()