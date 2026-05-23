import pygame
import random
pygame.init()

screenSize = (500,500)
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("날아다니다")
clock = pygame.time.Clock()

gravity = 0.2
bird_speed = 0
score = 0
font = pygame.font.SysFont("malgungothic",40)

img = pygame.image.load(r"Testing\TestGames\BirdGame\image1.png")
img = pygame.transform.rotozoom(img, False, 0.2)
bird_rect = img.get_rect()
bird_rect.x = 100
bird_rect.y = 300

pipe_top_img = pygame.image.load("Testing\TestGames\BirdGame\image.png")
pipe_top_img = pygame.transform.rotozoom(pipe_top_img, False, 0.5)
pipe_bottom_img = pygame.transform.flip(pipe_top_img,False,True)

Pipe_Gap = 150

top_pipes = []
bottom_pipes = []

SPAWNPIPE = pygame.USEREVENT # 사용자 정의 이벤트인데, 여러개 일시, + 번호 해서 만들 수 있음, pygame.USEREVENT + 1 , pygame.USEREVENT + 2 이런식
pygame.time.set_timer(SPAWNPIPE, 3000)

def create_pipe():
    random_pos = random.randint(200,400)
    
    # 상단 파이프는 통로 중앙에서 간격의 절반 만큼 위에서 끝나게
    top_rect = pipe_top_img.get_rect(midbottom = (screenSize[0] + 100, random_pos - Pipe_Gap / 2))
    
    # 하단 파이프는 통로 중앙에서 간격의 절반 만큼 아래에서 시작하게
    bottom_rect = pipe_bottom_img.get_rect(midtop = (screenSize[0] + 100, random_pos + Pipe_Gap / 2))
    
    top_pipes.append(top_rect)
    bottom_pipes.append(bottom_rect)
    
def check():
    
    for pipe in top_pipes:
        if bird_rect.colliderect(pipe):
            return True
    
    for pipe in bottom_pipes:
        if bird_rect.colliderect(pipe):
            return True
    
    if bird_rect.top <= 0 or bird_rect.bottom >= screenSize[1]:
        return True

    return False


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_speed = -4
        
        if event.type == SPAWNPIPE:
            create_pipe()
    
    
    screen.fill("skyblue")
    
    bird_speed += gravity
    bird_rect.y += bird_speed
    screen.blit(img, bird_rect)  
    
    for pipe in top_pipes:
        pipe.x -= 3
        screen.blit(pipe_top_img, pipe)
    
    for pipe in bottom_pipes:
        pipe.x -= 3
        screen.blit(pipe_bottom_img, pipe)

    score += 1/60
    score_sf = font.render(f"Score : {int(score)}", True, "white")
    screen.blit(score_sf, (10,10))
    
    if check():
        running = False
    
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()    