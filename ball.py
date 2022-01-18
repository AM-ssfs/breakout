import pygame



class Ball(pygame.sprite.Sprite):

    def __init__(self, color, windowWidth, windowHeight, radius):
        # initialize sprite super class
        super().__init__()

        # finish setting the class variables to the parameters
        self.color = color

        # Create a surface, get the rect coordinates, fill the surface with a white color (or whatever color the
        # background of your breakout game will be.
        self.image = pygame.Surface((10, 10))
        self.image.fill(color)
        self.rect = self.image.get_rect()

        # Add a circle to represent the ball to the surface just created. Just use the pygame.draw.circle method.
        # The surface will be self.image
#        pygame.draw.rect(self.image, self.rect, ())

        # Give the ball an initial speed. You will need a speed for the x direction and one for the y direction.
        self.window_width = windowWidth
        self.window_height = windowHeight

    speed_x = 2
    speed_y = 5

    def move(self):
        if self.rect.x > self.window_width-10:
            self.speed_x = -self.speed_x
        if self.rect.x < 0:
            self.speed_x = -self.speed_x
        if self.rect.y > self.window_height-10:
            self.speed_y = -self.speed_y
        if self.rect.y < 0:
            self.speed_y = -self.speed_y

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def collide_brick(self, bricks):
        if pygame.sprite.spritecollide(self, bricks, True):
            self.speed_y = -self.speed_y

    def collide_paddle(self, paddle):
        if pygame.sprite.spritecollide(self, paddle, False):
            self.speed_y = -self.speed_y
