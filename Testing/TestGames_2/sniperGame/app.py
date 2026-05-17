import pygame
import random
import math

screenSize = 800, 600
mapSize = 2000, 1500

class Miku:
    def __init__(self,x,y):
        self.x, self.y = x,y
        self.img = pygame.transform.rotozoom(pygame.image.load(r"Testing\TestGames_2\sniperGame\assets\miku_cry.png"), False, 0.5)
        self.rect = self.img.get_rect()
        self.hp, self.mx_hp = 100,100
        self.speed = 0.8

    def update(self):
        self.x += self.speed

    def draw(self, screen, bg_x, bg_y):
        m_draw_x = (self.x + bg_x) % mapSize[0]
        m_draw_y = (self.y + bg_y) % mapSize[1]

        self.rect.x, self.rect.y = m_draw_x , m_draw_y

        screen.blit(self.img, self.rect)

        pygame.draw.rect(screen, "red", (m_draw_x, m_draw_y - 15, self.rect.w, 8))
        hp_w = (self.hp / self.mx_hp) * self.rect.w
        pygame.draw.rect(screen, "green", (m_draw_x, m_draw_y - 15, hp_w if hp_w > 0 else 0, 8))

class Teto:
    def __init__(self,x,y):
        self.speed = random.uniform(1.0, 5.0)
        self.frames = [pygame.transform.rotozoom(pygame.image.load(rf"Testing\TestGames_2\sniperGame\assets\TetoFrames\frame_{i}_delay-0.06s.gif"), False, 0.5 * self.speed / 2.5 ) for i in range(8)]
        self.image = self.frames[0]
        self.index = 0
        self.lastTick = pygame.time.get_ticks()
        

        self.x, self.y = x, y
        self.rect = self.image.get_rect()
        self.frame_sec = 0.06 / self.speed

    def update(self, target):
        dx, dy = target.x - self.x, target.y - self.y
        dist = math.hypot(dx, dy)
        if dist > 50:
            self.x += (dx / dist) * self.speed
            self.y += (dy / dist) * self.speed
        else:
            target.hp -= 0.5
        
    def draw(self, screen, bg_x, bg_y):
        draw_x = (self.x + bg_x) % mapSize[0]
        draw_y = (self.y + bg_y) % mapSize[1]
        
        if -100 < draw_x < screenSize[0] + 100 and -100 < draw_y < screenSize[1]:
            
            if ((t := pygame.time.get_ticks()) - self.lastTick) / 1000 > self.frame_sec:
                self.lastTick = t
                self.image = self.frames[i] if (i := self.index + 1) < len(self.frames) else self.frames[i := 0]
                self.index = i
            self.rect.x , self.rect.y = draw_x, draw_y
            screen.blit(self.image, self.rect)


pygame.init()
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("타겟 게임임")
clock = pygame.time.Clock()

bg = pygame.Surface(mapSize)
bg.fill((40,40,40))
for i in range(0, mapSize[0], 200):
    pygame.draw.line(bg, (60,80,60), (i, 0), (i, mapSize[1]), 2)
    pygame.draw.line(bg, (60,80,60), (0, i), (mapSize[0], i) , 2)


scope_layer = pygame.Surface(screenSize, pygame.SRCALPHA)
scope_layer.fill((0,0,0,180))
pygame.draw.circle(scope_layer, (0,0,0,0), (screenSize[0]//2 , screenSize[1]//2), 250)
pygame.draw.circle(scope_layer, (0,0,0), (screenSize[0]//2 , screenSize[1]//2), 250,5)
bg_x, bg_y = 0,0
score, is_firing = 0,0
game_over = False
game_win = False

miku = Miku(200,750)
enemies = []

SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT, 1500)

font = pygame.font.SysFont("malgun gothic", 30, bold = True)
large_font = pygame.font.SysFont("malgun gothic", 60, bold = True)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not game_over and not game_win:
            if event.type == SPAWN_EVENT:
                if len(enemies) < 12:
                    enemies.append(Teto(random.randint(0, mapSize[0]), random.randint(0, mapSize[1])))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if is_firing == 0:
                    is_firing = 10
                    for e in enemies[:]:
                        sx = (e.x + bg_x) % mapSize[0]
                        sy = (e.y + bg_y) % mapSize[1]
                        if e.rect.collidepoint(screenSize[0]//2, screenSize[1]//2):
                            score += 100
                            enemies.remove(e)
                            break
    
    if not game_over and not game_win:
        mx, my = pygame.mouse.get_pos()
        bg_x -= (mx - screenSize[0] // 2) * 0.1
        bg_y -= (my - screenSize[1] // 2) * 0.1
        
        bg_x = 0 if bg_x <= 0 else mapSize[0] if bg_x >= mapSize[0] else bg_x
        bg_y = 0 if bg_y <= 0 else mapSize[1] if bg_y >= mapSize[1] else bg_y
        miku.update()

        if miku.x >= mapSize[0] - 250: 
            game_win = True
        if miku.hp <= 0:
            game_over = True
        
        for e in enemies:
            e.update(miku)
    
    screen.fill("black")
    
    lx, ly = bg_x % mapSize[0], bg_y % mapSize[1]

    screen.blit(bg, (lx - mapSize[0], ly - mapSize[1]))
    screen.blit(bg, (lx, ly - mapSize[1]))
    screen.blit(bg, (lx - mapSize[0], ly))
    screen.blit(bg, (lx,ly))
    
    sz_draw_x = (mapSize[0] - 250 + bg_x) % mapSize[0]
    sz_draw_y = (700 + bg_y) % mapSize[1]

    pygame.draw.rect(screen, (0,255,100), (sz_draw_x, sz_draw_y, 250, 160) , 4)
    sz_text = font.render("safe zone", True, (0,255,100))
    screen.blit(sz_text, (sz_draw_x + 35, sz_draw_y - 40))
    
    center_x = sz_draw_x + 125
    center_y = sz_draw_y + 80
    pygame.draw.circle(screen, (0, 255, 100), (int(center_x), int(center_y)), 60, 5)
    pygame.draw.line(screen, (0, 255, 100), (center_x - 30, center_y - 35), (center_x - 30, center_y + 35), 10) 
    pygame.draw.line(screen, (0, 255, 100), (center_x + 30, center_y - 35), (center_x + 30, center_y + 35), 10) 
    pygame.draw.line(screen, (0, 255, 100), (center_x - 30, center_y), (center_x + 30, center_y), 10) 

    miku.draw(screen, bg_x, bg_y)
    for e in enemies:
        e.draw(screen, bg_x, bg_y)

    
    gun_recoil = is_firing * 4
    gun_x = screenSize[0] // 2 - 40
    pygame.draw.rect(screen, (30,30,30), (gun_x, screenSize[1] - 200 + gun_recoil, 80, 200))
    pygame.draw.rect(screen, (10,10,10), (screenSize[0]//2 - 10, screenSize[1] - 250 + gun_recoil, 20, 100))

    screen.blit(scope_layer, (0,0))
    pygame.draw.line(screen, "black", (screenSize[0]//2 - 250, screenSize[1]//2), (screenSize[0]//2 + 250, screenSize[1]//2), 2)
    pygame.draw.line(screen, "black", (screenSize[0]//2, screenSize[1]//2 - 250), (screenSize[0]//2, screenSize[1]//2 + 250), 2)


    if is_firing > 0:
        pygame.draw.circle(screen, (255, 200, 0), (screenSize[0] // 2 ,screenSize[1]//2), is_firing*5, 3)
        is_firing -= 1
    
    pygame.draw.circle(screen, (255,0,0), (screenSize[0] // 2, screenSize[1] // 2),5)
    
    score_surf = font.render(f"Score : {score : 05d} | Miku HP : {int(max(0, miku.hp))} %", True, "white")
    screen.blit(score_surf, (20,20))

    if game_over:
        screen.blit(large_font.render("MISSION FAILED", True, (255,50,50)), (150, 250))
    elif game_win:
        screen.blit(large_font.render("MISSION CLEAR", True, (50,255,50)), (150,250))

    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
    
    