import pygame
import GUI
import GameResource
import GameCharacter
import random
from .GamePartClass import GamePart

class Title(GamePart):
    def __init__(self):
        
        self.MainFrame = GUI.Frame(
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
            Parent = self.MainFrame.panel,
        )
        self.InitialPlayButton = GUI.ImageAndTextButton(
            manager = GameResource.UIManager,
            size = (300,75),
            pos = (100,650),
            text = "처음부터",
            font_size= 6,
            normal_image= pygame.image.load(r"Assets\UiResource\DefalutButton.png"),
            Parent = self.MainFrame.panel,
        )
        self.LoadPlayButton = GUI.ImageAndTextButton(
            manager = GameResource.UIManager,
            size = (300,75),
            pos = (450,650),
            text = "이어서",
            font_size= 6,
            normal_image= pygame.image.load(r"Assets\UiResource\DefalutButton.png"),
            Parent = self.MainFrame.panel,
        )
        self.OptionButton = GUI.ImageAndTextButton(
            manager = GameResource.UIManager,
            size = (300,75),
            pos = (800,650),
            text = "옵션",
            font_size= 6,
            normal_image= pygame.image.load(r"Assets\UiResource\DefalutButton.png"),
            Parent = self.MainFrame.panel,
        )
        self.QuitButton = GUI.ImageAndTextButton(
            manager = GameResource.UIManager,
            size = (300,75),
            pos = (1150,650),
            text = "게임 종료",
            font_size= 6,
            normal_image= pygame.image.load(r"Assets\UiResource\DefalutButton.png"),
            Parent = self.MainFrame.panel,
        )
        
        self.ButtonFrame = GUI.Frame(
            manager= GameResource.UIManager,
            size = GameResource.ScreenSize,
            pos = (0,0),
            alpha=0,
            layer = 20,
            Parent = self.MainFrame.panel
        )
        ### 게임 시작 창
        self.PlaySetFrame = GUI.Frame(
            manager= GameResource.UIManager,
            size = GameResource.ScreenSize,
            pos = (0,0),
            Parent= self.ButtonFrame.panel
        )
        self.Stage_1Button = GUI.ImageButton(
            manager = GameResource.UIManager,
            size = (500,600),
            pos = (600,0),
            normal_image= pygame.image.load(r"assets\Close.png"),
            hovered_image= pygame.image.load(r"assets\Close.png"),
            selected_image= pygame.image.load(r"assets\Close.png"),
            Parent = self.PlaySetFrame.panel,
        )
        self.Stage_1Title = GUI.TextLabel(
            manager= GameResource.UIManager,
            size = (500,100),
            pos = (600,600),
            text= "제 1화 \n 첫 번째 역전",
            Parent = self.PlaySetFrame.panel,
            alpha = 0,
            layer=3,
            font_size=6,
            align_horiz = "center",
            align_vert= "bottom"
        )
        ### 게임 시작 동의 창
        self.GameSetFrame = GUI.Frame(
            manager= GameResource.UIManager,
            size = (900,500),
            pos = (350,200),
            alpha=0,
            Parent= self.ButtonFrame.panel,
        )
        self.YesStartButton = GUI.ImageAndTextButton(
            manager = GameResource.UIManager,
            size = (300,100),
            pos = (100, 150),
            text = "네",
            font_size= 7,
            normal_image= pygame.image.load(r"Assets\UiResource\DefalutButton.png"),
            Parent = self.GameSetFrame.panel,
            )
        
        self.NopeStartButton = GUI.ImageAndTextButton(
            manager = GameResource.UIManager,
            size = (300,100),
            pos = (500,150),
            text = "아니요",
            font_size= 7,
            normal_image= pygame.image.load(r"Assets\UiResource\DefalutButton.png"),
            Parent = self.GameSetFrame.panel,
        )


        ### 게임 설정 창
        self.SettingFrame = GUI.Frame(
            manager= GameResource.UIManager,
            size = (1000,600),
            pos = (300,100),
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
            alpha=0,
            Parent= self.ButtonFrame.panel
        )
        self.YesQuitButton = GUI.ImageAndTextButton(
            manager = GameResource.UIManager,
            size = (300,100),
            pos = (100, 150),
            text = "종료",
            font_size= 7,
            normal_image= pygame.image.load(r"Assets\UiResource\DefalutButton.png"),
            Parent = self.QuitFrame.panel,
            )
        
        self.NopeQuitButton = GUI.ImageAndTextButton(
            manager = GameResource.UIManager,
            size = (300,100),
            pos = (500,150),
            text = "취소",
            font_size= 7,
            normal_image= pygame.image.load(r"Assets\UiResource\DefalutButton.png"),
            Parent = self.QuitFrame.panel,
            )
        
        
        self.ButtonFrame.panel.hide()
        self.SettingFrame.panel.hide()
        self.QuitFrame.panel.hide()
        self.GameSetFrame.panel.hide()
        self.PlaySetFrame.panel.hide()
        
        self.TitleFrames = [
            self.PlaySetFrame,
            self.QuitFrame,
            self.SettingFrame,
            self.GameSetFrame,
            ]
        self.Characters = {}
        
    def ButtonChecks(self,event):
        if self.InitialPlayButton.is_clicked(event):
            print("플레이 버튼 눌림")
            self.Open_Frame(self.PlaySetFrame)
        if self.LoadPlayButton.is_clicked(event):
            print("이어서 플레이 버튼 눌림") 
        if self.OptionButton.is_clicked(event):
            print("설정 버튼 눌림")
            self.Open_Frame(self.SettingFrame)
        if self.QuitButton.is_clicked(event):
            self.Open_Frame(self.QuitFrame)
            GameResource.GameController.Chatting("시스템","정말로 게임을 종료하시겠습니까?")
        
        ### 설정 창 부분
        if self.SettingFrameCloseButton.is_clicked(event):
            self.Close_Frame(self.SettingFrame)
        
        ### 게임 종료 부분
        if self.NopeQuitButton.is_clicked(event):
            self.Close_Frame(self.QuitFrame)
        if self.YesQuitButton.is_clicked(event):
            GameResource.Running = False
        ### 게임 시작 챕터 
        if self.Stage_1Button.is_clicked(event):
            self.Open_Frame(self.GameSetFrame)
            GameResource.GameController.Chatting("시스템","첫 번째 역전을(를) 시작합니다. \n 진행하시겠습니까?")
            print("d")
        if self.YesStartButton.is_clicked(event):
            self.Close_Frame(self.GameSetFrame)
            GameResource.GameController.NextPage()
        if self.NopeStartButton.is_clicked(event):
            self.Close_Frame(self.GameSetFrame)
            self.Open_Frame(self.PlaySetFrame)

    def KeyChecks(self,event):
        pass
    
    def RepeatKeyChecks(self,keys):
        pass
    
    def MouseChecks(self,event):
        pass
    
    def Open_Frame(self,Frame):
        self.ButtonFrame.panel.show()
        for i in self.TitleFrames:
            if i != Frame:
                i.panel.hide()
                print(i)
        Frame.panel.show()
        
    def Close_Frame(self,Frame):
        self.ButtonFrame.panel.hide()
        GameResource.GameController.CloseChatWindow()
        print(Frame.panel.visible)

    def Execute(self):
        self.MainFrame.panel.show()
        self.ButtonFrame.panel.hide()
        for i in self.TitleFrames:
            i.panel.hide()
    
    def Quit(self):
        self.MainFrame.panel.hide()
