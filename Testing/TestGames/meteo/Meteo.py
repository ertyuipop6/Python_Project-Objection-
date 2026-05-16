import pygame
import random

pygame.init()

screenSize = (1200,800)
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("운석 피하기")

clock = pygame.time.Clock()

bg_img = pygame.image.load(r"Testing\TestGames\meteo\Background.png")
bg_img = pygame.transform.scale(bg_img,screenSize)

teto_right = []
for i in range(8):
    img = pygame.image.load(rf"Testing\TestGames\meteo\TetoFrames\frame_{i}_delay-0.06s.gif")
    img = pygame.transform.rotozoom(img, 0, 0.5) # 이미지 크기를 절반으로 부드럽게 줄임
    teto_right.append(img)

teto_left = [pygame.transform.flip(img, True, False) for img in teto_right]

teto_image = teto_right

teto_rect = teto_right[0].get_rect()
teto_rect.x = (screenSize[0] - teto_rect.width) // 2
teto_rect.y = (screenSize[1] - teto_rect.height)

teto_speed = 0

pear = pygame.image.load(r"Testing\TestGames\meteo\image.png").convert_alpha()
pear = pygame.transform.rotozoom(pear, 0, 00.5)
pear_rect = pear.get_rect()
pear_rect.x = random.randint(0, screenSize[0] - pear_rect.width)
pear_rect.y = 0
pear_speed = 10

frame_index = 0 # 속도 조절용
animation_speed = 0.4 # 숫자가 작을 수록 천천히 움직이게 됨
stop = True

score = 0 
font = pygame.font.SysFont("malgun gothic",40)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                stop = False
                teto_image = teto_left
                teto_speed = -10
            if event.key == pygame.K_d:
                stop = False
                teto_image = teto_right
                teto_speed = 10
        
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_a, pygame.K_d):
                stop = True
                teto_speed = 0
                frame_index = 0
    
    teto_rect.x += teto_speed
    if teto_rect.left < 0:
        teto_rect.left = 0
    if teto_rect.right > screenSize[0]:
        teto_rect.right = screenSize[0]
    
    if not stop:
        frame_index += animation_speed + 1
        if frame_index >= len(teto_image):
            frame_index = 0
    
    pear_rect.y += pear_speed
    if pear_rect.y > screenSize[0]:
        score += 10
        pear_speed += 3
        pear_rect.y = 0
        pear_rect.x = random.randint(0, screenSize[0] - pear_rect.width)
    
    if teto_rect.colliderect(pear_rect):
        running = False
    
    screen.blit(bg_img, (0,0))

    screen.blit(teto_image[int(frame_index)], (teto_rect.x, teto_rect.y))
    
    screen.blit(pear, (pear_rect.x, pear_rect.y))
    s_text = font.render(f"Score : {score}",True,(0,0,0))
    screen.blit(s_text, (20,20))

    pygame.display.update()
    clock.tick(60)

pygame.quit()