import pygame
import random


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = random.randint(10, 30) 
        self.color = (random.randint(50, 255), 
                      random.randint(50, 255), 
                      random.randint(50, 255))

        self.dx = random.randint(-5, 5)
        self.dy = random.randint(-5, 5)


        if self.dx == 0: self.dx = 3
        if self.dy == 0: self.dy = 3

    def move(self, width, height):

        self.x += self.dx
        self.y += self.dy

        if self.x - self.radius < 0 or self.x + self.radius > width:
            self.dx *= -1 
        if self.y - self.radius < 0 or self.y + self.radius > height:
            self.dy *= -1 
            
    def draw(self, screen):

        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)


pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble")
clock = pygame.time.Clock()

ball_list = []

running = True
while running:
    screen.fill((30, 30, 30)) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            new_ball = Ball(mx, my) 
            ball_list.append(new_ball) 


    for ball in ball_list:
        ball.move(WIDTH, HEIGHT)
        ball.draw(screen)        

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
