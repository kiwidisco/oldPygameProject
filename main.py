"""
Jayden Tsai
Final Project

"""





#background will be city, not urban, but outer city rim, footpath like celeste, metal / tile floor

#Celeste Background
import pygame, time, math
from pygame import mixer

from pygame.locals import(
  K_UP,
  K_DOWN,
  K_LEFT,
  K_RIGHT,
  K_ESCAPE,
  KEYDOWN,
  QUIT,
)

floorLoc = -320

#initiate pygame
pygame.init()

#FPS
clock = pygame.time.Clock()
fps = 30

# set window title
pygame.display.set_caption("propagation")

# load and set window icon
gameIcon = pygame.image.load("images/player.png")
pygame.display.set_icon(gameIcon)

#Create screen
screenWidth = 1280
screenHeight = 720
screenSize = (screenWidth,screenHeight)
screen = pygame.display.set_mode(screenSize)

#Load Music
switch = pygame.mixer.Sound('Audio/SFX/switch.mp3')

#Load Sprites
floor = pygame.image.load('images/floor.png')
floorWidth = floor.get_width()
floorHeight = floor.get_height()

playerImage = pygame.image.load('images/player.png')

#Add
background1 = pygame.image.load('images/background1.webp')
#background2 = pygame.image.load('images/background2.png')
scrollX = 0
scrollY = 0

#Font
font = pygame.font.SysFont('dejavuserif',10)

button = pygame.image.load('images/button.png')

leftBoundary =  (3/10)*screenWidth
rightBoundary = (7/10)*screenWidth
topBoundary = (1/10)*screenHeight

def music():
  time.sleep(0.5)  
  pygame.mixer.Sound.play(switch)
  time.sleep(0.5)
  mixer.music.load('Audio/Music/Mustache Girl EX.mp3')
  mixer.music.play(-1)
  source = mixer.music.play()

class Player(pygame.sprite.Sprite):
  def __init__(self,x,y):
    super(Player, self).__init__()
    #Declare player sprite
    self.surf = playerImage
    
    #Declare player box
    self.rect = self.surf.get_rect()
    self.x, self.y = (x,y)
    #self.rect.centerx = 400
    #self.rect.bottom = 244

    #Does this update?
    #self.rect.centerx = self.x
    #self.rect.bottom = self.y
    
    #self.pos = (self.x,self.y)
    self.xVelo = 0
    self.yVelo = 0
    #self.velo = (self.xVelo,self.yVelo)
    #self.xAccel = 1
    
  def update(self,pressed_keys,pos,lmb):
    #Slow down player by reducing velocity
    if abs(self.xVelo) > 10:
      self.xVelo *= 0.6
    if abs(self.yVelo) > 10: 
      self.yVelo *= 0.6
    ##############################################################
    #Mouse Movement 
    mouseX,mouseY = pos
    xDiff = abs(mouseX-self.x)
    yDiff = abs(mouseY-(self.y-self.rect.height/2))
    dist = math.sqrt((xDiff)**2 + (yDiff)**2)
    if dist <= 100 and lmb == True:
      #Player size is the forgiveness of the blast radius
      playerSize = 2
      
      blastPower = 150/(dist**2)
      if self.x < mouseX:
        self.xVelo -= blastPower*xDiff
      else:
        self.xVelo += blastPower*xDiff
      if self.y < mouseY:
        self.yVelo -= blastPower*yDiff
      else:
        self.yVelo += blastPower*yDiff
    
    else:
      #Keyboard Movement
      if pressed_keys[K_LEFT]:
        self.xVelo -= 3
      if pressed_keys[K_RIGHT]:
        self.xVelo += 3
      if pressed_keys[K_UP]:
        self.yVelo -= 3
      if pressed_keys[K_DOWN]:
        self.yVelo += 3
    
    ##############################################################
    #add gravity    
    gravity = 1
    self.yVelo += gravity
    
    #Define player bounds
    predictedX = self.x + self.xVelo
    predictedY = self.y + self.yVelo
    #leftBoundary =  (3/10)*screenWidth
    #rightBoundary = (7/10)*screenWidth
    #topBoundary = (1/10)*screenHeight
    #Make sure player stays within bounds


    ##############################################################
    #Y Bounds
    
    if predictedY > topBoundary and predictedY < grass.rect.top:
      self.y += self.yVelo
    else:
      
      if predictedY < topBoundary:
        self.y = topBoundary
      if predictedY >= grass.rect.top:
        self.yVelo = 0
        self.y = grass.rect.top
    #X Bounds
    if predictedX <= rightBoundary and predictedX >= leftBoundary:
      self.x += self.xVelo
    else:
      if predictedX > rightBoundary:
        self.x = rightBoundary
      else:
        self.x = leftBoundary

      
    #If player touches floor, reset speed.
    ##############################################################
    #return self.pos,self.velo
    self.rect.centerx = self.x
    self.rect.bottom = self.y
    return self.x,self.xVelo

#Declare player's existence
player = Player(400,144)
"""
class Block(pygame.sprite.Sprite):
  def __init__(self, pos, size):
    super(Block, self).__init__(pos, size)
    #Declare player sprite
    self.surf = playerImage
    #Declare player box
    self.rect = self.surf.get_rect()

    self.rect.centerx, self.rect.centery = pos
    cube.surf = pygame.transform.scale(self.surf, size)
    
    #stretch, compression, 
    

  #def update(self):
    #update display based on scroll x and scroll y
    #self.rect.centerx += scrollX
    

cube = Block((200,200),(40,40))

"""

class Floor(pygame.sprite.Sprite):
  def __init__(self,i):
    super(Floor, self).__init__()
    #Declare player sprite
    self.image = floor
    #self.surf = floor
    #Declare player box
    self.rect = self.image.get_rect()
    
    self.rect.top = 300
    print(self.rect.width)
    self.rect.x = self.rect.width * i

    
  def update(self):
    if (player.x + player.rect.width/2) >= rightBoundary:
      print("pen")
      self.rect.move_ip((-player.xVelo, 0))
    if (player.x - player.rect.width/2) <= leftBoundary:
      print("pen")
      self.rect.move_ip((-player.xVelo, 0))

floors = pygame.sprite.Group()
for i in range(0,3):
  grass = Floor(i)
  floors.add(grass)
  


def drawText(x,y,text):
  location = (x,y)
  #parameters: text you want, true, color of text
  display = font.render(text, True, (255,25,25))
  screen.blit(display,location)
  """
  a = button.get_width()
  #b = button.get_height()
  www = (x+a/4,y)
  screen.blit(display,www)
  """

#Main Loop
def main():

  
  mixer.music.load('Audio/Music/Anticipation.mp3')
  mixer.music.play(-1)
  source = mixer.music.play()
  
  lmbCd = 0
  running = True
  while running:
    #If quit, quit
    clock.tick(fps)
    
    for event in pygame.event.get():
      if event.type == QUIT:
        #Goodbye screen
        running = False
  
  
        
    #Player
    pressed_keys = pygame.key.get_pressed()
    MousePos = pygame.mouse.get_pos()
    lmb,scrollWheel,rmb = pygame.mouse.get_pressed(num_buttons=3)
  
    if rmb ==1:
      music()
    if lmbCd <= 0:
      if lmb == 1:
        Lclick = True
        lmbCd = 90
        #cd = 1 sec (30 frames)
    else:
      lmbCd -=1
      lmb = False
    
    playerPos, playerVelo = player.update(pressed_keys,MousePos,lmb)
    screen.blit(background1,(0,0))
    
    #Update Player Sprite on screen
    #UH
    pygame.draw.line(screen,(255,255,255),MousePos,(player.rect.centerx,player.rect.centery))
    #screen.blit(player.surf,(player.x,player.y-player.rect.height))
    screen.blit(player.surf,player.rect)
    
    #screen.blit(cube.surf,cube.pos)
    
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, 244+64, screenWidth, 10))
    pygame.draw.circle(screen,(25,25,25),(player.x,player.y),5)
    drawText(20,20,str(player.xVelo))
    drawText(90,90,str(player.x - player.rect.width/2))
    drawText(190,190,str(leftBoundary))
    #drawFloor(player.xVelo)
    
    
    floors.update()
    floors.draw(screen)
    
    pygame.draw.line(screen,(255,255,255),(0,300),(500,300))
    pygame.draw.line(screen,(255,255,255),(player.rect.bottomright),(player.rect.topleft))
    #Coords of spawn location
    #pygame.draw.line(screen,(255,255,255),(0,144),(500,144))
    #pygame.draw.line(screen,(255,255,255),(400,2),(400,500))
    #Update display
    pygame.display.flip()

main()