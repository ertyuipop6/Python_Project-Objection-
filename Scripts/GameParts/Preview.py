import pygame
import GUI
import GameResource
import GameCharacter
from .GamePartClass import GamePart

class Preview(GamePart):
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
                
                GameResource.GameController.CurrentChat = "  "+ ChatData["Chat"]
                Animation = None if not "Anim" in ChatData else ChatData["Anim"]
                Repeat = 1 if not "RepeatCount" in ChatData else ChatData["RepeatCount"]
                    
                GameResource.GameController.Chatting(ChatData["Speaker"],ChatData["Chat"][GameResource.GameController.ChatIndex],Animation=Animation,RepeatCount= Repeat)
                
                
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