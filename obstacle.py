from random import randrange

import pygame

class Obstacle():
    MAX_Y = 800
    MID = 250
    OFFSET = 130
    IMG_WIDTH = 20

    def __init__(self, vel, img) -> None:
        self.vel = vel
        self.y  = -20
        self.x = self.MID + randrange(-1, 2, 1) * self.OFFSET - self.IMG_WIDTH
        self.img = img
        self.passed = False

    def move(self):
        self.y += self.vel
        if self.y > self.MAX_Y:
            self.passed = True

    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

    def collide(self, player):
        player_mask = player.get_mask()
        mask = pygame.mask.from_surface(self.img)
        offset = (self.x - player.x, self.y - player.y)
        if player_mask.overlap(mask, offset):
            return True
        return False

    def update_speed(self, vel):
        self.vel = vel