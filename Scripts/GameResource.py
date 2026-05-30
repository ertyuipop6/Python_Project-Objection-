import pygame
import pygame_gui
import GameData

ScreenSize = None
screen = None
Clock = None
Font_1 = None
UIManager = None
Running = None
Title = None
GameController = None
GameTextJsonData = None
GameParts = None

def ChangeColorToInt(string):
    string : str = string
    string = string.lstrip("#")
    
    return (int(string[0:2], 16) , int(string[2:4], 16), int(string[4:6], 16))
