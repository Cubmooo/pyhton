import pygame
pygame.init()
i=0
screenheight=500
screenwidth=500

window = pygame.display.set_mode((600, 600))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    
    pygame.draw.rect(window, (0,   0, 255),
                 [100, 100, 400, 100], 0)
 
    window.fill((255,255,255))  
    #pygame.draw.circle(screen, (255,100,0), (screenheight/2,screenheight/2), 75)
    pygame.display.flip()
    pygame.display.update()
pygame.quit()