Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
t=turtle.Turtle
t.shape(turtle)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    t.shape(turtle)
  File "C:\python310\lib\turtle.py", line 2775, in shape
    return self.turtle.shapeIndex
AttributeError: module 'turtle' has no attribute 'turtle'. Did you mean: 'Turtle'?
t=turtle.Turtle()
t.shape(turtle)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    t.shape(turtle)
  File "C:\python310\lib\turtle.py", line 2777, in shape
    raise TurtleGraphicsError("There is no shape named %s" % name)
turtle.TurtleGraphicsError: There is no shape named <module 'turtle' from 'C:\\python310\\lib\\turtle.py'>
t.shape("turtle")
radius=50
t.up()
t.goto(0,0)
t.down()
t.circle(radius)
radius=50+20
t.up()
t.goto(10,0)
t.down
<bound method TPen.pendown of <turtle.Turtle object at 0x000001C940FBDF30>>
t.down()
t.circle(radius)
t.up()
t.goto(100,0)
t.down()
t.circle(radius)
