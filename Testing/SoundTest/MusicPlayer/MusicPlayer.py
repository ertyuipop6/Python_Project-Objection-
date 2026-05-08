import pygame
pygame.init() ## 믹서 초기화

screenSize = (800,800)
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("뮤직플레이어")

Musiclist = [
    [r"C:\Users\master\Desktop\pygame_project\Testing\SoundTest\MusicPlayer\tetoris.png",r"C:\Users\master\Desktop\pygame_project\Testing\SoundTest\MusicPlayer\柊マグネタイト - テトリス copy.mp3"],
    [r"C:\Users\master\Desktop\pygame_project\Testing\SoundTest\MusicPlayer\override.png",r"C:\Users\master\Desktop\pygame_project\Testing\SoundTest\MusicPlayer\override kasane teto.mp3"],
             ]

__index = 0

def music_play():
    
    pygame.mixer.music.load(Musiclist[__index][1])
    pygame.mixer.music.play()

    img = pygame.image.load(Musiclist[__index][0])
    img = pygame.transform.scale(img, (500, 500))
    screen.blit(img, [400-250,400-250])
    
music_play()
pause = True # 일시정지 상태 변수

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                __index = len(Musiclist)-1 if __index - 1 < 0 else __index - 1
                music_play()
            elif event.key == pygame.K_RIGHT:
                __index = 0 if __index + 1 < len(Musiclist)-1 else __index + 1
                music_play()
            elif event.key == pygame.K_SPACE:
                if pause == True:
                    pause = False
                    pygame.mixer.music.pause()
                else:
                    pause = True
                    pygame.mixer_music.unpause()
    pygame.display.update()

pygame.quit()

    