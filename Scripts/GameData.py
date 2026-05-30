import pygame
import GUI
import GameResource
import random

import GameParts



## 매우 중요
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
        
        self.RepeatCount = 0
        self.AnimationType = None
        self.Speaker = None
        
        # 단순 UI

        self.GameChatFrame = GUI.Frame(
            manager = GameResource.UIManager,
            pos = (0,550),
            size = (GameResource.ScreenSize[0],350),
            bg_color = (60,60,60),
            alpha= 0,
            layer = 10,
        )
        self.ChatWindow = GUI.ImageLabel(
            manager = GameResource.UIManager,
            pos = (5,50),
            size = (GameResource.ScreenSize[0]+10,250),
            bg_color = (60,60,60),
            alpha= 255,
            image_surface= pygame.image.load(r"Assets\UiResource\ChatWindow.png"),
            Parent=self.GameChatFrame.panel,
        )
        self.ChatTextlabel = GUI.TextLabel(
            manager = GameResource.UIManager,
            pos = (GameResource.ScreenSize[0]//4-50,20),
            size = (GameResource.ScreenSize[0]//2+200,260),
            text = "아니 세상에 자기가 노인이라는 사람인데 키설정을 했대 인제 처음하는건가봐",
            font_size= 7,
            bg_color = (60,60,60),
            alpha= 0,
            layer = 5,
            align_horiz='left',
            align_vert='top',
            Parent= self.ChatWindow.panel,
        )
        self.SpeakerFrame = GUI.ImageLabel(
            manager = GameResource.UIManager,
            pos = (125,30),
            size = (225,50),
            bg_color = GameResource.ChangeColorToInt("#FF0000"),
            alpha= 0,
            image_surface=pygame.image.load(r"Assets\UiResource\SpeakerName.png"),
            layer=5,
            Parent= self.GameChatFrame.panel,
        )
        self.SpeakerName = GUI.TextLabel(
                        manager = GameResource.UIManager,
            pos = (0,0),
            size = (225,50),
            bg_color = GameResource.ChangeColorToInt("#0099FF"),
            text = "즌다몬",
            font_size= 6,
            alpha= 0,
            Parent= self.SpeakerFrame.panel,
        )

        # 초기화
        self.GameChatFrame.panel.hide()
                                                
        self.GameParts = GameResource.GameParts
        
        for i in self.GameParts:
            i.Quit()
        
        self.NextPage()
    
    def EventCycle(self,event):
        '''한 프레임에 입력된 이벤트들을 검사하는 함수'''
        self.GameParts[self.Part].ButtonChecks(event) # UI 버튼 이벤트 체크
        self.GameParts[self.Part].KeyChecks(event)

    def MainCycle(self,keys):
        '''한 프레임 당 한 번만 도는 사이클'''
        self.GameParts[self.Part].RepeatKeyChecks(keys)
        self.Texting()
    #     self.AnimationCycle()

    def AnimationCycle(self):
        
        if not self.AnimationType is None:
            if self.RepeatCount == 0:
                self.AnimationType = None
            elif self.RepeatCount == -1:
                if self.AnimationType == "Idle":
                    self.Speaker.Idle()
            else:
                if self.AnimationType == "Idle":
                    self.Speaker.Idle()

    def Texting(self): 
        '''현재 읽는 텍스트 검사 함수'''
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

            
    def Chatting(self,speaker="",text="",s=1.5,Sound=None,Animation=None,RepeatCount=1):
        '''텍스트 전달 받는 함수'''
        self.TextSpeed = s/(len(self.CurrentChat)+1)
        self.GameChatFrame.panel.show()
        self.ChatTextlabel.set_text(text)
        self.SpeakerName.set_text(speaker)
        self.SpeakerName.panel.show()
        if speaker == "":
            self.SpeakerFrame.panel.hide()
        elif speaker in self.GameParts[self.Part].Characters:
            self.AnimationType = Animation
            self.RepeatCount = RepeatCount
            self.Speaker = self.GameParts[self.Part].Characters[speaker]
            self.Speaker.Show()
            
    def CloseChatWindow(self):
        '''채팅 창 닫는 함수'''
        self.GameChatFrame.panel.hide()

    def NextPage(self):
        '''다음 챕터로 넘어가는 함수'''
        self.GameParts[self.Part].Quit()
        self.Part += 1
        self.GameParts[self.Part].Execute()


