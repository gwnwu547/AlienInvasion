import pygame

class Ship:
    """管理飞船的类"""
    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp') # pygame.image.load()返回了一个表示飞船的surface
        self.rect = self.image.get_rect() #调用get_rect()获取相应surface的属性rect

        # 每艘飞船都放在屏幕的底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """在制定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)