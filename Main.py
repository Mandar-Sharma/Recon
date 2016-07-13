__author__ = 'Mandar'
import pygame
import eztext
import Surface
import Render
import CheckNet
import GPS

#colors
white = (255, 255, 255)
black = (0, 0, 0)
color1 = (89, 89, 87)
#Initialize
pygame.init()
screen = pygame.display.set_mode((400,300))
# Screen Title
pygame.display.set_caption('Recon 1.0')
#Logic
stop = False
#Authentication Text
# Display some text
font = pygame.font.Font(None, 20)
text = font.render("Authentication Successful.", 1, white)
textpos = text.get_rect()
textpos.centerx = 200
textpos.centery = 170
#Input Username and Password
textbox=eztext.Input(maxlength=20, color=(255,255,255), prompt='User:')
textbox.set_pos(150,100)
textbox.set_font(pygame.font.Font(None, 20))
textbox1=eztext.Input(maxlength=20, color=(255,255,255), prompt='Password:')
textbox1.set_pos(150,120)
textbox1.set_font(pygame.font.Font(None, 20))
textbox2=eztext.Input(maxlength=20, color=(255,255,255), prompt='Wireframe Project(w)/Render Sample(r):')
textbox2.set_pos(60,100)
textbox2.set_font(pygame.font.Font(None, 20))
#CheckConnectivity
textbox3=eztext.Input(maxlength=20, color=(255,255,255), prompt='Checking Internet Connectivity ...')
textbox3.set_pos(90,100)
textbox3.set_font(pygame.font.Font(None, 20))
textbox4=eztext.Input(maxlength=20, color=(255,255,255), prompt='Connected to the internet')
textbox4.set_pos(110,120)
textbox4.set_font(pygame.font.Font(None, 20))
textbox5=eztext.Input(maxlength=20, color=(255,255,255), prompt='Connection failed. Default Location: Pulchowk Campus')
textbox5.set_pos(20,120)
textbox5.set_font(pygame.font.Font(None, 20))
textbox6=eztext.Input(maxlength=20, color=(255,255,255), prompt='Enter current address:')
textbox6.set_pos(0,0)
textbox6.set_font(pygame.font.Font(None, 20))
textbox7=eztext.Input(maxlength=20, color=(255,255,255), prompt='(End with "."):')
textbox7.set_pos(0,20)
textbox7.set_font(pygame.font.Font(None, 20))
screen.fill(color1)
textbox3.draw(screen)
pygame.display.update()
pygame.time.delay(3000)
if(CheckNet.internet_on()):
    screen.fill(color1)
    textbox3.draw(screen)
    textbox4.draw(screen)
    pygame.display.update()
    pygame.time.delay(3000)
    stop0 = False
    while not stop0:
        screen.fill(color1)
        textbox6.draw(screen)
        events0 = pygame.event.get()
        for event in events0:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    address = textbox6.value
                    stop0 = True
        textbox6.update(events0)
        pygame.display.update()
    #Get GPS
    geocodex,geocodey=GPS.getgeo(address)
    geocode = str([geocodex,geocodey])

else:
    screen.fill(color1)
    textbox3.draw(screen)
    textbox5.draw(screen)
    pygame.display.update()
    pygame.time.delay(3000)
    address = 'Pulchowk, Lalitpur'
    geocode = str([27.68284,85.32331])
#GPS data
text1 = font.render(address, 1, white)
textpos1 = text1.get_rect()
textpos1.centerx = 325
textpos1.centery = 10
text2 = font.render(geocode, 1, white)
textpos2 = text2.get_rect()
textpos2.centerx = 325
textpos2.centery = 30
while not stop:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            stop = True
        if event.type == pygame.KEYDOWN:
            if event.key== pygame.K_ESCAPE:
                stop = True
    if((textbox.value).lower()== 'mandar'):
        stop1=False
        while not stop1:
            screen.fill(color1)
            events1 = pygame.event.get()
            textbox.draw(screen)
            textbox1.update(events1)
            textbox1.draw(screen)
            pygame.display.update()
            if((textbox1.value).lower()=='recon'):
                screen.fill(color1)
                screen.blit(text, textpos)
                textbox.draw(screen)
                textbox1.draw(screen)
                pygame.display.update()
                pygame.time.delay(2000)
                stop2=False
                while not stop2:
                    screen.fill(color1)
                    events2 = pygame.event.get()
                    textbox2.draw(screen)
                    textbox2.update(events2)
                    pygame.display.update()
                    if(textbox2.value.lower()=='w'):
                        stop2=True
                        pygame.quit()
                        Surface.mainfunction()
                    elif(textbox2.value.lower()=='r'):
                        stop2=True
                        pygame.quit()
                        Render.mainfunction()

    screen.fill(color1)
    textbox.update(events)
    textbox.draw(screen)
    screen.blit(text1, textpos1)
    screen.blit(text2, textpos2)
    pygame.display.update()

pygame.quit()
quit()
