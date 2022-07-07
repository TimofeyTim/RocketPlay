#Создай собственный Шутер!
from random import randint
from pygame import *
mixer.init()
mixer.music.load('space.ogg')
mixer.music.set_volume(0.05)
mixer.music.play()
kick = mixer.Sound('fire.ogg')
kick.set_volume(0.5)
win = display.set_mode((1600,900),FULLSCREEN)#создание окна приложения 
display.set_caption('стрелять в инопланетян и решать междупланетные конфликты.не онлайн')
background = transform.scale(
    image.load('galaxy.jpg'),(1600,900)
)
#RESIZABLE
class obTverdiyznaKekt(sprite.Sprite):
    def __init__(self,x,y,img,w,h,speed):
        super().__init__()
        self.image = transform.scale(image.load(img),(w,h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        win.blit(self.image,(self.rect.x,self.rect.y))


class ForPulya(obTverdiyznaKekt):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
              
            self.kill()

Pulii = sprite.Group()

class ForPlayer(obTverdiyznaKekt):
    def move(self):
        key_pressed = key.get_pressed()
        
        if key_pressed[K_d] and self.rect.x < 1500:
            self.rect.x += 10
        if key_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= 10
    def fire(self):
        bullet = ForPulya(self.rect.centerx,self.rect.top,'bullet.png',32,64,22)
        Pulii.add(bullet)
player1 = ForPlayer(750,750,'rocket.png',100,100,10)

class ForEnemy(obTverdiyznaKekt):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= 900:
            self.rect.y = 0
            self.rect.x = randint(0,1500)
Enemys = sprite.Group()

   
EnemyOdin = ForEnemy( randint(0,1500),0,'ufo.png',160,80,randint(3,7))
EnemyBob = ForEnemy( randint(0,1500),0,'ufo.png',160,80,randint(3,7))
EnemyTor = ForEnemy( randint(0,1500),0,'ufo.png',160,80,randint(3,7))
EnemyTom = ForEnemy( randint(0,1500),0,'ufo.png',160,80,randint(3,7))
EnemyGarry = ForEnemy( randint(0,1500),0,'ufo.png',160,80,randint(3,7))
Enemys.add(EnemyOdin)
Enemys.add(EnemyBob)
Enemys.add(EnemyTor)
Enemys.add(EnemyTom)
Enemys.add(EnemyGarry)


font.init()
shrift = font.SysFont('Franklin Gothic',150)
gameOver = shrift.render('game over!',True,(118, 0, 0))
fps = 144#игрвовой цикл
clock = time.Clock()
game = True
finish = False
while game == True:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                player1.fire()

                kick.play()
                
    win.blit(background,(0,0))
        
    


    if finish != True:
        player1.reset()
        player1.move()
        Enemys.draw(win)
        Enemys.update()
        Pulii.draw(win)
        Pulii.update()
        if sprite.spritecollide(player1,Enemys,False):
            finish = True
        if sprite.groupcollide(Pulii,Enemys,True,True):
            monster = ForEnemy( randint(0,1500),0,'ufo.png',160,80,randint(3,7))
            Enemys.add(monster)

           
    else:
        player1.reset()
        Enemys.draw(win)
        win.blit(gameOver,(500,400))
        key_pressed = key.get_pressed()
        if key_pressed[K_SPACE]:
            finish = False
            player1 = ForPlayer(750,750,'rocket.png',100,100,10)
            EnemyOdin.remove()
            EnemyTor.remove()
            EnemyTom.remove()
            EnemyGarry.remove()
            EnemyBob.remove()               
            EnemyOdin = ForEnemy( randint(0,1500),0,'ufo.png',160,80,randint(3,7))
            EnemyBob = ForEnemy( randint(0,1500),0,'ufo.png',160,80,randint(3,7))
            EnemyTor = ForEnemy( randint(0,1500),0,'ufo.png',160,80,randint(3,7))
            EnemyTom = ForEnemy( randint(0,1500),0,'ufo.png',160,80,randint(3,7))
            EnemyGarry = ForEnemy( randint(0,1500),0,'ufo.png',160,80,randint(3,7))
            Enemys.add(EnemyOdin)
            Enemys.add(EnemyBob)
            Enemys.add(EnemyTor)
            Enemys.add(EnemyTom)
            Enemys.add(EnemyGarry)

            
            
            

    display.update()
    clock.tick(fps)


#добавить перезапуск игры по кнопке
#добавить надпись game over
#лабиринт


    

