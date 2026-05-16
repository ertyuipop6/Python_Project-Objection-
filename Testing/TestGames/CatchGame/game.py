import pygame
import random

pygame.init()
screenSize = (800, 600)
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("두더지 잡기 게임")

clock = pygame.time.Clock()

teto = pygame.image.load(r"Testing\TestGames\CatchGame\assets\teto.png").convert_alpha()
teto = pygame.transform.scale(teto, (80,80))

Max = 5
tetos = []

for _ in range(Max):
    rect = teto.get_rect()
    rect.x = random.randint(0, screenSize[0] - rect.width)
    rect.y = random.randint(0,screenSize[1] - rect.height)
    tetos.append(rect)
    
score = 0
time_limit = 60
start_time = pygame.time.get_ticks()

font = pygame.font.SysFont("malgungothic",32)

Move_teto_Event = pygame.USEREVENT +1
pygame.time.set_timer(Move_teto_Event, random.randint(1000,2000))

running = True
while running:
    c_time = pygame.time.get_ticks()
    e_time = (c_time - start_time) // 1000
    remain_time = 0 if (a := (time_limit - e_time)) <= 0 else a
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == Move_teto_Event:
            for teto_r in tetos:
                teto_r.x = random.randint(0, screenSize[0] - teto_r.width)
                teto_r.y = random.randint(0,screenSize[1] - teto_r.height)
        
            pygame.time.set_timer(Move_teto_Event, random.randint(1000,2000))
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for teto_r in tetos:
                if teto_r.collidepoint(event.pos):
                    score += 1
                    
                    teto_r.x = random.randint(0, screenSize[0] - teto_r.width)
                    teto_r.y = random.randint(0,screenSize[1] - teto_r.height)
                    
                    break
    if remain_time <= 0:
        runnig = False
    
    screen.fill("yellowgreen")
    
    for teto_r in tetos:
        screen.blit(teto, teto_r)
    score_t = font.render(f"Score : {score}",True,"black")
    time_t = font.render(f"Timne : {remain_time}",True,"red")
    
    screen.blit(score_t, (20,20))
    screen.blit(time_t, (20,60))
    
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
    