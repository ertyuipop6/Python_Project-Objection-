import pygame
import pygame_gui
import GameData
import GameResource
import json


pygame.init()

## 공유 데이터 초기화 부분임
GameResource.ScreenSize = (1600,900)
GameResource.Screen = pygame.display.set_mode(GameResource.ScreenSize)
GameResource.Clock = pygame.time.Clock()
GameResource.Font_1 = pygame.font.SysFont("malgun gothic", 20)
GameResource.UIManager = pygame_gui.UIManager(GameResource.ScreenSize) #theme_path=r"Scripts\theme.json"
GameResource.Running = True
GameResource.Title = "역전 재판"
GameResource.GameController = GameData.GameController()

with open(r"assets\GameChatData.json","r",encoding="utf-8") as file:
    GameResource.GameTextJsonData = json.load(file)

pygame.display.set_caption(GameResource.Title)



while GameResource.Running:
    DeltaTime = GameResource.Clock.tick(60) / 1000.0
    GameResource.Screen.fill("white")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameResource.Running = False
        GameResource.GameController.Cycle(event)
        GameResource.GameController.KeyCycle(event)
        GameResource.UIManager.process_events(event)
        
    GameResource.GameController.RepeatKeyCycle(pygame.key.get_pressed())
    GameResource.GameController.Texting()
    GameResource.GameController.AnimationCycle()
    GameResource.UIManager.update(DeltaTime)
    m_x, m_y = pygame.mouse.get_pos()
    DebuggingMouseSet = GameResource.Font_1.render(f"MousePos : X({m_x}) , Y({m_y})",True, "black")

    GameResource.Screen.blit(DebuggingMouseSet, (m_x, m_y-20))
    
    GameResource.UIManager.draw_ui(GameResource.Screen)

    pygame.display.update()
    

pygame.quit()
