import pygame

pygame.init()

SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

obj = pygame.Rect((300,250,50,50))

run = True

while run:

    screen.fill((255,255,255))

    pygame.draw.rect(screen,(255,0,0),obj)

    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        obj.move_ip(-1,0)
    elif key[pygame.K_d]:
        obj.move_ip(1,0)
    elif key[pygame.K_w]:
        obj.move_ip(0,-1)
    elif key[pygame.K_s]:
        obj.move_ip(0,1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()