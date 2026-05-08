import pygame
pygame.init()

screen_size = (500,500)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Timer")

font = pygame.font.Font(None,50)
start = pygame.time.get_ticks()

clock = pygame.time.Clock()


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("black")
    
    currentTime = (pygame.time.get_ticks()-start) / 1000

    timer_text = str(int(currentTime))

    text = font.render(timer_text,True,"gray")
    
    screen.blit(text, ((screen_size[0]-text.get_width()) / 2 ,(screen_size[1]-text.get_height()) / 2 ))

    pygame.display.update()

    clock.tick(60)

pygame.quit()