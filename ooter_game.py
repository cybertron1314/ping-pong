from pygame import *
from random import randint
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_y, player_x, player_speed, size):
        super().__init__()
        self.image = transform.scale(image.load(player_image), size)
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.y = player_y
        self.rect.x = player_x
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_d] and self.rect.x < 700 - self.rect.width - 5:
            self.rect.x += self.speed
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
    def fire(self):
        pass

window = display.set_mode((700, 500))
display.set_caption('Шутер')
mixer.init()
mixer.music.load('space.ogg')
mixer.music.set_volume(0.20)
mixer.music.play()


clock = time.Clock()
FPS = 60
run = True
finish = False


    window.blit(background,(0, 0))
    draw_lost(lost)
    draw_score(0)
    if not finish:
    
    display.update() 
    clock.tick(60)
