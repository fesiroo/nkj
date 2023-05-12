import pygame
height = 380
width = 360
blue = (66, 135, 245)
pink = (255, 3, 255)
black = (8, 5, 10)
grey = (66, 59, 71)
yellow = (255, 255, 0)
fps = 30
speed = 15
x = 80
y = 80
pygame.init()
screen = pygame.display.set_mode((height, width))
pygame.display.set_caption("шаблон")
run = True
clock = pygame.time.Clock()
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= speed 
            elif event.key == pygame.K_RIGHT:
                x += speed
            elif event.key == pygame.K_UP:
                y -= speed
            elif event.key == pygame.K_DOWN:
                y += speed
    screen.fill(yellow)
    pygame.draw.circle(screen, grey, (x, y), 60)
    pygame.display.flip()
pygame.quit()