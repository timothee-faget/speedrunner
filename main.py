# Imports
from operator import index
import pygame
import os
pygame.font.init()  # init font

from player import Player
from obstacle import Obstacle
from base import Base

# Constants

WIN_WIDTH = 500
WIN_HEIGHT = 700
X_INIT = WIN_WIDTH/2
Y_INIT = 600

MOVE_SPEED = 5

FONT = pygame.font.SysFont("comicsans", 30)

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Speed Runner")

player_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","player.png")).convert_alpha())
bg_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bg.png")).convert_alpha())
obs_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","obs_1.png")).convert_alpha())

def draw_window(win, base, player, obstacles, debug, keys=[]):
    base.draw(win)
    player.draw(win)
    for obs in obstacles:
        obs.draw(win)
    draw_score(player.score, win)
    if debug:
        pos_label = FONT.render(f"Pos: {player.x}",1,(255,0,0))
        win.blit(pos_label, (15, 10))
        vel_label = FONT.render(f"Vel: {player.vel}",1,(255,0,0))
        win.blit(vel_label, (15, 30))
        state_label = FONT.render(f"State: {player.state}",1,(255,0,0))
        win.blit(state_label, (15, 50))
        moving_label = FONT.render(f"State: {player.is_moving}",1,(255,0,0))
        win.blit(moving_label, (15, 70))
        if len(keys)!=0:
            i = 0
            for key in keys:
                key_label = FONT.render(f"Key: {key}",1,(255,0,0))
                win.blit(key_label, (15, 70+i*20))
                i += 1
    pygame.display.update()

def draw_score(score, win):
    score_label = FONT.render(f"Score: {score}",1,(100,100,100))
    win.blit(score_label, (15, 10))

def run_game():
    global WIN

    player = Player(player_img, X_INIT, Y_INIT)
    
    move_speed = MOVE_SPEED
    move_speed_int = int(move_speed)

    base = Base(move_speed_int, bg_img)

    obstacles = [Obstacle(move_speed_int, obs_img)]

    clock = pygame.time.Clock()

    run = True
    debug = False
    while run:
        clock.tick(60)

        base.move()
        base.update_speed(move_speed_int)
        # keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.set_state('Left')
                if event.key == pygame.K_RIGHT:
                    player.set_state('Right')
            
        player.set_speed()
        player.move()

        for obstacle in obstacles:
            obstacle.move()

            if obstacle.collide(player):
                run = False
                print(player.score)
                break

            if obstacle.passed:
                player.score += 1
                obstacles.pop(obstacles.index(obstacle))
                obstacles.append(Obstacle(move_speed_int, obs_img))

            obstacle.update_speed(move_speed_int)

        # if not obstacles:
        #     print('adding obstacle')
        #     obstacles.append(Obstacle(5, obs_img))
        move_speed += 0.001
        move_speed_int = int(move_speed)
        draw_window(WIN, base, player, obstacles, debug)
    
    print('GAME OVER')

if __name__ == "__main__":
    run_game()