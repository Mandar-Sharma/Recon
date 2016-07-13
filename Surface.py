__author__ = 'Mandar'
def mainfunction():
    #Imports
    import pygame
    import Pointer
    import numpy as np
    import Cuboid
    import Sphere
    c1=Cuboid.Cuboid()
    s1=Sphere.Sphere()
    # Init Z-buffer
    z_buffer = np.ndarray(shape=(300, 400), dtype=float, order='F')
    # Initialize Pygames
    pygame.init()
    my_screen = pygame.display.set_mode((400, 300))
    # Screen Title
    pygame.display.set_caption('Recon 1.0')
    #colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    color1 = (89, 89, 87)
    #ViewPlane and Vanishing Point
    zvp = -200
    zprp = -500
    #Rotation Angles:
    phi = 0
    theta = 0
    gama = 0
    #Clear ZBuffer
    def clearz():
        for i in range(300):
            for j in range(400):
                z_buffer[i][j] = 99999999.0
    #Logic
    stop = False
    while not stop:
        delta = 15
        my_screen.fill(color1)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                stop = True
            if event.type == pygame.KEYDOWN:
                if event.key== pygame.K_ESCAPE:
                    stop = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    zprp=zprp-delta
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    zprp=zprp+delta
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    gama=gama+2.5
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    gama=gama-2.5
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_PERIOD:
                    theta=theta-2.5
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_COMMA:
                    theta=theta+2.5
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_PAGEUP:
                    phi=phi+2.5
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_PAGEDOWN:
                    phi=phi-2.5
        #s1.Throws_wire(0,0,0,150,zvp,zprp,phi,theta,gama,my_screen,white)
        c1.definecuboidwireframe(-150,200,10,400,10,400,zvp,zprp,phi,theta,gama,my_screen)
        pygame.display.flip()

    pygame.quit()
    quit()

