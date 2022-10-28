import pygame
pygame.init()
displaywidth = 800
displayheight = 800
surface= pygame.display.set_mode(displaywidth, displayheight)
pygame.display.set_caption("sweep the room and change the bed sheet")
displayimage = pygame.mage.load(r'C:\Users\gumgu\Download.png')
while True:
    surface.fill((255, 255, 255))
    surface.blit(displayimage, (0, 0))
    for event in pygame.event.get():
