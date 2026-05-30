import pygame
import pygame_gui
import GameData
import GameResource 
import GameParts
import json


pygame.init()

## 공유 데이터 초기화 부분임
GameResource.ScreenSize = (1600,900)
GameResource.Screen = pygame.display.set_mode(GameResource.ScreenSize)
GameResource.Clock = pygame.time.Clock()
GameResource.UIManager = pygame_gui.UIManager(GameResource.ScreenSize,theme_path=r"Scripts\theme.json") #theme_path=r"Scripts\theme.json"
GameResource.Running = True
GameResource.Title = "역전 재판"
GameResource.GameParts = [GameParts.Title(),GameParts.Preview()]
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
        GameResource.GameController.EventCycle(event)
        GameResource.UIManager.process_events(event)
        
    GameResource.GameController.MainCycle(pygame.key.get_pressed())
    GameResource.UIManager.update(DeltaTime)
    
    GameResource.UIManager.draw_ui(GameResource.Screen)

    pygame.display.update()
    

pygame.quit()
