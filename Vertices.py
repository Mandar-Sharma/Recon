__author__ = 'Mandar'

import numpy as np
import math as m
from pygame import gfxdraw

class Ver(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def ver(self):
        return np.matrix([[self.x], [self.y], [self.z],[1]], float)

    def length(self):
        return (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5

    def n(self):
        return ver(self)/ Ver.length(self)



def rotx(ver, ang):
    ang = m.radians(ang)
    sin1 = m.sin(ang)
    cos1 = m.cos(ang)
    return np.matrix([[1, 0, 0,0], [0, cos1, -sin1,0], [0, sin1, cos1,0],[0, 0, 0, 1]], float) * ver


def roty(ver, ang):
    ang = m.radians(ang)
    sin1 = m.sin(ang)
    cos1 = m.cos(ang)
    return np.matrix([[cos1, 0, sin1,0], [0, 1, 0,0], [-sin1, 0, cos1,0],[0,0,0,1]], float) * ver.ver()


def rotz(ver, ang):
    ang = m.radians(ang)
    sin1 = m.sin(ang)
    cos1 = m.cos(ang)
    return np.matrix([[cos1, -sin1, 0,0], [sin1, cos1, 0,0], [0, 0, 1,0],[0,0,0,1]], float) * ver


def rot(ver, phi, theta):
    final= rotx(roty(ver,-phi),-theta)
    return final


def per(ver, zvp, zprp):
    dp = float(zprp - zvp)
    mat = np.matrix(
        [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, (-zvp / dp), (zvp * (zprp / dp))], [0, 0, (-1 / dp), (zprp / dp)]],
        float)
    rec = np.matrix([[1], [1], [1], [1]], float)
    rec = mat * ver
    h = rec[3]
    xp = int(rec[0] / h)+200
    yp = int(rec[1] / h)+150
    return Ver(xp,yp,zvp).ver()


def per2(ver, zvp, zprp):
    dp = float(zprp - zvp)
    mat = np.matrix(
        [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, (-zvp / dp), (zvp * (zprp / dp))], [0, 0, (-1 / dp), (zprp / dp)]],
        float)
    rec = mat * ver
    h = rec[3]
    xp = int(rec[0] / h)+200
    yp = int(rec[1] / h)+150
    return xp,yp

def final(ver, zvp, zprp, phi, theta, gama):
    toplot = per(rot(ver, phi, theta, gama),zvp, zprp)
    return toplot

def centroid(vera,verb,verc):
    x1=float((vera.ver()[0]+verb.ver()[0]+verc.ver()[0])/3.0)
    y1=float((vera.ver()[1]+verb.ver()[1]+verc.ver()[1])/3.0)
    z1=float((vera.ver()[2]+verb.ver()[2]+verc.ver()[2])/3.0)
    return np.array([x1,y1,z1])

def final1(ver, zvp, zprp, phi, theta):
    toplot = per(rot(ver, phi, theta),zvp, zprp)
    return toplot[0],toplot[1]

#Z component of the cross product
cache = {}
def crossz(ver1,ver2):
    return ver1[0]*ver2[1, :]-ver1[1]*ver2[0,:]

#Checks if a point is inside triangle
def pointinside_triangle(ver1,vera,verb,verc):
    x= crossz((verb-vera),(ver1-vera)).A1
    y= crossz((verc-verb),(ver1-verb)).A1
    z= crossz((vera-verc),(ver1-verc)).A1
    return ((x >= 0) & (y >= 0) & (z >= 0)) | ((x < 0) & (y < 0) & (z < 0))

#Triangle Fill with Z-buffering#
def trianglefill(vera,verb,verc,zvp,zprp,phi,theta,surface,color,z_buffer,light):
    vca = rot(vera, phi, theta)
    vcb = rot(verb, phi, theta)
    vcc = rot(verc, phi, theta)
    #Obtain the triangle normal i.e A,B,C of Ax+By+Cz+D=0
    para1=vcb-vca
    para2=vcc-vca
    para3= np.squeeze(np.asarray(para1))
    para4= np.squeeze(np.asarray(para2))
    #Checked normal,works !
    normal= np.cross(para3[:3],para4[:3])
    unit_size= (normal[0]*normal[0]+normal[1]*normal[1]+normal[2]*normal[2])**0.5
    unit_normal = normal/unit_size
    cen = centroid(vera,verb,verc)
    L=light-cen
    L_size=(L[0]*L[0]+L[1]*L[1]+L[2]*L[2])**0.5
    L_unit= L/L_size
    I=np.dot(unit_normal,L_unit)
    I = abs(I)
    col_list = list(color)
    for i in range(3):
        col_list[i] *= I
    color = tuple(col_list)
    #d=-(Ax+By+Cz), Put point vca
    d=-(normal[0]*vca[0]+normal[1]*vca[1]+normal[2]*vca[2])
    pa=per(vca,zvp,zprp)
    pb=per(vcb,zvp,zprp)
    pc=per(vcc,zvp,zprp)
    minx=int(min(pa[0],min(pb[0],pc[0])))
    miny=int(min(pa[1],min(pb[1],pc[1])))
    maxx=int(max(pa[0],max(pb[0],pc[0])))
    maxy=int(max(pa[1],max(pb[1],pc[1])))
    for i in range(miny,(maxy+1)):
        if (i<0): continue
        if (i >= 300): break
        j = range (max(minx,0),min(400,(maxx+1)))
        v = np.zeros((4, len(j)))
        v[0, :] = j
        v[1, :] = i
        v[3, :] = 1
        pin = pointinside_triangle(v, pa, pb, pc)
        inside = False
        for e, j in enumerate(range(max(minx,0.0),(maxx+1))):
            if(j >= 400): break
            if pin[e]:
                inside=True
                D= zprp-zvp
                xp = j - 200
                yp= i- 150
                F = normal[0]*xp + normal[1]*yp - normal[2]*D
                point_z = ((normal[0]*xp+normal[1]*yp)*zprp+d*D)/F
                #gfxdraw.pixel(surface,j,i,color)
                if (point_z < z_buffer[i][j]):
                    z_buffer[i][j] = point_z
                    gfxdraw.pixel(surface,j,i,color)
                elif (inside): break
    for i in range(300):
        for j in range(400):
            z_buffer[i][j]=99999999.0

def trianglefill_no_rot(vera,verb,verc,zvp,zprp,phi,theta,surface,color,z_buffer):
    vca = vera.ver()
    vcb = verb.ver()
    vcc = verc.ver()
    #Obtain the triangle normal i.e A,B,C of Ax+By+Cz+D=0
    para1=vcb-vca
    para2=vcc-vca
    para3= np.squeeze(np.asarray(para1))
    para4= np.squeeze(np.asarray(para2))
    #Checked normal,works !
    normal= np.cross(para3[:3],para4[:3])
    #d=-(Ax+By+Cz), Put point vca
    d=-(normal[0]*vca[0]+normal[1]*vca[1]+normal[2]*vca[2])
    pa=per(vca,zvp,zprp)
    pb=per(vcb,zvp,zprp)
    pc=per(vcc,zvp,zprp)
    minx=int(min(pa[0],min(pb[0],pc[0])))
    miny=int(min(pa[1],min(pb[1],pc[1])))
    maxx=int(max(pa[0],max(pb[0],pc[0])))
    maxy=int(max(pa[1],max(pb[1],pc[1])))
    for i in range(miny,(maxy+1)):
        if (i<0): continue
        if (i >= 300): break
        j = range (max(minx,0),min(400,(maxx+1)))
        v = np.zeros((4, len(j)))
        v[0, :] = j
        v[1, :] = i
        v[3, :] = 1
        pin = pointinside_triangle(v, pa, pb, pc)
        inside = False
        for e, j in enumerate(range(max(minx,0.0),(maxx+1))):
            if(j >= 400): break
            if pin[e]:
                inside=True
                D= zprp-zvp
                xp = j - 200
                yp= i- 150
                F = normal[0]*xp + normal[1]*yp - normal[2]*D
                point_z = ((normal[0]*xp+normal[1]*yp)*zprp+d*D)/F
                #gfxdraw.pixel(surface,j,i,color)
                if (point_z < z_buffer[i][j]):
                    z_buffer[i][j] = point_z
                    gfxdraw.pixel(surface,j,i,color)
                elif (inside): break
    for i in range(300):
        for j in range(400):
            z_buffer[i][j]=99999999.0
