import pygame

pygame.init()
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption("역전재판")
clock = pygame.time.Clock()

running  = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("white")
    pygame.display.update()
    clock.tick(60) # 초당 60프레임으로 동작하게 끔 설정

pygame.quit()