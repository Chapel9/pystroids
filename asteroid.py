import pygame
import random
from circleshape import CircleShape
from logger import log_event
from constants import *



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
       
    def split(self):
        
        if (self.radius <= ASTEROID_MIN_RADIUS):
            self.kill()
            return
        if (self.radius > ASTEROID_MIN_RADIUS):
            from asteroidfield import AsteroidField
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            new_ast_1 = self.velocity.rotate(angle)
            new_ast_2 = self.velocity.rotate(-angle)
            new_ast_radius = self.radius - ASTEROID_MIN_RADIUS
            new_vel = self.velocity * 1.2
            AsteroidField.spawn(self, new_ast_radius, new_ast_1, new_vel)
            AsteroidField.spawn(self, new_ast_radius, new_ast_2, new_vel)
            self.kill()
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)