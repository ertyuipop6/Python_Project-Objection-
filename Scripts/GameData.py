import pygame
import GUI
import GameResource

class Title():
    def __init__(self):
        
        self.TitlePage = GUI.Frame(
            manager= GameResource.UIManager,
            size = GameResource.ScreenSize,
            pos = (0,0),
            alpha=0,
        )
        
        self.Title = GUI.ImageLabel(
            manager= GameResource.UIManager,
            size = (500,600),
            pos = (600,0),
            image_surface = pygame.image.load(r"assets\Hahaha.png"),
            Parent = self.TitlePage.panel,
        )
        self.InitialPlayButton = GUI.TextButton(
            manager = GameResource.UIManager,
            size = (300,100),
            pos = (100,650),
            text = "처음부터",
            Parent = self.TitlePage.panel,
            )
        self.LoadPlayButton = GUI.TextButton(
            manager = GameResource.UIManager,
            size = (300,100),
            pos = (450,650),
            text = "이어서",
            Parent = self.TitlePage.panel,
            )
        self.OptionButton = GUI.TextButton(
            manager = GameResource.UIManager,
            size = (300,100),
            pos = (800,650),
            text = "옵션",
            Parent = self.TitlePage.panel,
        )
        
        self.QuitButton = GUI.TextButton(
            manager = GameResource.UIManager,
            size = (300,100),
            pos = (1150,650),
            text = "게임 종료",
            Parent = self.TitlePage.panel,
            )
        
        self.ButtonFrame = GUI.Frame(
            manager= GameResource.UIManager,
            size = GameResource.ScreenSize,
            pos = (0,0),
            alpha=0,
            layer = 5,
        )
        
        ### 게임 설정 창
        self.SettingFrame = GUI.Frame(
            manager= GameResource.UIManager,
            size = (1000,600),
            pos = (500,100),
            Parent= self.ButtonFrame.panel
        )
        self.SettingFrameTitle = GUI.TextLabel(
            manager = GameResource.UIManager,
            size = (700,100),
            pos= (100, 50),
            text = "설정",
            font_size = 6,
            alpha= 50,
            Parent = self.SettingFrame.panel,
        )
        self.SettingFrameCloseButton = GUI.ImageButton(
            manager = GameResource.UIManager,
            size = (100,100),
            pos = (900,0),
            normal_image= pygame.image.load(r"assets\Close.png"),
            hovered_image= pygame.image.load(r"assets\Close.png"),
            selected_image= pygame.image.load(r"assets\Close.png"),
            Parent = self.SettingFrame.panel,
            )

        ### 게임 종료 창
        self.QuitFrame = GUI.Frame(
            manager= GameResource.UIManager,
            size = (900,500),
            pos = (350,200),
            Parent= self.ButtonFrame.panel
        )
        self.QuitFrameTitle = GUI.TextLabel(
            manager = GameResource.UIManager,
            size = (700,200),
            pos= (100, 50),
            text = "정말로 게임을 종료하시겠습니까?",
            font_size = 6,
            alpha= 100,
            Parent = self.QuitFrame.panel,
        )
        self.YesQuitButton = GUI.TextButton(
            manager = GameResource.UIManager,
            size = (300,100),
            pos = (100, 300),
            text = "종료",
            Parent = self.QuitFrame.panel,
            )
        
        self.NopeQuitButton = GUI.TextButton(
            manager = GameResource.UIManager,
            size = (300,100),
            pos = (500,300),
            text = "취소",
            Parent = self.QuitFrame.panel,
            )
        
        
        
        self.ButtonFrame.panel.hide()
        self.SettingFrame.panel.hide()
        self.QuitFrame.panel.hide()

        self.TitleFrames = [self.QuitFrame,self.SettingFrame]

    def ButtonChecks(self,event):
        if self.InitialPlayButton.is_clicked(event):
            print("플레이 버튼 눌림")
        if self.LoadPlayButton.is_clicked(event):
            print("이어서 플레이 버튼 눌림") 
        if self.OptionButton.is_clicked(event):
            print("설정 버튼 눌림")
            self.Open_Frame(self.SettingFrame)
        if self.QuitButton.is_clicked(event):
            print("게임 종료 버튼 눌림")
            self.Open_Frame(self.QuitFrame)
        
        ### 설정 창 부분
        if self.SettingFrameCloseButton.is_clicked(event):
            self.Close_Frame(self.SettingFrame)
        
        ### 게임 종료 부분
        if self.NopeQuitButton.is_clicked(event):
            self.Close_Frame(self.QuitFrame)
        if self.YesQuitButton.is_clicked(event):
            GameResource.Running = False
            
    def Open_Frame(self,Frame):
        self.ButtonFrame.panel.show()
        for i in self.TitleFrames:
            if i != Frame:
                i.panel.hide()
        print(Frame.panel.visible)
        
    def Close_Frame(self,Frame):
        self.ButtonFrame.panel.hide()
        print(Frame.panel.visible)
    
class GameController():
    '''실질적으로 게임을 파트 별로 나눠 실행 시켜주는 클래스임'''
    def __init__(self):
        self.Part = 0 # 0이면 Title
        self.TitlePart = Title()
    def Cycle(self,event):
        if self.Part == 0:
            self.TitlePart.ButtonChecks(event)