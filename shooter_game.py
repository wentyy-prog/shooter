#Создай собственный Шутер!
from random import *
from pygame import *
from time import time as time_reload
init()
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,player_size_x,player_size_y):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(player_size_x,player_size_y))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update(self):
        keys=key.get_pressed()
        if keys[K_d]:
            self.rect.x += self.speed
        if keys[K_a]:
            self.rect.x -= self.speed
    def fire(self):
        bullt=Bullet('bullet.png',self.rect.centerx-10,self.rect.top,5,20,20)
        bullet.add(bullt)

class Ufo(GameSprite):
    def update(self):
        global ls
        global text_lose
        self.rect.y += self.speed
        if self.rect.y >500:
            self.rect.x=randint(10,670)
            self.rect.y=0
            ls+=1
            text_lose=font1.render("Пропущено: "+str(ls),1,(243,17,13))
class Bullet(GameSprite):
    def update(self):
        self.rect.y -=self.speed
        if self.rect.y<-5:
            self.kill()
class Asteroid(GameSprite):
    def update(self):
        self.rect.y+=self.speed
        if self.rect.y >500:
            self.rect.x=randint(10,670)
            self.rect.y=0

bullet=sprite.Group()
asteroid=sprite.Group()

window=display.set_mode((700,500))
display.set_caption('Шутер')
background=transform.scale(image.load('galaxy.jpg'),(700,500))

wn=0
font1=font.SysFont('Arial',35)
text_win=font1.render("Счёт: "+str(wn),1,(0,209,13))

ls=0
text_lose=font1.render("Пропущено: "+str(ls),1,(243,17,13))


player=Player('rocket.png',200,400,2,50,50)
ufo=Ufo('ufo.png',randint(10,650),randint(10,60),randint(1,3),40,40)
ufo1=Ufo('ufo.png',randint(10,650),randint(10,60),randint(1,3),40,40)
ufo2=Ufo('ufo.png',randint(10,650),randint(10,60),randint(1,3),40,40)
ufo3=Ufo('ufo.png',randint(10,650),randint(10,60),randint(1,3),40,40)
ufo4=Ufo('ufo.png',randint(10,650),randint(10,60),randint(1,3),40,40)

asteroid1=Asteroid('asteroid.png',randint(10,650),randint(10,60),randint(1,2),randint(20,50),randint(40,70))
asteroid2=Asteroid('asteroid.png',randint(10,650),randint(10,60),randint(1,2),randint(20,50),randint(40,70))
asteroid3=Asteroid('asteroid.png',randint(10,650),randint(10,60),randint(1,2),randint(20,50),randint(40,70))

asteroid.add(asteroid1)
asteroid.add(asteroid2)
asteroid.add(asteroid3)

lf=3
life=font1.render('Жизни: '+str(lf),1,(20,145,86))


font=font.SysFont('Arial',100)
win=font.render("YOU WIN!",True,(0,255,0))
lose=font.render("YOU LOSE!",True,(255,0,0))
reload_time=font1.render('Wait reload',True,(255,41,50))
monsters=sprite.Group()
monsters.add(ufo)
monsters.add(ufo1)
monsters.add(ufo2)
monsters.add(ufo3)
monsters.add(ufo4)

clock=time.Clock()
FPS=60

mixer.music.load('space.ogg')
mixer.music.set_volume(0.3)
mixer.music.play()

fire=mixer.Sound('fire.ogg')

num_fire=0
rel_time=False
count_win=0
finish=False
game=True
while game:
    for e in event.get():
        if e.type==QUIT:
            game=False
        if e.type==KEYDOWN:
            if e.key==K_SPACE:
                if num_fire<5 and rel_time==False:
                    player.fire()
                    fire.play()
                    num_fire+=1
                if num_fire>=5 and rel_time==False:
                    rel_time=True
                    time_start=time_reload()
            if e.key==K_r:
                bullet.empty()
                monsters.empty()
                mixer.music.play()
                finish=False
                ufo=Ufo('ufo.png',randint(10,650),randint(10,60),randint(1,3),40,40)
                ufo1=Ufo('ufo.png',randint(10,650),randint(10,60),randint(1,3),40,40)
                ufo2=Ufo('ufo.png',randint(10,650),randint(10,60),randint(1,3),40,40)
                ufo3=Ufo('ufo.png',randint(10,650),randint(10,60),randint(1,3),40,40)
                ufo4=Ufo('ufo.png',randint(10,650),randint(10,60),randint(1,3),40,40)
                monsters.add(ufo)
                monsters.add(ufo1)
                monsters.add(ufo2)
                monsters.add(ufo3)
                monsters.add(ufo4)
                count_win=0
                ls=0
                lf=3
                text_win=font1.render("Счёт: "+str(count_win),1,(0,209,13))
                text_lose=font1.render("Пропущено: "+str(ls),1,(243,17,13))
                life=font1.render('Жизни: '+str(lf),1,(20,145,86))
    if finish !=True:
        window.blit(background,(0,0))
        
        window.blit(text_win,(10,10))
        window.blit(text_lose,(10,40))
        window.blit(life,(570,20))
        asteroid.draw(window)
        asteroid.update()
        player.reset()
        player.update()
        monsters.draw(window)
        monsters.update()
        bullet.draw(window)
        bullet.update()
        collides=sprite.groupcollide(monsters, bullet, True, True)
        sprite_collides=sprite.spritecollide(player,monsters,False)
        sprite_asteroid=sprite.spritecollide(player,asteroid,True)
        if sprite_collides:
            window.blit(lose,(150,200))
            finish=True
            mixer.music.stop()
        
        if sprite_asteroid:
            asteroid_random=Asteroid('asteroid.png',randint(10,650),randint(10,60),randint(1,2),randint(20,50),randint(40,70))
            asteroid.add(asteroid_random)
            lf-=1
            life=font1.render('Жизни: '+str(lf),1,(20,145,86))

        for SPRITE in collides:
            count_win+=1
            ufo_random=Ufo('ufo.png',randint(10,700),100,randint(1,3),40,40)
            monsters.add(ufo_random)
            text_win=font1.render("Счёт: "+str(count_win),1,(0,209,13))
        if count_win >= 10:
            window.blit(win,(150,200))
            finish=True
            mixer.music.stop()
        if ls >=3:
            window.blit(lose,(150,200))
            finish=True
            mixer.music.stop()
        if lf <=0:
            window.blit(lose,(150,200))
            finish=True
            mixer.music.stop()
        if rel_time==True:
            time_end=time_reload()
            if time_end-time_start <=3:
                window.blit(reload_time,(250,460))


        display.update()
        clock.tick(FPS)