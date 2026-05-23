import pygame
import pygame_gui
import GameData
import GameResource


pygame.init()

## 공유 데이터 초기화 부분임
GameResource.ScreenSize = (1600,900)
GameResource.Screen = pygame.display.set_mode(GameResource.ScreenSize)
GameResource.Clock = pygame.time.Clock()
GameResource.Font_1 = pygame.font.SysFont("malgun gothic", 20)
GameResource.UIManager = pygame_gui.UIManager(GameResource.ScreenSize,theme_path=r"Scripts\theme.json")
GameResource.Running = True
GameResource.Title = "역전 재판"

pygame.display.set_caption(GameResource.Title)
    
# ChatFrame = GUI.TextLabel(
#     manager=GameResource.UIManager,
#     text="동현아 맞을래",
#     pos=(0, 600),
#     size=(1600, 290),
#     bg_color=(0, 0, 0),
#     alpha=50,
#     layer=1,
#     font_size=6.5,
#     font_color="#FFFFFF",
#     font_name="malgun gothic",
#     align_horiz="left",    
#     align_vert="top"    
# )

GameController = GameData.GameController()

while GameResource.Running:
    DeltaTime = GameResource.Clock.tick(60) / 1000.0
    GameResource.Screen.fill("white")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameResource.Running = False
        GameController.Cycle(event)
        
        GameResource.UIManager.process_events(event)

    GameResource.UIManager.update(DeltaTime)

    m_x, m_y = pygame.mouse.get_pos()
    DebuggingMouseSet = GameResource.Font_1.render(f"MousePos : X({m_x}) , Y({m_y})",True, "black")

    GameResource.Screen.blit(DebuggingMouseSet, (m_x, m_y-20))
    
    GameResource.UIManager.draw_ui(GameResource.Screen)

    pygame.display.update()
    

pygame.quit()
