import pygame
pygame.init() # 내부적으로 Mixer가 초기화 됨

Clock = pygame.time.Clock()

screenSize = (500,500)

screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("소리 테스트 (배경 음악 및 효과음(T))")

font = pygame.font.SysFont("malgun gothic",40)

# 배경음악 설정
pygame.mixer.music.load(r"C:\Users\master\Desktop\pygame_project\Testing\SoundTest\柊マグネタイト - テトリス.mp3")
pygame.mixer.music.set_volume(0.2) # 배경 음악 볼륨 설정
pygame.mixer.music.play(-1)

# 효과음 불러오기 (효과음일땐 용량 작은게 좋음)
s_teto = pygame.mixer.Sound(r"C:\Users\master\Desktop\pygame_project\Testing\SoundTest\teto-wav.mp3")

cT = "T키를 눌러보세요."

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                s_teto.play()
                cT = "Teto"
    screen.fill("yellow")

    text_ui = font.render(cT,True,"red")
    
    text_rect = text_ui.get_rect(center = (screenSize[0]//2,screenSize[1]//2))
    screen.blit(text_ui,text_rect)

    pygame.display.update()
    Clock.tick(60)

pygame.quit()