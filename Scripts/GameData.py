import pygame
import GUI
import GameResource
import random
import GameCharacter

class Title():
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
        self.InitialPlayButton = GUI.TextButton(
            manager = GameResource.UIManager,
            size = (300,100),
            pos = (100,650),
            text = "처음부터",
            Parent = self.MainFrame.panel,
            )
        self.LoadPlayButton = GUI.TextButton(
            manager = GameResource.UIManager,
            size = (300,100),
            pos = (450,650),
            text = "이어서",
            Parent = self.MainFrame.panel,
            )
        self.OptionButton = GUI.TextButton(
            manager = GameResource.UIManager,
            size = (300,100),
            pos = (800,650),
            text = "옵션",
            Parent = self.MainFrame.panel,
        )
        
        self.QuitButton = GUI.TextButton(
            manager = GameResource.UIManager,
            size = (300,100),
            pos = (1150,650),
            text = "게임 종료",
            Parent = self.MainFrame.panel,
            )
        
        self.ButtonFrame = GUI.Frame(
            manager= GameResource.UIManager,
            size = GameResource.ScreenSize,
            pos = (0,0),
            alpha=0,
            layer = 5,
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
        self.YesStartButton = GUI.TextButton(
            manager = GameResource.UIManager,
            size = (300,100),
            pos = (100, 150),
            text = "네",
            Parent = self.GameSetFrame.panel,
            )
        
        self.NopeStartButton = GUI.TextButton(
            manager = GameResource.UIManager,
            size = (300,100),
            pos = (500,150),
            text = "아니요",
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
        GameResource.GameController.EndChatting()
        print(Frame.panel.visible)

    def Execute(self):
        self.MainFrame.panel.show()
        self.ButtonFrame.panel.hide()
        for i in self.TitleFrames:
            i.panel.hide()
    
    def Quit(self):
        self.MainFrame.panel.hide()

















































class GamePart_1():
    def __init__(self):
        self.Part = 1
        self.__index = 0
        self.MainFrame = GUI.Frame(
            manager=GameResource.UIManager,
            pos = (0,0),
            size = GameResource.ScreenSize,
            alpha = 0,
        )
        self.Characters = {"Zundamon" : GameCharacter.Character(Name = "Zundamon",Anim = {"Idle" : [pygame.image.load(rf"assets\Zunda\frame_{i:02d}_delay-0.1s.gif") for i in range(10)]})}
        
    def NextChat(self):
        if GameResource.GameController.CanChatting:
            if self.__index < len(ChatData := GameResource.GameTextJsonData["Game_Part_1"][f"Starting_{self.Part}"]):
                GameResource.GameController.CanChatting = False
                GameResource.GameController.ChatIndex = 0
                
                ChatData = ChatData[self.__index]
                
                GameResource.GameController.CurrentChat = ChatData["Chat"]
                Animation = None if not "Anim" in ChatData else ChatData["Anim"]
                    
                GameResource.GameController.Chatting(ChatData["Speaker"],ChatData["Chat"][GameResource.GameController.ChatIndex],Animation=Animation)
                
                
                self.__index += 1
            else:
                self.Part += 1
                self.__index = 0
        else:
            GameResource.GameController.ChatIndex = len(GameResource.GameController.CurrentChat)-1
            
    def ButtonChecks(self,event):
        pass
    
    def KeyChecks(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.NextChat()
                
    def RepeatKeyChecks(self,keys):
        pass
    def MouseChecks(self,event):
        pass
    
    def Execute(self):
        self.MainFrame.panel.show()
        self.NextChat()
        
    def Quit(self):
        self.MainFrame.panel.hide()

















































class GameController():
    '''실질적으로 게임을 파트 별로 나눠 실행 시켜주는 클래스임'''
    def __init__(self):
        self.Part = -1 # 0이면 Title 
        
        self.TypeSound = pygame.mixer.Sound(r"assets\test2.mp3")
        self.TypeSound.set_volume(0.2)
        self.SoundTick = 1
        self.lastPlaytick = pygame.time.get_ticks()
        
        self.ChatIndex = 0
        self.CanChatting = True
        self.CurrentChat = ""
        self.lastTextingTick = pygame.time.get_ticks()
        self.TextSpeed = 0
        
        self.AnimationType = None
        self.Speaker = None
        
        self.GameChatFrame = GUI.Frame(
            manager = GameResource.UIManager,
            pos = (0,550),
            size = (GameResource.ScreenSize[0],350),
            bg_color = (60,60,60),
            alpha= 0,
            layer = 10,
        )
        self.ChatWindow = GUI.Frame(
            manager = GameResource.UIManager,
            pos = (0,50),
            size = (GameResource.ScreenSize[0],250),
            bg_color = (60,60,60),
            alpha= 255,
            Parent=self.GameChatFrame.panel,
        )
        self.ChatTextlabel = GUI.TextLabel(
            manager = GameResource.UIManager,
            pos = (GameResource.ScreenSize[0]//4-50,20),
            size = (GameResource.ScreenSize[0]//2+200,260),
            text = "아니 세상에 자기가 노인이라는 사람인데 키설정을 했대 인제 처음하는건가봐",
            font_size= 7,
            bg_color = (60,60,60),
            alpha= 255,
            layer = 5,
            align_horiz='left',
            align_vert='top',
            Parent= self.ChatWindow.panel,
        )
        self.SpeakerFrame = GUI.Frame(
            manager = GameResource.UIManager,
            pos = (125,15),
            size = (225,75),
            bg_color = GameResource.ChangeColorToInt("#FFFFFF"),
            alpha= 255,
            layer=5,
            Parent= self.GameChatFrame.panel,
        )
        self.SpeakerName = GUI.TextLabel(
                        manager = GameResource.UIManager,
            pos = (0,0),
            size = (225,75),
            bg_color = GameResource.ChangeColorToInt("#0099FF"),
            text = "즌다몬",
            font_size= 5.5,
            alpha= 255,
            Parent= self.SpeakerFrame.panel,
        )
        self.GameChatFrame.panel.hide()
                                                
        self.GameParts = [
            Title(),
            GamePart_1(),
            ]
        for i in self.GameParts:
            i.Quit()
        
        self.NextPage()
        
    def Texting(self):
        if not self.CanChatting and self.ChatIndex < len(self.CurrentChat):
            if ((time := pygame.time.get_ticks())-self.lastTextingTick) / 1000 > self.TextSpeed:
                self.lastTextingTick = time
                self.ChatIndex += 1
                self.ChatTextlabel.set_text(self.CurrentChat[:self.ChatIndex+1])
                if (time - self.lastPlaytick) / 1000 > self.SoundTick * self.TextSpeed * random.randint(25,120):
                    self.lastPlaytick = time
                    self.TypeSound.play()
        else:
            self.CanChatting = True

            
    def Chatting(self,speaker="",text="",s=0.5,Sound=None,Animation=None):
        self.TextSpeed = s/(len(self.CurrentChat)+1)
        self.GameChatFrame.panel.show()
        self.ChatTextlabel.set_text(text)
        self.SpeakerName.set_text(speaker)
        self.SpeakerName.panel.show()
        if speaker == "":
            self.SpeakerFrame.panel.hide()
        elif speaker in self.GameParts[self.Part].Characters:
            print("d",speaker)
            self.AnimationType = Animation
            self.Speaker = self.GameParts[self.Part].Characters[speaker]
            self.Speaker.Show()
            
    def EndChatting(self):
        self.GameChatFrame.panel.hide()
        
    def Cycle(self,event):
        self.GameParts[self.Part].ButtonChecks(event)
        
    def TextingCycle(self):
        self.Texting()
    
    def KeyCycle(self,event):
        self.GameParts[self.Part].KeyChecks(event)
        
    def RepeatKeyCycle(self,keys):
        self.GameParts[self.Part].RepeatKeyChecks(keys)
        
    def NextPage(self):
        self.GameParts[self.Part].Quit()
        self.Part += 1
        self.GameParts[self.Part].Execute()
        
    def AnimationCycle(self):
        if not self.AnimationType is None:
            if self.AnimationType == "Idle":
                self.Speaker.Idle()
        