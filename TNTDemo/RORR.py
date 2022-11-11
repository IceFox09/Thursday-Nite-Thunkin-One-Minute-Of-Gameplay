import pygame as walnut

walnut.init()
x, y = (1024, 576)
screen = walnut.display.set_mode((x, y))
walnut.display.set_caption("Revenge Of Richie Rich")
richbg = walnut.transform.scale(walnut.image.load("RichieRich.jpg"),(x*1.5,y*1.5))
bgrect = richbg.get_rect()
jumpxtwo = walnut.transform.scale(walnut.image.load("DoubleJump.png"),(130,50))
spikeblock = walnut.transform.scale(walnut.image.load("Spike.png"),(35,35))
antigrav = walnut.transform.scale(walnut.image.load("antigrav.png"),(200,60))
icecream = walnut.transform.scale(walnut.image.load("IceCreamShackAgain.png"),(180,200))
cardboard = walnut.transform.scale(walnut.image.load("Level4Part1End.JPG"), (1024, 576))
purpplattutorial = walnut.transform.scale(walnut.image.load("PPT.png"), (180,180))
money = walnut.image.load("MoneyByPinkFloyd.png")
walnut.mixer.music.load("PlatformingParadiseFish.mp3")
death = walnut.mixer.Sound("DeathSound.wav")
complete = walnut.mixer.Sound("Left_Arrow.mp3")
walnut.mixer.music.set_volume(0.6)
death.set_volume(0.6)
complete.set_volume(0.6)
walnut.display.set_icon(money)
walnut.mixer.music.play(-1)
finish = walnut.Rect(725, 220, 20, 20)
clock = walnut.time.Clock()
spike = walnut.surface.Surface((50,50))
finished = False
class Player(walnut.sprite.Sprite):
    def __init__(self):
        walnut.sprite.Sprite.__init__(self)
        self.image = walnut.image.load("JB_I.png")
        self.image = walnut.transform.scale(self.image, (50, 60))
        self.rect = self.image.get_rect(bottomleft=rect1.rect.topleft)
        self.rect.y -= 1
        self.ng = True  # normal gravity
        self.jumps = 2
        self.jumptime = 0
        self.speed = 5
        self.right = True
        self.landed = True
    def update(self):
        keys = walnut.key.get_pressed()
        if keys[walnut.K_a] or keys[walnut.K_LEFT]:
            self.right = False
            touchingpurple = walnut.sprite.spritecollide(self,purpleplatforms,False,walnut.sprite.collide_rect_ratio(1.1))
            if not touchingpurple:
                self.rect.x -= self.speed
            touching = walnut.sprite.spritecollide(self, platforms, False, walnut.sprite.collide_rect)
            if touching:
                self.rect.x = touching[0].rect.right
            touchingspike = walnut.sprite.spritecollide(self,spikeblocks,False,walnut.sprite.collide_rect_ratio(1.1))
            if touchingspike:
                death.play(0)
                player.rect.bottomleft = (80, 400)
                player.ng = True
        if keys[walnut.K_f] or keys[walnut.K_RIGHT] or keys[walnut.K_d]:
            self.right = True
            touchingpurple = walnut.sprite.spritecollide(self,purpleplatforms,False,walnut.sprite.collide_rect_ratio(1.1))
            if not touchingpurple:
                self.rect.x += self.speed
            touching = walnut.sprite.spritecollide(self, platforms, False, walnut.sprite.collide_rect)
            if touching:
                self.rect.right = touching[0].rect.left
            touchingspike = walnut.sprite.spritecollide(self, spikeblocks, False, walnut.sprite.collide_rect_ratio(1.1))
            if touchingspike:
                death.play(0)
                player.rect.bottomleft = (80, 400)
                player.ng = True
        if self.jumptime:
            self.landed = False
            if not self.ng:
                self.rect.y += self.speed
                touching = walnut.sprite.spritecollide(self, platforms, False, walnut.sprite.collide_rect)
                if touching:
                    self.rect.bottom = touching[0].rect.top
                    self.jumptime = 1
            else:
                self.rect.y -= self.speed
                touching = walnut.sprite.spritecollide(self, platforms, False, walnut.sprite.collide_rect)
                if touching:
                    self.rect.top = touching[0].rect.bottom
                    self.jumptime = 1
            self.jumptime -= 1
        else:
            self.landed = False
            if not self.ng:
                self.rect.y -= 10
                touching = walnut.sprite.spritecollide(self, platforms, False, walnut.sprite.collide_rect)
                if touching:
                    self.rect.top = touching[0].rect.bottom
                    self.landed = True
            else:
                self.rect.y += 10
                touching = walnut.sprite.spritecollide(self, platforms, False, walnut.sprite.collide_rect)
                if touching:
                    self.rect.bottom = touching[0].rect.top
                    self.landed = True
        if self.landed:
            self.jumps = 2
            touchingspike = walnut.sprite.spritecollide(self, spikeblocks, False, walnut.sprite.collide_rect_ratio(1.1))
            if touchingspike:
                death.play(0)
                player.rect.bottomleft = (80, 400)
                player.ng = True
        else:
            if self.ng:
                if self.rect.bottom >= screen.get_rect().bottom:
                    death.play(0)
                    player.rect.bottomleft = (80,400)
                    player.ng = True
            else:
                if self.rect.top <= screen.get_rect().top:
                    death.play(0)
                    player.rect.bottomleft = (80,400)
                    player.ng = True
platforms = walnut.sprite.Group()
purpleplatforms = walnut.sprite.Group()
spikeblocks = walnut.sprite.Group()
class Platform(walnut.sprite.Sprite):
    def __init__(self, x, y, width, height):
        walnut.sprite.Sprite.__init__(self, platforms)
        self.image = walnut.Surface((width, height))
        self.image.fill((0, 0, 255))
        self.rect = walnut.Rect(x, y, width, height)
        self.x = x
        self.y = y
    def update(self):
        self.rect.x = self.x + (bgrect.x*0.6)
class PurplePlatform(walnut.sprite.Sprite):
    def __init__(self, x, y, width, height):
        walnut.sprite.Sprite.__init__(self, purpleplatforms,platforms)
        self.image = walnut.Surface((width, height))
        self.image.fill((174, 52, 235))
        self.rect = walnut.Rect(x, y, width, height)
        self.x = x
        self.y = y
    def update(self):
        self.rect.x = self.x + (bgrect.x*0.6)
class Spike(walnut.sprite.Sprite):
    def __init__(self, x, y):
        walnut.sprite.Sprite.__init__(self, spikeblocks,platforms)
        self.image = spikeblock
        self.rect = self.image.get_rect(topleft = (x,y))
        self.x = x
        self.y = y
    def update(self):
        self.rect.x = self.x + (bgrect.x*0.6)
rect1 = Platform(100, 400, 200, 100)
rect2 = PurplePlatform(160, 150, 200, 30)
rect3 = PurplePlatform(460, 390, 120, 20)
rect4 = Platform(530, 160, 50, 50)
rect5 = Platform(750, 400, 95, 20)
rect6 = Platform(980,300,200,30)
rect7 = Platform(750,150,20,250)
player = Player()
spikeboy1 = Spike(425,380)
spikeboy2 = Spike(320,180)
spikeboy3 = Spike(300,450)
spikeboy4 = Spike(715,190)
spikeboy5 = Spike(715,340)
endone = PurplePlatform(1000,100,180,200)
endone.image = icecream
goal = walnut.sprite.Group()
goal.add(endone)
while True:
    for event in walnut.event.get():
        if event.type == walnut.QUIT:
            quit()
        if event.type == walnut.KEYDOWN:
            if event.key == walnut.K_SPACE and player.jumps:
                player.jumptime = 18
                player.jumps -= 1
            if event.key == walnut.K_g:
                player.ng = not player.ng
    screen.blit(richbg, bgrect)
    richbg.blit(jumpxtwo,(80,200))
    richbg.blit(purpplattutorial,(450,250))
    richbg.blit(antigrav,(175,100))
    if not finished:
        player.update()
        platforms.update()
    bgrect.x = player.rect.x*-0.5
    if walnut.sprite.spritecollide(player,goal,False,walnut.sprite.collide_rect_ratio(1.1)):
        screen.blit(cardboard,(0,0))
        if not finished:
            complete.play(0)
        finished = True
    else:
        screen.blit(walnut.transform.flip(player.image, not player.right, not player.ng), player.rect)
        platforms.draw(screen)
    clock.tick(60)
    walnut.display.update()