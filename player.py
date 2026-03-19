import pygame
from circleshape import CircleShape
from shot import Shot
from constants import *

class Player(CircleShape):
    def __init__(self, x, y, *groups):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
        
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)
    
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def shoot(self,dt):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        bullet = Shot(self.position.x, self.position.y)
        bullet.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOT_SPEED
        

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shoot_timer -= dt

        if keys[pygame.K_a] or keys[pygame.k_LEFT]:
            self.rotate(-dt)

        if keys[pygame.K_d] or keys[pygame.k_RIGHT]:
            self.rotate(dt)
        
        if keys[pygame.K_w] or keys[pygame.k_UP]:
            self.move(dt)

        if keys[pygame.K_s] or keys[pygame.k_DOWN]:
            self.move(-dt)
        
        if keys[pygame.K_SPACE]:
            self.shoot(dt)


    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

