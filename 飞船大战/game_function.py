import sys
import pygame


def check_keydown_events(event, ship):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    """响应按键和鼠标"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RIGHT:
        #         # 飞船右移动
        #         ship.rect.centerx += 1
        elif event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_RIGHT:
            #     ship.moving_right = True
            # elif event.key == pygame.K_LEFT:
            #     ship.moving_left=True
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            # if event.key == pygame.K_RIGHT:
            #     ship.moving_right = False
            # elif event.key==pygame.K_LEFT:
            #     ship.moving_left=False
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship):
    """更新屏幕,传入的分别是屏幕颜色\屏幕\飞船"""
    # 每次循环都会绘制屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # 让绘制的屏幕可见
    pygame.display.flip()
