#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle
turtle.setup(800,500,200,100)
turtle.penup()
turtle.fd(-300)
# turtle.color("red")
turtle.pendown()
turtle.pensize(20)
turtle.seth(-40)
color_list=('red','black','blue','green','pink',)
for i in color_list:
  turtle.color(i)
  turtle.circle(40,80)
  turtle.circle(-40,80)
turtle.color('yellow')
turtle.seth(0)
turtle.fd(100)
turtle.circle(40,180)
turtle.fd(60)

turtle. mainloop()

