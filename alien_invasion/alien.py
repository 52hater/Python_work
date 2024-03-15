import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    """함대에 속한 외계인 하나를 나타내는 클래스"""

    def __init__(self, ai_game):
        """외계인을 초기화하고 시작 위치를 설정"""
        super().__init__()
        self.screen = ai_game.screen

        # 외계인  이미지를 불러와 rect속성 설정
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #외계인을 0,0 근처에 만듦
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #외계인의 가로위치 저장
        self.x = float(self.rect.x)
