__author__ = 'Mandar'
import Shapes
import Vertices as v
import numpy as np
def point_here(x,y,z,zvp,zprp,my_screen,color):
    h=50
    s=Shapes.Creates()
    x1= (3*x-30)/3
    y1= (3*y-90)/3
    z1= (z-h)
    x2= x1
    y2= y1+60
    z2= z1
    x3= x1+30
    y3= y1+30
    z3= (z-h)
    xp,yp=v.per2(np.matrix([[x],[y],[z],[1]]),zvp,zprp)
    xp1,yp1=v.per2(np.matrix([[x1],[y1],[z1],[1]]),zvp,zprp)
    xp2,yp2=v.per2(np.matrix([[x2],[y2],[z2],[1]]),zvp,zprp)
    xp3,yp3=v.per2(np.matrix([[x3],[y3],[z3],[1]]),zvp,zprp)
    s.line(my_screen,xp,yp,xp1,yp1,color)
    s.line(my_screen,xp,yp,xp2,yp2,color)
    s.line(my_screen,xp,yp,xp3,yp3,color)
    s.line(my_screen,xp1,yp1,xp2,yp2,color)
    s.line(my_screen,xp2,yp2,xp3,yp3,color)
    s.line(my_screen,xp3,yp3,xp1,yp1,color)



