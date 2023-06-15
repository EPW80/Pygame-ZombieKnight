"""This is the ruby file for the project."""

import random
import pygame

vector = pygame.math.Vector2  # pylint: disable=invalid-name

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 736


class Ruby(pygame.sprite.Sprite):
    """A class the player must collect to earn points and health"""

    def __init__(self, platform_group, portal_group):
        """Initialize the ruby"""
        super().__init__()

        # Set constant variables
        self.VERTICAL_ACCELERATION = 3  # pylint: disable=invalid-name
        self.HORIZONTAL_VELOCITY = 5  # pylint: disable=invalid-name

        # Animation frames
        self.ruby_sprites = []

        # Rotating
        self.ruby_sprites.append(
            pygame.transform.scale(
                pygame.image.load("images/ruby/tile000.png"), (64, 64)
            )
        )
        self.ruby_sprites.append(
            pygame.transform.scale(
                pygame.image.load("images/ruby/tile001.png"), (64, 64)
            )
        )
        self.ruby_sprites.append(
            pygame.transform.scale(
                pygame.image.load("images/ruby/tile002.png"), (64, 64)
            )
        )
        self.ruby_sprites.append(
            pygame.transform.scale(
                pygame.image.load("images/ruby/tile003.png"), (64, 64)
            )
        )
        self.ruby_sprites.append(
            pygame.transform.scale(
                pygame.image.load("images/ruby/tile004.png"), (64, 64)
            )
        )
        self.ruby_sprites.append(
            pygame.transform.scale(
                pygame.image.load("images/ruby/tile005.png"), (64, 64)
            )
        )
        self.ruby_sprites.append(
            pygame.transform.scale(
                pygame.image.load("images/ruby/tile006.png"), (64, 64)
            )
        )

        # Load image and get rect
        self.current_sprite = 0
        self.image = self.ruby_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (WINDOW_WIDTH // 2, 100)

        # Attach sprite groups
        self.platform_group = platform_group
        self.portal_group = portal_group

        # Load sounds
        self.portal_sound = pygame.mixer.Sound("sounds/portal_sound.wav")

        # Kinematic vectors
        self.position = vector(self.rect.x, self.rect.y)
        self.velocity = vector(
            random.choice([-1 * self.HORIZONTAL_VELOCITY, self.HORIZONTAL_VELOCITY]), 0
        )
        self.acceleration = vector(0, self.VERTICAL_ACCELERATION)

    def update(self):
        """Update the ruby"""
        self.animate(self.ruby_sprites, 0.25)
        self.move()
        self.check_collisions()

    def move(self):
        """Move the ruby"""
        # We don't need to update the accelreation vector because it never changes here

        # Calculate new kinematics values: (4, 1) + (2, 8) = (6, 9)
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5 * self.acceleration

        # Update rect based on kinematic calculations and add wrap around movement
        if self.position.x < 0:
            self.position.x = WINDOW_WIDTH
        elif self.position.x > WINDOW_WIDTH:
            self.position.x = 0

        self.rect.bottomleft = self.position

    def check_collisions(self):
        """Check for collisions with platforms and portals"""
        # Collision check between ruby and platforms when falling
        collided_platforms = pygame.sprite.spritecollide(
            self, self.platform_group, False
        )
        if collided_platforms:
            self.position.y = collided_platforms[0].rect.top + 1
            self.velocity.y = 0

        # Collision check for portals
        if pygame.sprite.spritecollide(self, self.portal_group, False):
            self.portal_sound.play()
            # Determine which portal you are moving to
            # Left and right
            if self.position.x > WINDOW_WIDTH // 2:
                self.position.x = 86
            else:
                self.position.x = WINDOW_WIDTH - 150
            # Top and bottom
            if self.position.y > WINDOW_HEIGHT // 2:
                self.position.y = 64
            else:
                self.position.y = WINDOW_HEIGHT - 132

            self.rect.bottomleft = self.position

    def animate(self, sprite_list, speed):
        """Animate the ruby"""
        if self.current_sprite < len(sprite_list) - 1:
            self.current_sprite += speed
        else:
            self.current_sprite = 0

        self.image = sprite_list[int(self.current_sprite)]
