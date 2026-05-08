import pygame
pygame.init()

screenSize = (500,500)
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Jump Game")

bg1_x = 0
bg2_x = screenSize[0]
bg_speed = 5

font = pygame.font.SysFont("malgungothic",40,True)
big_font = pygame.font.SysFont("malgungothic", 60, True)

bgimage = pygame.image.load(r"Testing\TestGames\JumpGame\Background.png")
bgimage = pygame.transform.scale(bgimage, screenSize)

img_speed = 0.4 # 작을수록 느림
frame_index = 0
img_list = []
for i in range(8):
    img = pygame.image.load(rf"TetoFrames\frame_{i}_delay-0.06s.gif")
    img = pygame.transform.rotozoom(img, 0, 0.5) 
    img_list.append(img)

pear_img = pygame.image.load(r"Testing\TestGames\JumpGame\image.png")
pear_img = pygame.transform.scale(pear_img, (60,100))

jump_s = pygame.mixer.Sound(r"Testing\TestGames\JumpGame\teto-wav.mp3")
jump_s.set_volume(0.1)

plr = img_list[0].get_rect()
plr.x = 150
plr.bottom = 500

pear = pear_img.get_rect()
pear.x = screenSize[0]
pear.bottom = 500
pear_speed = 7

y_vel = 0
score = 0
isGameOver = False
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if isGameOver:

                    plr.bottom = 500
                    pear.x = screenSize[0]
                    pear_speed = 7
                    y_vel = 0
                    score = 0 
                    isGameOver = False
                else:
                    if plr.bottom >= 500:
                        y_vel = -20
                        jump_s.play()
    if not isGameOver:
        bg1_x -= bg_speed
        bg2_x -= bg_speed

        if bg1_x <= -screenSize[0]:
            bg1_x = screenSize[0]
        if bg2_x <= -screenSize[0]:
            bg2_x = screenSize[0]
        
        frame_index += img_speed + 1
        if frame_index >= len(img_list):
            frame_index = 0

        y_vel += 1
        plr.y += y_vel
        if plr.bottom >= 500:
            plr.bottom = 500
            y_vel = 0

        pear.x -= pear_speed
        if pear.right < 0:
            pear.x = screenSize[0]
            score += 1
            pear_speed += 0.2
        
        if plr.colliderect(pear):
            isGameOver = True
        
        
    screen.blit(bgimage, (bg1_x, 0))
    screen.blit(bgimage, (bg2_x, 0))

    screen.blit(pear_img, pear)
    screen.blit(img_list[int(frame_index)], plr)

    score_t = font.render(f"Score : {score}",True,(0,0,0))
    screen.blit(score_t, (20,20))

    if isGameOver:
        overtext = big_font.render("Game Over", True, (255,0,0))
        retry_t = font.render("Space를 눌러 다시 시작", True, (0,0,0))

        screen.blit(overtext, (screenSize[0]//2 - overtext.get_width()//2, 200))
        screen.blit(retry_t, (screenSize[0]//2 - retry_t.get_width()//2, 300))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
    