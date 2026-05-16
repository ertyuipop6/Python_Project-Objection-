import pygame
import random

pygame.init()

screenSize = (1000, 800)
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("카드 맞추기 게임")
Clock = pygame.time.Clock()
font = pygame.font.SysFont("malgun gothic",50)
BackCard = pygame.image.load(r"Testing\TestGames_2\memoryGame\assets\carddd.png")

cardTypes = {1 : (pygame.image.load(r"Testing\TestGames_2\memoryGame\assets\teto1.png"),None),
             2 : (pygame.image.load(r"Testing\TestGames_2\memoryGame\assets\teto2.png"),None),
             3 : (None , [pygame.image.load(rf"Testing\TestGames_2\memoryGame\assets\mikuEnjoy\frame_{i}_delay-0.09s.gif") for i in range(8)],0.09),
             4 : (None , [pygame.image.load(rf"Testing\TestGames_2\memoryGame\assets\mikuMe\frame_{i:02d}_delay-0.09s.gif") for i in range(16)],0.09),
             5 : (None , [pygame.image.load(rf"Testing\TestGames_2\memoryGame\assets\mikushout\frame_{i:02d}_delay-0.05s.gif") for i in range(16)],0.05),
             6 : (None , [pygame.image.load(rf"Testing\TestGames_2\memoryGame\assets\mikuWa\frame_{i}_delay-0.08s.gif") for i in range(4)],0.08),
             }
class Game:
    def __init__(self):
        self.total = 12 # 총 카드 수
        self.cardlist = []
        self.firstCard = None # 첫 번째로 뒤집은 카드
        self.secondCard = None # 두 번째로 뒤집은 카드
        self.matched_count = 0 
        
        self.limit_t = 30
        self.start_tick = 0
        
        number = [1,2,3,4,5,6,1,2,3,4,5,6]
        random.shuffle(number)
        for i in range(self.total):
            if cardTypes[number[i]][0] != None:
                self.cardlist.append(Card(i, number[i],cardTypes[number[i]][0]))
            else:
                self.cardlist.append(GifCard(i, number[i],cardTypes[number[i]][1],cardTypes[number[i]][2]))
        
    def ready(self):
        screen.fill("black")
        font = pygame.font.SysFont("malgun gothic", 100)
        text = font.render("Look!", True, "White")
        screen.blit(text, (320,40))
        
        for pt in self.cardlist:
            pt.front = True
            pt.draw()
        
        pygame.display.update()
        pygame.time.delay(3000)

        for pt in self.cardlist:
            pt.front = False
        
        self.start_tick = pygame.time.get_ticks()
        
    def check(self,xy):
        for pt in self.cardlist:
            if pt.rect.collidepoint(xy) and not pt.front:
                pt.front = True
                pt.draw()
                pygame.display.update()
                
                if self.firstCard is None:
                    self.firstCard = pt
                elif self.firstCard != pt:
                    self.secondCard = pt
                    pygame.time.delay(500)
                    
                    if self.firstCard.number == self.secondCard.number:
                        self.matched_count += 1
                    else:
                        screen.fill("red")
                        
                        for pt in self.cardlist:
                            pt.draw()
                        
                        pygame.display.update()
                        pygame.time.delay(200)
                        
                        self.firstCard.front = False
                        self.secondCard.front = False
                        
                    self.firstCard = None
                    self.secondCard = None
    def draw(self, surface):
        surface.fill("white")
        r_time = self.limit_t-((pygame.time.get_ticks() - self.start_tick) // 1000)
        
        if r_time < 0:
            r_time = 0
        
        
        timer_t = font.render(f"time : {r_time}",True,"white" if r_time > 5 else "red")
        screen.blit(timer_t, (600, 50))
        
        for card in self.cardlist:
            card.draw()
        
        return r_time

    
class Card:
    def __init__(self,index, number, img = None):
        self.index = index
        self.number = number
        
        self.x = (self.index % 4 + 1) * 200
        self.y = (self.index // 4 + 1) * 200
        
        self.image : pygame.Surface =  img
        self.rect = self.image.get_rect(x = self.x, y = self.y) if self.image is not None else None
        self.front = False
    
    def draw(self):
        
        if self.front:
            screen.blit(self.image, (self.x, self.y))
        else:
            screen.blit(BackCard,(self.x,self.y))

class GifCard(Card): 
    def __init__(self,index,number,Frames,time):
        super().__init__(index,number)
        
        self.Frameindex = 0
        self.Frames = Frames
        self.lastTick = pygame.time.get_ticks()
        self.image : pygame.Surface =  Frames[0]
        self.rect = self.image.get_rect(x = self.x, y = self.y)
        self.time = time
        
    def draw(self):
        if self.front:
            
            if ((a := pygame.time.get_ticks()) - self.lastTick) / 1000 > self.time:
                self.image = self.Frames[i] if (i := self.Frameindex + 1) < len(self.Frames) else self.Frames[i := 0]
                self.lastTick = a
                self.Frameindex = i
            screen.blit(self.image, (self.x, self.y))
        else:
            screen.blit(BackCard,(self.x,self.y))
            
cardGame = Game()
cardGame.ready()

running = True
victory = False
fail = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            cardGame.check(pygame.mouse.get_pos())
    
    r_time = cardGame.draw(screen)
    
    
    if cardGame.matched_count == 6:
        g_t = font.render("다 맞추셨습니다.",True,"blue")
        screen.blit(g_t,(320,40))
        victory = True
    elif r_time <= 0:
        g_t = font.render("다시 시도하세요.", True , "red")
        screen.blit(g_t,(320,40))
        fail = True
        
    pygame.display.update()
    Clock.tick(60)
    
    if fail or victory:
        pygame.time.delay(500)
        running = False

pygame.quit()
        
        
        
                    
                    
        
        