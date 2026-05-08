import pygame
pygame.init()

screenSize = (500,500)
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("움직이는 이미지")

clock = pygame.time.Clock()

# 양쪽 방향 이미지 준비
img_left = pygame.image.load(r"Testing\imageTest\image.png").convert_alpha() 

#rotozoom을 써서 각도는 0, 크기 비율은 0.5(절반)로 조절
img_left = pygame.transform.rotozoom(img_left, 0,0.5)

#오른쪽 이미지
img_right = pygame.transform.flip(img_left, True, False)

img = img_left

x = (screenSize[0] - img_left.get_width()) // 2
y = (screenSize[1] - img_left.get_height()) // 2

x_speed = 0
y_speed = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -5
                img = img_left
            elif event.key == pygame.K_RIGHT:
                x_speed = 5
                img = img_right
            elif event.key == pygame.K_UP:
                y_speed = -5
            elif event.key == pygame.K_DOWN:
                y_speed = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
        x += x_speed
        y += y_speed

        if x < 0:
            x = 0
        elif x > screenSize[0] - img.get_width():
            x = screenSize[0] - img.get_width()
        
        if y < 0:
            y = 0
        elif y > screenSize[1] - img.get_height():
            y = screenSize[1] - img.get_height()
        
        screen.fill("white")
        screen.blit(img, (x,y))
        pygame.display.update()
        
        clock.tick()

pygame.quit()