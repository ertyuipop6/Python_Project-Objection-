import pygame
pygame.init()

ScreenSize = (500,500)
screen = pygame.display.set_mode(ScreenSize)
pygame.display.set_caption("이미지 테스팅")

clock = pygame.time.Clock()

img = pygame.image.load(r"Testing\imageTest\image.png").convert_alpha() # convert_alpha는 누끼 부분이 검은색으로 나오지 않도록 처리하는 것임

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    screen.blit(img, ((ScreenSize[0] - img.get_width()) // 2 , (ScreenSize[1] - img.get_height()) // 2))
    pygame.display.update()
    clock.tick(60)

pygame.quit()