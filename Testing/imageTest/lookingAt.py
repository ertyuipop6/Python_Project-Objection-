import pygame

pygame.init()

screenSize = (500,500)

screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("이동하는 방향 쳐다봄")

clock = pygame.time.Clock()

# 양쪽 방향의 이미지를 미리 준비함
img_left = pygame.image.load(r"Testing\imageTest\image2.png").convert_alpha()

img_right = pygame.transform.flip(img_left,True,False)

img = img_left # 처음 보여줄 이미지

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                img = img_left
            elif event.key == pygame.K_RIGHT:
                img = img_right
    screen.fill("white")

    screen.blit(img,((screenSize[0]-img.get_width())/2,(screenSize[1]-img.get_height())/2))
    pygame.display.update()
    clock.tick(60)

pygame.quit()