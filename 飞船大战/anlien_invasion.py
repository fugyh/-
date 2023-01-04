import sys
import pygame
from settings import Settings
from ship import Ship
import game_function as gf
def run_game():
    # 初始化创建屏幕对象
    pygame.init()
    # 实例化一个对象
    ai_settings=Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("alien invasion")
    # 设置背景色
    bg_color=(ai_settings.bg_color)
    # 创建一艘飞船
    ship=Ship(ai_settings,screen)

    # 开始主循环

    while True:
        # 监听事件
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship)
        # #加颜色
        # screen.fill(bg_color)
        # #加飞船
        # ship.blitme()
        # # 让绘制的屏幕可见
        # pygame.display.flip()
run_game()