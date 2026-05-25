import pygame
import GUI
import GameResource


class Character():
    def __init__(self,Name,Anim : dict):
        self.Name = Name
        self.Animations = {
            "IdleAnim" : Anim["Idle"],
            # "SpeakAnim" : [Anim["Speak"]],
        }
        self.AnimationTick = pygame.time.get_ticks()
        self.AnimationReloadTime = 0.1 # 막 정해본 기본 값임
        self.AnimationIndex = 0
        
        
        self.Image = GUI.ImageLabel(
            GameResource.UIManager,
            image_surface= pygame.image.load(r"assets\Hahaha.png"),
            size = (250,500),
            pos = (300,100),
            alpha=0,
            layer = 10,
        )
        self.Image.panel.hide()
        
    def Show(self):
        self.Image.panel.show()
    def Hide(self):
        self.Image.panel.hide()
        
    def Idle(self):
        if  ((time := pygame.time.get_ticks()) - self.AnimationTick)/1000 > self.AnimationReloadTime:
            self.AnimationTick = time
            self.Image.set_image(self.Animations["IdleAnim"][self.AnimationIndex],reset_size = False)
            self.AnimationIndex = (self.AnimationIndex + 1) if self.AnimationIndex < len(self.Animations["IdleAnim"]) -1 else 0
        