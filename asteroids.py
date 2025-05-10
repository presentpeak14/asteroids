import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    containers = None  # This will be set in main.py
    
    def __init__(self, x, y, radius):
        # Call the parent's constructor with x, y, and radius
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        # Draw a circle on the screen at the asteroid's position with its radius
        # The width parameter should be 2 as per the assignment
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)
    
    def update(self, dt):
        # Update position based on velocity (which comes from CircleShape)
        self.position += self.velocity * dt