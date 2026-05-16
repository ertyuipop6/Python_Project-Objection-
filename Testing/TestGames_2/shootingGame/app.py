import pygame
import random

pygame.init()
screenSize = (800, 600)
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("슈팅 게임")

bg_img = pygame.image.load(r"Testing\TestGames_2\shootingGame\assets\Background.png")
bg_img = pygame.transform.scale(bg_img, screenSize)

miku_frames = [pygame.transform.rotozoom(pygame.image.load(rf"Testing\TestGames_2\shootingGame\assets\miku\frame_{i}_delay-0.09s.gif"),False,0.5) for i in range(8)]
miku_img = miku_frames[0]

baeteto_img = pygame.transform.rotozoom(pygame.image.load(r"Testing\TestGames_2\shootingGame\assets\image.png"),False,0.2)

teto_frames = [pygame.transform.rotozoom(pygame.image.load(rf"Testing\TestGames_2\shootingGame\assets\TetoFrames\frame_{i}_delay-0.06s.gif"),False,0.5) for i in range(8)]
teto_img = teto_frames[0]

explosion_img = pygame.transform.rotozoom(pygame.image.load(r"Testing\TestGames_2\shootingGame\assets\TetoFrames\died.png"),False,0.5)

score_font = pygame.font.SysFont("malgun gothic",30)

class miku:
    def __init__(self):
        self.index = 0
        self.frames = miku_frames
        self.frame_sec = 0.09
        self.lastTick = pygame.time.get_ticks()
        self.image = miku_img
        self.rect = self.image.get_rect()
        self.rect.centerx = screenSize[0] // 2
        self.rect.bottom = screenSize[1]
        self.speed = 5
    
    def move(self, keys):
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screenSize[0]:
            self.rect.right = screenSize[0]
    
    def draw(self, surface):
        if ((t := pygame.time.get_ticks())-self.lastTick) / 1000 > self.frame_sec:
            self.lastTick = t
            self.image = self.frames[i] if (i := self.index + 1) < len(self.frames) else self.frames[i := 0]
            self.index = i
        surface.blit(self.image, self.rect)
        
class BaeTeto:
    def __init__(self,x,y):
        self.image = baeteto_img
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = 10
    
    def update(self):
        self.rect.y -= self.speed
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Teto:
    def __init__(self):
        self.index = 0
        self.frames = teto_frames
        self.lastTick = pygame.time.get_ticks()
        self.image = teto_img
        self.speed = random.randint(3,7)
        self.frame_sec = 0.18 / self.speed
        self.reset()
    def reset(self):
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screenSize[0] - self.rect.width)
        self.rect.y = -self.rect.height
        
    def update(self):
        self.rect.y += self.speed
        if self.rect.top > screenSize[1]:
            self.reset()
    
    def draw(self, surface):
        if ((t := pygame.time.get_ticks()) - self.lastTick) / 1000 > self.frame_sec:
            self.lastTick = t
            self.image = self.frames[i] if (i := self.index + 1) < len(self.frames) else self.frames[i := 0]
            self.index = i
        surface.blit(self.image, self.rect)
        
Miku = miku()
BaeTetos = []
teto = Teto()

score = 0
clock = pygame.time.Clock()
start_tick = pygame.time.get_ticks()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                new_Bae = BaeTeto(Miku.rect.centerx,Miku.rect.top)
                BaeTetos.append(new_Bae)
        
    keys = pygame.key.get_pressed()
    Miku.move(keys)
    teto.update()
    
    for b in BaeTetos[:]: # 인덱스 꼬임 방지용
        b : BaeTeto = b
        b.update()
        
        if b.rect.colliderect(teto.rect):
            BaeTetos.remove(b)
            score += 1
            screen.blit(explosion_img, teto.rect)
            teto.reset()
            continue
        
        if b.rect.bottom <= 0:
            BaeTetos.remove(b)
        
    if teto.rect.colliderect(Miku.rect):
        running = False
    
    screen.blit(bg_img,(0,0))
    Miku.draw(screen)
    teto.draw(screen)
    
    for b in BaeTetos:
        b.draw(screen)
        
    text = score_font.render(f"Score : {score}",True,"Black")

    screen.blit(text,(20,50))
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()

    


        