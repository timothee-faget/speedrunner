import pygame


class Player():
    """
    Player that moves left and right to avoid obstacles
    """
    MAX_SPEED = 10
    MAX_X = 200
    INERTIA = 2
    IMG_WIDTH = 20

    OFFSET = 130
    MOVE_SPEED = OFFSET/10 # px per ticks

    def __init__(self, img, x, y) -> None:
        self.x_init = x  - self.IMG_WIDTH
        self.x = x  - self.IMG_WIDTH
        self.y = y
        self.state = 0
        self.is_moving = False
        self.vel = 0
        self.img = img
        self.score = 0

    def move(self):
        displacement = self.vel
        self.x += displacement

        target_pos = self.x_init + self.state * self.OFFSET
        # print(f"Target : {target_pos}; x : {self.x}; state : {self.state}")
        if target_pos == self.x:
            self.is_moving = False

    def set_state(self, side='None'):
        if not self.is_moving:
            if side == 'Left':
                self.state -= 1
                self.is_moving = True
                if self.state < -1:
                    self.state = -1
            if side == 'Right':
                self.state += 1
                self.is_moving = True
                if self.state > 1:
                    self.state = 1

    def set_speed(self):
        """
        sets player speed
        """
        if self.is_moving:
            target_pos = self.x_init + self.state * self.OFFSET
            if (self.x - target_pos) > 0:
                self.vel = -self.MOVE_SPEED
            else:
                self.vel = self.MOVE_SPEED
        else:
            self.vel = 0

    def draw(self, win):
        # print(f"Player: x:{self.x}, y:{self.y}, v:{self.vel}, s:{self.state}")
        win.blit(self.img, (self.x, self.y))

    def get_mask(self):
        return pygame.mask.from_surface(self.img)