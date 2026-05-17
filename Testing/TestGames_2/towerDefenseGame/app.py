import pygame
import math
import random

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("타워 디펜스")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
RED = (255, 80, 80)
GREEN = (80, 255, 80)
YELLOW = (255, 220, 0)
TOWER_COST = 0
KILL_REWARD = 15


PATH = [(50, 550), (150, 550), (150, 450), (250, 450), (250, 150), 
        (150, 150), (150, 50), (450, 50), (450, 550), (750, 550), 
        (750, 450), (550, 450), (550, 250), (650, 250), (650, 50), (750, 50)]


class Enemy:
    def __init__(self, wave_level):
        self.x, self.y = PATH[0]
        self.target_idx = 1 # 다음 목표 지점 번호
        self.speed = random.uniform(1.2, 2.0) + (wave_level * 0.1)
        self.max_hp = 20 + (wave_level * 10000)
        self.hp = self.max_hp

    def update(self):
        # 경로 리스트를 순서대로 따라가는 로직
        if self.target_idx < len(PATH):
            tx, ty = PATH[self.target_idx]
            dist = math.hypot(tx - self.x, ty - self.y)
            if dist > self.speed:
                self.x += (tx - self.x) / dist * self.speed
                self.y += (ty - self.y) / dist * self.speed
            else:
                self.target_idx += 1 # 목표 지점 도착 시 다음 지점으로!
        return self.target_idx >= len(PATH) # 기지 도착 시 True 반환

    def draw(self):
        pygame.draw.circle(screen, RED, (int(self.x), int(self.y)), 15)
        # 체력바 (초록색 부분은 남은 체력 비율)
        pygame.draw.rect(screen, GREEN, (self.x - 15, self.y - 25, (self.hp/self.max_hp)*30, 5))

class Bullet:
    def __init__(self, x, y, target):
        self.x, self.y = x, y
        self.target = target
        self.speed = 10
        self.active = True

    def update(self, enemies):
        
        if self.target not in enemies:
            self.active = False
            return

        dist = math.hypot(self.target.x - self.x, self.target.y - self.y)
        if dist > self.speed:
            self.x += (self.target.x - self.x) / dist * self.speed
            self.y += (self.target.y - self.y) / dist * self.speed
        else:
            self.target.hp -= 10
            self.active = False

    def draw(self):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), 5)

class Tower:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.range = 150
        self.cooldown = 0

    def update(self, enemies):
        if self.cooldown > 0:
            self.cooldown -= 1
        else:

            for e in enemies:
                if math.hypot(e.x - self.x, e.y - self.y) <= self.range:
                    self.cooldown = 3 
                    return Bullet(self.x, self.y, e)
        return None

    def draw(self):
        pygame.draw.rect(screen, YELLOW, (self.x - 20, self.y - 20, 40, 40))

enemies, towers, bullets = [], [], []
castle_hp, gold, score, wave = 10, 100, 0, 1
spawned_in_wave, timer = 0, 0
font = pygame.font.SysFont("arial", 22, bold=True)

running = True
while running:
    screen.fill(BLACK)

    if len(PATH) > 1: pygame.draw.lines(screen, (50, 50, 50), False, PATH, 40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
  
            mx, my = pygame.mouse.get_pos()
            grid_x, grid_y = (mx // 40) * 40 + 20, (my // 40) * 40 + 20

            if gold >= TOWER_COST:
                towers.append(Tower(grid_x, grid_y))
                gold -= TOWER_COST


    timer += 1
    if spawned_in_wave < wave * 5:
        if timer >= 60:
            enemies.append(Enemy(wave))
            spawned_in_wave += 1
            timer = 0
    elif len(enemies) == 0:
        wave += 1
        spawned_in_wave = 0
        gold += 50 

  
    for t in towers:
        t.draw()
        new_bullet = t.update(enemies)
        if new_bullet: bullets.append(new_bullet)

    for b in bullets[:]:
        b.update(enemies)
        b.draw()
        if not b.active: bullets.remove(b) 
    for e in enemies[:]:
        if e.update(): 
            castle_hp -= 1
            enemies.remove(e)
        elif e.hp <= 0: 
            gold += KILL_REWARD
            score += 100
            enemies.remove(e)
        else:
            e.draw()

  
    info = font.render(f"WAVE: {wave} | GOLD: {gold} | HP: {castle_hp} | SCORE: {score}", True, WHITE)
    screen.blit(info, (20, 10))

    if castle_hp <= 0:
        game_over_txt = font.render("GAME OVER", True, RED)
        screen.blit(game_over_txt, (WIDTH//2 - 60, HEIGHT//2))
        pygame.display.flip()
        pygame.time.delay(3000)
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()