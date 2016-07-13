__author__ = 'Mandar'
import Shapes
import Vertices as v
import Pointer
class Cuboid(object):

    def __init__(self):
        pass

    def definecuboidwireframe(self,x,y,z,l,b,h,zvp,zprp,phi,theta,gama,surface):

        s=Shapes.Creates()

        #Vertices

        a11 = v.Ver(x,y,z)
        b11 = v.Ver(x + l, y, z)
        c11 = v.Ver(x + l, y + b, z)
        d11 = v.Ver(x, y + b, z)
        e11 = v.Ver(x, y, z + h)
        f11 = v.Ver(x + l, y, z + h)
        g11 = v.Ver(x + l, y + b, z + h)
        h11 = v.Ver(x, y + b, z + h)
        ca1 = (x+l/2)
        ca2 = (y+b)
        ca3 = (z+h/2)
        cen = v.Ver(ca1,ca2,ca3)
        t1  = v.Ver(((3*ca1 - 20)/3),(z+100),((3*ca2-60)/3))
        t2  = v.Ver(((3*ca1 - 20)/3),(z+100),((3*ca2-60)/3)+60)
        t3  = v.Ver(((3*ca1 - 20)/3)+20,(z+100),((3*ca2-60)/3)+30)
        color = (255, 255, 255)

        a1,a2=v.final1(a11,zvp,zprp,phi,theta)
        b1,b2=v.final1(b11,zvp,zprp,phi,theta)
        c1,c2=v.final1(c11,zvp,zprp,phi,theta)
        d1,d2=v.final1(d11,zvp,zprp,phi,theta)
        e1,e2=v.final1(e11,zvp,zprp,phi,theta)
        f1,f2=v.final1(f11,zvp,zprp,phi,theta)
        g1,g2=v.final1(g11,zvp,zprp,phi,theta)
        h1,h2=v.final1(h11,zvp,zprp,phi,theta)
        cen1,cen2=v.final1(cen,zvp,zprp,phi,theta)
        t1p1,t1p2=v.final1(t1,zvp,zprp,phi,theta)
        t2p1,t2p2=v.final1(t2,zvp,zprp,phi,theta)
        t3p1,t3p2=v.final1(t3,zvp,zprp,phi,theta)
        s.line(surface,e1,e2,f1,f2,color)
        s.line(surface,f1,f2,g1,g2,color)
        s.line(surface,g1,g2,h1,h2,color)
        s.line(surface,h1,h2,e1,e2,color)

        s.line(surface,a1,a2,b1,b2,color)
        s.line(surface,b1,b2,c1,c2,color)
        s.line(surface,c1,c2,d1,d2,color)
        s.line(surface,d1,d2,a1,a2,color)

        s.line(surface,a1,a2,e1,e2,color)
        s.line(surface,b1,b2,f1,f2,color)
        s.line(surface,c1,c2,g1,g2,color)
        s.line(surface,d1,d2,h1,h2,color)

        s.line(surface,cen1,cen2,t1p1,t1p2,color)
        s.line(surface,cen1,cen2,t2p1,t2p2,color)
        s.line(surface,cen1,cen2,t3p1,t3p2,color)
        s.line(surface,t1p1,t1p2,t2p1,t2p2,color)
        s.line(surface,t2p1,t2p2,t3p1,t3p2,color)
        s.line(surface,t1p1,t1p2,t3p1,t3p2,color)

    def definecuboidfill(self,x,y,z,l,b,h,zvp,zprp,phi,theta,gama,surface,z_buffer,light):

        a11 = v.Ver(x,y,z)
        b11 = v.Ver(x + l, y, z)
        c11 = v.Ver(x + l, y + b, z)
        d11 = v.Ver(x, y + b, z)
        e11 = v.Ver(x, y, z + h)
        f11 = v.Ver(x + l, y, z + h)
        g11 = v.Ver(x + l, y + b, z + h)
        h11 = v.Ver(x, y + b, z + h)


        v.trianglefill(a11,b11,c11,zvp,zprp,phi,theta,surface,(176,176,176),z_buffer,light)
        v.trianglefill(a11,d11,c11,zvp,zprp,phi,theta,surface,(176,176,176),z_buffer,light)
        v.trianglefill(e11,f11,g11,zvp,zprp,phi,theta,surface,(176,176,176),z_buffer,light)
        v.trianglefill(e11,h11,g11,zvp,zprp,phi,theta,surface,(176,176,176),z_buffer,light)
        v.trianglefill(a11,d11,e11,zvp,zprp,phi,theta,surface,(176,176,176) ,z_buffer,light)
        v.trianglefill(h11,d11,e11,zvp,zprp,phi,theta,surface,(176,176,176) ,z_buffer,light)
        v.trianglefill(b11,f11,g11,zvp,zprp,phi,theta,surface,(176,176,176),z_buffer,light)
        v.trianglefill(c11,b11,g11,zvp,zprp,phi,theta,surface,(176,176,176),z_buffer,light)
        v.trianglefill(a11,e11,b11,zvp,zprp,phi,theta,surface,(176,176,176),z_buffer,light)
        v.trianglefill(e11,b11,f11,zvp,zprp,phi,theta,surface,(176,176,176),z_buffer,light)











