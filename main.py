import sys
import pygame
from asteroidfield import AsteroidField
from asteroid import Asteroid
from logger import log_state, log_event
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids,updatable, drawable)
    AsteroidField.containers = (updatable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for object in drawable:
            object.draw(screen)
        for object in updatable:
            object.update(dt)
        for object in asteroids:
            if object.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
