__author__ = 'Mandar'
import math as m
import Vertices as v
import Shapes
class Sphere():
    def __init__(self):
        pass

    def Throws_wire(self,x,y,z,r,zvp,zprp,phi,theta,gama,my_screen,color):
        s=Shapes.Creates()
        B_Power=5
        B_Points=32
        B_Mask=B_Points-2
        Sections_in_B=((B_Points/2)-1)
        Total_P=Sections_in_B*B_Points
        Section_Arc=float(6.28/Sections_in_B)
        v_list=[]
        for i in range(0,(Total_P+1)):
            x_angle = float((i & 1)+(i >> B_Power))
            y_angle = float(((i & B_Mask) >> 1) + ((i >> B_Power)*Sections_in_B))
            x_angle *= float(Section_Arc/2.0)
            y_angle *= float(Section_Arc * -1)
            x1 = (r*m.sin(x_angle)*m.sin(y_angle)) + x
            y1 = (r*m.cos(x_angle)) + y
            z1 = (r*m.sin(x_angle)*m.cos(y_angle)) + z
            vplot = v.Ver(x1,y1,z1)
            xp,yp = v.final1(vplot,zvp,zprp,phi,theta)
            v_list.append((xp,yp))
        for j in range(len(v_list)-2):
            s.line(my_screen,v_list[j][0],v_list[j][1],v_list[j+1][0],v_list[j+1][1],color)
            s.line(my_screen,v_list[j][0],v_list[j][1],v_list[j+2][0],v_list[j+2][1],color)
            s.line(my_screen,v_list[j+1][0],v_list[j+1][1],v_list[j+2][0],v_list[j+2][1],color)

    def Throws_fill(self,x,y,z,r,zvp,zprp,phi,theta,gama,my_screen,z_buffer):
        a=254
        b=154
        c=46
        B_Power=4
        B_Points=16
        B_Mask=B_Points-2
        Sections_in_B=((B_Points/2)-1)
        Total_P=Sections_in_B*B_Points
        Section_Arc=float(6.28/Sections_in_B)
        v_list=[]
        for i in range(0,(Total_P+1)):
            x_angle = float((i & 1)+(i >> B_Power))
            y_angle = float(((i & B_Mask) >> 1) + ((i >> B_Power)*Sections_in_B))
            x_angle *= float(Section_Arc/2.0)
            y_angle *= float(Section_Arc * -1)
            x1 = (r*m.sin(x_angle)*m.sin(y_angle)) + x
            y1 = (r*m.cos(x_angle)) + y
            z1 = (r*m.sin(x_angle)*m.cos(y_angle)) + z
            vplot = v.Ver(x1,y1,z1)
            v_list.append(vplot)
        for j in range(len(v_list)-2):
            v.trianglefill_no_rot(v_list[j],v_list[j+1],v_list[j+2],zvp,zprp,phi,theta,my_screen,(a,b,c),z_buffer)
            if(b>=154 and b<=252): b += 0.75


