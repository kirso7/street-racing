import pygame
import random
from pygame.transform import scale
import time
import os

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        qqq = random.randint(1, 3)
        if qqq ==1:
            self.image = scale(pygame.image.load("car1.png"), (140, 280))
        if qqq == 2:
            self.image = scale(pygame.image.load("car3.png"), (140, 280))
        if qqq == 3:
            self.image = scale(pygame.image.load("car4.png"), (140, 280))
        self.rect = pygame.Rect(x, y, 140 , 280)
        self.yvel = level #####################

    def draw(self, screen):
        screen.blit(self.image , (self.rect.x, self.rect.y))

    def update(self):
        self.rect.y += self.yvel

        if self.rect.y > 900:
            self.kill()

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.rect = pygame.Rect(x, y, 140, 280)
        self.image = scale(pygame.image.load("car2.png"), (140, 280))
        self.xvel = 0
        # добавим кораблю здоровье
        self.life = 100

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    # добавим группу с астероидами в обновление координат корабля
    def update(self, left, right, asteroids):
        if left:
            self.xvel -= 2
            ''' if self.xvel < 0:
                 self.xvel = 0
            elif self.xvel > 1280:
                self.xvel = 1280'''


        if right:
            self.xvel += 2
            '''if self.xvel < 0:
                self.xvel = 0
            elif self.xvel > 1280:
                self.xvel = 1280'''



        if not (left or right):
            self.xvel = 0
        


        self.rect.x += self.xvel

        # для каждого астероида
        for asteroid in asteroids:
            # если область, занимаемая астероидом пересекает область корабля
            if self.rect.colliderect(asteroid.rect):
                # уменьшаем жизнь
                self.life -= 100

pygame.init()
screen = pygame.display.set_mode((1280, 1024))
pygame.display.set_caption("Asteroids")

sky = scale(pygame.image.load("road.png"), (1280, 1024))

ship = Spaceship(700, 400)

left = False
right = False

asteroids = pygame.sprite.Group()


####################
level = 15
####################



pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

while ship.life > 0:

    if random.randint(1, 1000) > 980:
        asteroid_x = random.randint(-100, 1300)
        asteroid_y = -100
        asteroid = Asteroid(asteroid_x, asteroid_y)
        asteroids.add(asteroid)

    for e in pygame.event.get():

        if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
            left = True
        if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
            right = True

        if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
            left = False
        if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
            right = False

        if e.type == pygame.QUIT:
            raise SystemExit("QUIT")

    screen.blit(sky, (0, 0))

    # добавим группу астероидов в параметры
    ship.update(left, right, asteroids)
    ship.draw(screen)

    for asteroid in asteroids:
        asteroid.update()
        asteroid.draw(screen)

    #life = font.render(f'HP: {ship.life}', False, (255, 255, 255))
    #screen.blit(life, (20, 20))

    pygame.display.update()
else:
    
    ''''time.sleep(10)
  scale(pygame.image.load("gameover.png"), (1280, 1024))
    time.delay'''