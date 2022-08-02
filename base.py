class Base():
    HEIGHT = 700
    def __init__(self, vel, img) -> None:
        self.vel = vel
        self.img = img
        self.y1 = 0
        self.y2 = -self.HEIGHT

    def move(self):
        self.y1 += self.vel
        self.y2 += self.vel
        if self.y1 > self.HEIGHT:
            self.y1 = self.y2 - self.HEIGHT

        if self.y2 > self.HEIGHT:
            self.y2 = self.y1 - self.HEIGHT

    def draw(self, win):
        win.blit(self.img, (0, self.y1))
        win.blit(self.img, (0, self.y2))

    def update_speed(self, vel):
        self.vel = vel