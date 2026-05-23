import pygame
import pygame_gui
import GUI

pygame.init()
ScreenSize = (1600,900)
screen = pygame.display.set_mode(ScreenSize)
pygame.display.set_caption("역전재판")
clock = pygame.time.Clock()

font = pygame.font.SysFont("malgun gothic", 20)
# bg = pygame.Surface(ScreenSize)
# bg.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager(ScreenSize)

ChatFrame = GUI.TextLabel(
    manager=manager,
    text="동현아 맞을래",
    pos=(0, 600),
    size=(1600, 290),
    bg_color=(0, 0, 0),
    alpha=50,
    layer=1,
    font_size=6.5,
    font_color="#FFFFFF",
    font_name="malgun gothic",
    align_horiz="left",    
    align_vert="top"    
)


running  = True
while running:
    DeltaTime = clock.tick(60) / 1000.0
    screen.fill("white")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        manager.process_events(event)

    manager.update(DeltaTime)

    m_x, m_y = pygame.mouse.get_pos()
    DebuggingMouseSet = font.render(f"MousePos : X({m_x}) , Y({m_y})",True, "black")

    screen.blit(DebuggingMouseSet, (m_x, m_y-20))
    
    manager.draw_ui(screen)

    pygame.display.update()
    

pygame.quit()