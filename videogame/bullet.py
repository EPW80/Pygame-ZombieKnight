""" This is the bullet file for the project."""

import pygame


class Bullet(pygame.sprite.Sprite): # pylint: disable=too-few-public-methods
    """A projectile launched by the player"""

    # Load image once rather than in each instance
    IMAGE = pygame.image.load("images/player/slash.png")

    def __init__(self, x, y, bullet_group, player):  # pylint: disable=invalid-name
        """Initialize the bullet"""
        super().__init__()

        # Set constant variables
        self.VELOCITY = 20  # pylint: disable=invalid-name
        self.RANGE = 500  # pylint: disable=invalid-name

        # Determine the image to use
        if player.velocity.x > 0:
            self.image = pygame.transform.scale(self.IMAGE, (32, 32))
        else:
            self.image = pygame.transform.scale(
                pygame.transform.flip(self.IMAGE, True, False),
                (32, 32),
            )
            self.VELOCITY = -self.VELOCITY

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.starting_x = x

        bullet_group.add(self)

    def update(self):
        """Update the bullet"""
        self.rect.x += self.VELOCITY

        # If the bullet has passed the range, kill it
        if abs(self.rect.x - self.starting_x) > self.RANGE:
            self.kill()
