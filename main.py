import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()  # Plural form as per assignment
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    # Set containers for Player
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Set containers for Asteroid
    Asteroid.containers = (asteroids, updatable, drawable)  # Needs to be a tuple with all three groups

    # Set containers for AsteroidField (only updatable)
    AsteroidField.containers = (updatable,)  # Note the comma to make this a tuple

    # Create the asteroid field
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        for entity in drawable:
            entity.draw(screen)
        dt = clock.tick(60) / 1000        # limit the framerate to 60 FPS
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
        pygame.display.flip()




if __name__ == "__main__":
    main()
