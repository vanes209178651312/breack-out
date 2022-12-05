import pygame
import random
pygame.init()
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("brakeout")

clock = pygame.time.Clock()

#variables
doExit = False
px = 320
py = 470

bx = 350
by = 465

bVx = 5
bVy = 5
lives = 3
score = 0

class Brick:
  def __init__(self,xpos,ypos):
    self.xpos = xpos
    self.ypos = ypos
    self.alive = True
    self.color = (random.randrange(0, 255),random.randrange(0, 255),random.randrange(0, 255))

  def draw(self):
    if self.alive is True:
      pygame.draw.rect(screen, (self.color),(self.xpos, self.ypos, 50,20))

  def collide(self,x,y):
    if self.alive is True:
      if x+20>self.xpos and x<self.xpos+50 and y+20> self.ypos and y < self.ypos+20:
        self.alive= False
        return True



#bricks
b1 = Brick(20,20)
b2 = Brick(80, 20)
b3 = Brick(140, 20)
b4 = Brick(200, 20)
b5 = Brick(260, 20)
b6 = Brick(320,20)
b7 = Brick(380, 20)
b8 = Brick(440, 20)
b9 = Brick(500, 20)
b10 = Brick(560, 20)
b11 = Brick (620, 20)
b12 = Brick(20,40)
b13 = Brick(80,40)
b14 = Brick(140,40)
b15 = Brick(200, 40)
b16 = Brick(260, 40)
b17 = Brick(320,40)
b18 = Brick(380, 40)
b19 = Brick(440, 40)
b20 = Brick(500, 40)
b21 = Brick(560, 40)
b22 = Brick (620, 40)
b23 = Brick(20,60)
b24 = Brick(80, 60)
b25 = Brick(140, 60)
b26 = Brick(200, 60)
b27 = Brick(260, 60)
b28 = Brick(320, 60)
b29 = Brick(380, 60)
b30 = Brick(440, 60)
b31 = Brick(500, 60)
b32 = Brick(560, 60)
b33 = Brick (620, 60)
b34 = Brick(20,80)
b35 = Brick(80, 80)
b36 = Brick(140, 80)
b37 = Brick(200, 80)
b38 = Brick(260, 80)
b39 = Brick(320, 80)
b40 = Brick(380, 80)
b41 = Brick(440, 80)
b42 = Brick(500, 80)
b43 = Brick(560, 80)
b44 = Brick (620, 80)
b45 = Brick(20,100)
b46 = Brick(80, 100)
b47 = Brick(140, 100)
b48 = Brick(200, 100)
b49 = Brick(260, 100)
b50 = Brick(320, 100)
b51 = Brick(380, 100)
b52 = Brick(440, 100)
b53 = Brick(500, 100)
b54 = Brick(560, 100)
b55 = Brick (620,100)
b56 = Brick(20,120)
b57 = Brick(80, 120)
b58 = Brick(140, 120)
b59 = Brick(200, 120)
b60 = Brick(260, 120)
b61 = Brick(320, 120)
b62 = Brick(380, 120)
b63 = Brick(440, 120)
b64 = Brick(500, 120)
b65 = Brick(560, 120)
b66 = Brick (620,120)




while not doExit: #gameloop
  clock.tick(60)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      doExit = True

  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    px -=7
  if keys[pygame.K_RIGHT]:
    px +=7

#moves ball
  bx += bVx
  by += bVy

# makes ball blounce
  if bx < 0 or bx+20> 700:
    bVx *= -1
  if by < 0:
    bVy *= -1



  if b1.collide(bx,by):
    bVy*=-1
  if b2.collide(bx,by):
    bVy*=-1
  if b3.collide(bx,by):
    bVy*=-1
  if b4.collide(bx,by):
    bVy*=-1
  if b5.collide(bx,by):
    bVy*=-1
  if b6.collide(bx,by):
    bVy*=-1
  if b7.collide(bx,by):
    bVy*=-1
  if b8.collide(bx,by):
    bVy*=-1
  if b9.collide(bx,by):
    bVy*=-1
  if b10.collide(bx,by):
    bVy*=-1
  if b11.collide(bx,by):
    bVy*=-1
  if b12.collide(bx,by):
    bVy*=-1    
  if b13.collide(bx,by):
    bVy*=-1    
  if b14.collide(bx,by):
    bVy*=-1    
  if b15.collide(bx,by):
    bVy*=-1
  if b16.collide(bx,by):
    bVy*=-1
  if b17.collide(bx,by):
    bVy*=-1    
  if b18.collide(bx,by):
    bVy*=-1    
  if b19.collide(bx,by):
    bVy*=-1
  if b20.collide(bx, by):
    bVy *=-1
  if b21.collide(bx, by):
    bVy *=-1
  if b22.collide(bx, by):
    bVy *=-1
  if b23.collide(bx, by):
    bVy *=-1
  if b24.collide(bx, by):
    bVy *=-1
  if b25.collide(bx, by):
    bVy *=-1
  if b26.collide(bx, by):
    bVy *=-1
  if b27.collide(bx, by):
    bVy *=-1
  if b28.collide(bx, by):
    bVy *=-1 
  if b29.collide(bx, by):
    bVy *=-1
  if b30.collide(bx, by):
    bVy *=-1
  if b31.collide(bx, by):
    bVy *=-1
  if b32.collide(bx, by):
    bVy *=-1
  if b33.collide(bx, by):
    bVy *=-1
  if b34.collide(bx, by):
    bVy *=-1
  if b35.collide(bx, by):
    bVy *=-1
  if b36.collide(bx, by):
    bVy *=-1
  if b37.collide(bx, by):
    bVy *=-1
  if b38.collide(bx, by):
    bVy *=-1 
  if b39.collide(bx, by):
    bVy *=-1
  if b40.collide(bx, by):
    bVy *=-1
  if b41.collide(bx, by):
    bVy *=-1
  if b42.collide(bx, by):
    bVy *=-1
  if b43.collide(bx, by):
    bVy *=-1
  if b44.collide(bx, by):
    bVy *=-1
  if b45.collide(bx, by):
    bVy *=-1
  if b46.collide(bx, by):
    bVy *=-1
  if b47.collide(bx, by):
    bVy *=-1
  if b48.collide(bx, by):
    bVy *=-1
  if b49.collide(bx, by):
    bVy *=-1
  if b50.collide(bx, by):
    bVy *=-1
  if b51.collide(bx, by):
    bVy *=-1
  if b52.collide(bx, by):
    bVy *=-1
  if b53.collide(bx, by):
    bVy *=-1 
  if b54.collide(bx, by):
    bVy *=-1
  if b55.collide(bx, by):
    bVy *=-1
  if b56.collide(bx, by):
    bVy *=-1
  if b57.collide(bx, by):
    bVy *=-1
  if b58.collide(bx, by):
    bVy *=-1
  if b59.collide(bx, by):
    bVy *=-1
  if b60.collide(bx, by):
    bVy *=-1
  if b61.collide(bx, by):
    bVy *=-1
  if b62.collide(bx, by):
    bVy *=-1
  if b63.collide(bx, by):
    bVy *=-1
  if b64.collide(bx, by):
    bVy *=-1
  if b65.collide(bx, by):
    bVy *=-1
  if b66.collide(bx, by):
    bVy *=-1
# makes ball bounce of paddle
  if by +20> py and bx +20 > px and bx < px+100:
    bVy *= -1
  #collision with ground
    if by >= 500:
        lives -= 1
        bx = 350
        by = 250 
   
#renter section the
  screen.fill((0,255,0))

  b1.draw()
  b2.draw()
  b3.draw()
  b4.draw()
  b5.draw()
  b6.draw()
  b7.draw()
  b8.draw()
  b9.draw()
  b10.draw()
  b11.draw()
  b12.draw()
  b13.draw()
  b14.draw()
  b15.draw()
  b16.draw()
  b17.draw()
  b18.draw()
  b19.draw()
  b20.draw()
  b20.draw()
  b21.draw()
  b22.draw()
  b23.draw()
  b24.draw()
  b25.draw()
  b26.draw()
  b27.draw()
  b28.draw()
  b29.draw()
  b30.draw()
  b31.draw()
  b32.draw()
  b33.draw()
  b34.draw()
  b35.draw()
  b36.draw()
  b37.draw()
  b38.draw()
  b39.draw()
  b40.draw()
  b41.draw()
  b42.draw()
  b43.draw()
  b44.draw()
  b45.draw()
  b46.draw()
  b47.draw()
  b48.draw()
  b49.draw()
  b50.draw()
  b51.draw()
  b52.draw()
  b53.draw()
  b54.draw()
  b55.draw()
  b56.draw()
  b57.draw()
  b58.draw()
  b59.draw()
  b60.draw()
  b61.draw()
  b62.draw()
  b63.draw()
  b64.draw()
  b65.draw()
  b66.draw()
  font = pygame.font.Font(None, 15)
  text = font.render(str(lives),1, (0, 0,0))
  screen.blit(text, (660, 9))
  font = pygame.font.Font(None, 15)
  text = font.render(str(score),1, (0, 0, 0))
  screen.blit(text, (40, 9))
  
  pygame.draw.rect(screen,(255,255,255),(px,py,100,20))
  pygame.draw.ellipse(screen,(255,200,255),(bx,by,20,20))

  pygame.display.flip()
#end of game loop
pygame.quit()
