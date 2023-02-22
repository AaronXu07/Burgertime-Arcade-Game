'''
Name: Aaron Xu
Date: January 9, 2023
Title: BurgerTime Arcade Game
Description: The goal of the game is to complete the burger without being touched by the enemy. To complete a burger, you must walk on top of every piece of the topping to drop it to the next level. If there is another burger topping on the level dropped to, the other burger topping will be knocked down to the next level. If you are touched by the enemy, you lose the game. If you complete the burger, you win the game. The controls are the arrow keys, up, down, left, right. You can go up and down only on the ladders. Each burger that falls will give 50 points and a completed burger will give 500 points. Enjoy!
Last Modified: January 20, 2023
'''

import pygame, sys #imports the libraries (  Pygame and System Modules)
from pygame.locals import* #Only imports the locals part of the module
pygame.init() #Initialize all usefull variables

WINDOW = pygame.display.set_mode((500, 680)) #set window size, which is 400 pixels wide and 300 high

BLACK = (0, 0, 0) #colour variable for black
WHITE = (255, 255, 255)  #colour variable for white
RED = (242, 46, 31)#colour variable for bright red
GREEN = (0, 204, 0) #colour variable for green

pygame.display.set_caption("BurgerTime.py") #Set Caption

FPS = 60 #this sets the number of frames per second
fpsClock = pygame.time.Clock() #Initializes the pygame clock

Bold = pygame.font.SysFont("Times New Roman", 20, True, False) #Bold font is times new roman, the font is set to 20 and is bolded
BIGESTTEXT = pygame.font.SysFont("Times New Roman", 70, False, False)#very big text for game over text

ScoreText = Bold.render("SCORE", True, RED)
Winning = BIGESTTEXT.render("YOU WON!", True, GREEN) #loads winning text in green
Losing = BIGESTTEXT.render("YOU LOST", True, RED) #loads losing text in green

SpriteSheet = pygame.image.load("spritesheet-removebg-preview.png") #imports the sprite sheet
SpriteSheet = pygame.transform.scale(SpriteSheet, (700, 500)) #changes the dimentions of the sprite sheet
OppositeSheet = pygame.transform.flip(SpriteSheet, True, False)#sprite sheet doesn't come with character walking right
Plate = pygame.image.load("burgertimeplate.png") #imports the picture for the plate for the burgers
Plate = pygame.transform.scale(Plate, (120, 20)) #changes the size of the plates
Map = pygame.image.load("map.png") #this is a picture of the map 

Score = 0#temporary variable that tracks the score

L = 1 #temporary variable to track the costume number for the walking left animation
Linc = 0 #temporary variable to track the walking left costume cycle velocity
R = 1 #temporary variable to track the costume number for the walking right animation
Rinc = 0 #temporary variable to track the walking right costume cycle velocity
U = 1 #temporary variable to track the costume number for the walking up animation
Uinc = 0#temporary variable to track the walking up costume cycle velocity
D = 1#temporary variable to track the costume number for the walking down animation
Dinc = 0#temporary variable to track the walking down costume cycle velocity

x = 445 #variable for the x value of the character 
xinc = 0 #variable for the entire character x velocity if they are walking around
y = 67 #variable for the y value of the character #(was 67)
yinc = 0 #variable for the entire character x velocity if they are going up or down

WalkLeft = False #defines variable that tracks if the character should be walking left 
WalkRight = False#defines variable that tracks if the character should be walking right
WalkUp = False#defines variable that tracks if the character should be walking up 
WalkDown = False#defines variable that tracks if the character should be walking down

Level1 = 495 #y coordinates for the bottom floor
Level2 = 355 #y coordinates for the 2nd lowest with a burger topping
Level3 = 255 #y coordinates for the 2nd highest floor with a burger topping
Level4 = 100 #y coordinates for the top floor

#temporary variables for the y values for all the burger pieces
burger1y1 = Level1
burger1y2 = Level1
burger1y3 = Level1
burger1y4 = Level1

burger2y1 = Level2
burger2y2 = Level2
burger2y3 = Level2
burger2y4 = Level2

burger3y1 = Level3
burger3y2 = Level3
burger3y3 = Level3
burger3y4 = Level3

burger4y1 = Level4
burger4y2 = Level4
burger4y3 = Level4
burger4y4 = Level4

#variable that tracks which level the burger topping is on
Burger1Level = 1
Burger2Level = 2
Burger3Level = 3
Burger4Level = 4

#variable for the enemy character
E = 1 #costume number
Einc = 1 #costume number increase
Ey = 67 #Y VALUE of the enemy
Eyinc = 1 #the velocity/direction of the enemy's movement

GameLost=False#if the game is lost

LostCostume = 0 #the costume number of the player if they lose the game
LostCostumeInc = 0 #the costume number increase

while True: #Main program loop
  for event in pygame.event.get(): #searches for any user input events for the program
    if event.type == QUIT: #makes sure that if the x button is clicked, the program ends
      pygame.quit()
      sys.exit()

    #movements: 
    if event.type == pygame.KEYDOWN: #if a key has been pressed
      if event.key == pygame.K_LEFT and WalkRight == False and WalkUp == False and WalkDown == False and GameLost == False: #if the left key has been pressed and no other movement is happening

        if y==460:#can only move left moveent on bottom platform
          xinc = -1 #sets x velocity to move left 
          Linc =1 #sets the animation to begin playing 
          L = 1#sets the costume to the first one
          WalkLeft = True#sets that the player is walking left

        elif y==67: #can only move left moveent on the top platform
          xinc = -1 #sets x velocity to move left 
          Linc =1 #sets the animation to begin playing 
          L = 1#sets the costume to the first one
          WalkLeft = True #sets that the player is walking left

        elif y>=320 and y<=330:#checks if its close enough to the platform
          y=325 #sets y to the exact platform height
          xinc = -1 #sets x velocity to move left 
          Linc =1 #sets the animation to begin playing 
          L = 1#sets the costume to the first one
          WalkLeft = True#sets that the player is walking left

        elif y>= 215 and y<=225:#checks if its close enough to the platform
          y=220#sets y to the exact platform height
          xinc = -1 #sets x velocity to move left 
          Linc =1 #sets the animation to begin playing 
          L = 1#sets the costume to the first one
          WalkLeft = True#sets that the player is walking left

        elif y>= 150 and y<=160:#checks if its close enough to the platform
          y=155#sets y to the exact platform height
          xinc = -1 #sets x velocity to move left 
          Linc =1 #sets the animation to begin playing 
          L = 1#sets the costume to the first one
          WalkLeft = True#sets that the player is walking left
          
    if event.type == pygame.KEYDOWN: #if a key has been pressed
      if event.key == pygame.K_RIGHT and WalkLeft == False and WalkUp == False and WalkDown == False and GameLost == False:#if the right key has been pressed and no other movements are happening
        
        if y==460:#only allows right movement on the bottom platform
          xinc = 1#sets direction velocity to 1 so it will move left if the key is held
          Rinc = 1#sets the costume cycle speed
          R = 1#sets the first costume
          WalkRight = True#sets that the player is currently walking right

        elif y==67:#only allows right movement on the top platform
          xinc = 1#sets direction velocity to 1 so it will move left if the key is held
          Rinc = 1#sets the costume cycle speed
          R = 1#sets the first costume
          WalkRight = True#sets that the player is currently walking right

        elif y>=323 and y<=327:#only allows right movment when its close enough to the platform
          y=325#sets the y to exactly the platform height
          xinc = 1#sets direction velocity to 1 so it will move left if the key is held
          Rinc = 1#sets the costume cycle speed
          R = 1#sets the first costume
          WalkRight = True#sets that the player is currently walking right

        elif y>= 215 and y<=225:#only allows right movment when its close enough to the platform
          y=220#sets the y to exactly the platform height
          xinc = 1#sets direction velocity to 1 so it will move left if the key is held
          Rinc = 1#sets the costume cycle speed
          R = 1#sets the first costume
          WalkRight = True#sets that the player is currently walking right

        elif y>= 150 and y<=160:#only allows right movment when its close enough to the platform
          y=155#sets the y to exactly the platform height
          xinc = 1#sets direction velocity to 1 so it will move left if the key is held
          Rinc = 1#sets the costume cycle speed
          R = 1#sets the first costume
          WalkRight = True#sets that the player is currently walking right
          
    if event.type == pygame.KEYDOWN: #if a key has been pressed
      if event.key == pygame.K_UP and WalkLeft == False and WalkRight == False and WalkDown == False and GameLost == False: #if the up key has been pressed
        if x >= 93 and x <= 103: #1st ladder
          yinc = -1 #sets x velocity to move left 
          Uinc = 1 #sets the animation to begin playing
          U = 1#sets to the first costume
          WalkUp = True#sets that the player is currently walking up

        elif x >= 217 and x <= 227: #2nd ladder
          yinc = -1 #sets x velocity to move left 
          Uinc = 1 #sets the animation to begin playing
          U = 1#sets to the first costume
          WalkUp = True#sets that the player is currently walking up

        elif x >= 343 and x <= 353: #3rd ladder
          yinc = -1 #sets x velocity to move left 
          Uinc = 1 #sets the animation to begin playing
          U = 1#sets to the first costume
          WalkUp = True

        elif x >= 0 and x <= 9:#1st small ladder
          yinc = -1 #sets x velocity to move left 
          Uinc = 1 #sets the animation to begin playing
          U = 1#sets to the first costume
          WalkUp = True#sets that the player is currently walking up

        elif x >= 155 and x <= 165:#2nd small ladder
            yinc = -1 #sets x velocity to move left 
            Uinc = 1 #sets the animation to begin playing
            U = 1#sets to the first costume
            WalkUp = True#sets that the player is currently walking up

        elif x >= 278 and x <= 288:#3rd small ladder
            yinc = -1 #sets x velocity to move left 
            Uinc = 1 #sets the animation to begin playing
            U = 1#sets to the first costume
            WalkUp = True#sets that the player is currently walking up

        elif x >= 447 and x <= 455:#4th small ladder
            yinc = -1 #sets x velocity to move left 
            Uinc = 1 #sets the animation to begin playing
            U = 1#sets to the first costume
            WalkUp = True#sets that the player is currently walking up
          
    if event.type == pygame.KEYDOWN: #if a key has been pressed
      if event.key == pygame.K_DOWN and WalkLeft == False and WalkRight == False and WalkUp == False and GameLost == False: #if the down key has been pressed

        if x >= 93 and x <= 103:
          yinc = 1 #sets x velocity to move left 
          Dinc = 1 #sets the animation to begin playing
          D = 1#sets to the first costume
          WalkDown = True

        elif x >= 217 and x <= 227:
          yinc = 1 #sets x velocity to move left 
          Dinc = 1 #sets the animation to begin playing
          D = 1#sets to the first costume
          WalkDown = True#sets that the player is currently moving down
          
        elif x >= 343 and x <= 353:
          yinc = 1 #sets x velocity to move left 
          Dinc = 1 #sets the animation to begin playing
          D = 1#sets to the first costume
          WalkDown = True#sets that the player is currently moving down

        elif x >= 0 and x <= 9:
          yinc = 1 #sets x velocity to move left 
          Dinc = 1 #sets the animation to begin playing
          D = 1#sets to the first costume
          WalkDown = True#sets that the player is currently moving down

        elif x >= 155 and x <= 165:#2nd small ladder
          yinc = 1 #sets x velocity to move left 
          Dinc = 1 #sets the animation to begin playing
          D = 1#sets to the first costume
          WalkDown = True#sets that the player is currently moving down

        elif x >= 278 and x <= 288:#3rd small ladder
          yinc = 1 #sets x velocity to move left 
          Dinc = 1 #sets the animation to begin playing
          D = 1#sets to the first costume
          WalkDown = True#sets that the player is currently moving down

        elif x >= 447 and x <= 455:#4th small ladder
          yinc = 1 #sets x velocity to move left 
          Dinc = 1 #sets the animation to begin playing
          D = 1#sets to the first costume
          WalkDown = True#sets that the player is currently moving down
          
    if event.type == pygame.KEYUP: #if a key has been lifted
      if event.key == pygame.K_LEFT: #if the left arrow has been lifted
        xinc = 0 #sets velocity to 0 
        Linc = 0 #stops playing walking left animation
        WalkLeft = False#player is not walking left anymore

    if event.type == pygame.KEYUP: #if a key has been lifted
      if event.key == pygame.K_RIGHT:
        xinc = 0#sets velocity to 0 
        Rinc = 0#stops the coostume cycle velocity
        WalkRight = False#player is not waking right anymore

    if event.type == pygame.KEYUP: #if a key has been lifted
      if event.key == pygame.K_UP: #if the up key has been lifted
        yinc = 0#sets velocity to 0 
        Uinc = 0#stops the costume cycle velocity
        WalkUp = False#player is not walking up anymore

    if event.type == pygame.KEYUP:#if a key has been lifted
      if event.key == pygame.K_DOWN: #if the down key has been lifted
        yinc = 0#sets velocity to 0
        Dinc = 0#stops the costume cycle velocity
        WalkDown = False#player is not walking down anymore

        
  #drawing map:
  WINDOW.fill(BLACK) #window colour is filled black

  WINDOW.blit(Plate, (125, 635), (0, 1, 110, 20)) #displays the plate

  WINDOW.blit(Map, (0, 112)) #displays the map

  WINDOW.blit(ScoreText, (15,5)) #displays the text score
  
  ScoreNum = Bold.render(f"{Score}", True, WHITE) #renders the updated score number
  WINDOW.blit(ScoreNum, (15, 30)) #outputs the updated score number
  
  #outlines
  pygame.draw.rect(WINDOW, WHITE, (498, 0, 2, 680), 0)#right wall line
  pygame.draw.rect(WINDOW, WHITE, (0, 0, 2, 680), 0)#left wall line
  pygame.draw.rect(WINDOW, WHITE, (0, 678, 500, 2), 0)#bottom wall line
  
  #burger condiments
  #bottom bun
  WINDOW.blit(SpriteSheet, (119, burger1y1), (305, 162, 43, 22))
  WINDOW.blit(SpriteSheet, (162, burger1y2), (345, 162, 22, 22))
  WINDOW.blit(SpriteSheet, (184, burger1y3), (368, 162, 22, 22))
  WINDOW.blit(SpriteSheet, (206, burger1y4), (396, 162, 32, 22))

  #burger
  WINDOW.blit(SpriteSheet, (117, burger2y1), (305, 207, 43, 20))
  WINDOW.blit(SpriteSheet, (160, burger2y2), (345, 207, 22, 20))
  WINDOW.blit(SpriteSheet, (182, burger2y3), (368, 207, 22, 20))
  WINDOW.blit(SpriteSheet, (204, burger2y4), (396, 207, 32, 20))

  #Lettuce
  WINDOW.blit(SpriteSheet, (117, burger3y1), (305, 255, 43, 22))
  WINDOW.blit(SpriteSheet, (160, burger3y2), (345, 255, 22, 22))
  WINDOW.blit(SpriteSheet, (182, burger3y3), (368, 255, 22, 22))
  WINDOW.blit(SpriteSheet, (204, burger3y4), (396, 255, 32, 22))

  #top bun
  WINDOW.blit(SpriteSheet, (117, burger4y1), (305, 140, 43, 22))
  WINDOW.blit(SpriteSheet, (160, burger4y2), (345, 140, 22, 22))
  WINDOW.blit(SpriteSheet, (182, burger4y3), (368, 140, 22, 22))
  WINDOW.blit(SpriteSheet, (204, burger4y4), (396, 140, 32, 22))


  #this is what moves the character as well as its animation
  if E<8:
    WINDOW.blit(SpriteSheet, (100, Ey), (188, 92, 45, 44))

  elif E<=16:
    WINDOW.blit(SpriteSheet, (100, Ey), (232, 92, 45, 44))
    if E ==16:
      E=1

  if Ey>=465:
    Eyinc=-1

  if Ey<=67:
    Eyinc=1

  
  #idle figure:
  if WalkLeft == False and WalkRight == False and WalkUp == False and WalkDown == False and GameLost == False:#the the character is standing still
    WINDOW.blit(SpriteSheet, (x, y), (47, 0, 45, 45))
    
  #walking left:
  elif WalkLeft == True: #if the character is supposed to walk left
    if L <= 5: #if L is under or equal to 5, it will display the 1st sprite walking left image
      WINDOW.blit(SpriteSheet, (x, y), (138, 0, 45, 44)) #4th sprite
      
    elif L <= 10: #if L is under or equal to 10 , it will display the 2nd walking left image 
      WINDOW.blit(SpriteSheet, (x, y), (185, 0, 45, 44)) #5th sprite
      
    elif L <= 15: #if L is under or equal to 15, it will display the 3rd walking left image\
      WINDOW.blit(SpriteSheet, (x,y), (230, 0, 45, 44)) #6th walking left sprite
      if L == 15:#if L reachs 15, it resets to the first walking image again
        L = 1
        
  #walking right
  elif WalkRight == True and GameLost == False: #if the character is supposed to walk right
    if R <= 5: #if R is under or equal to 5, it will display the 1st sprite walking right image
      WINDOW.blit(OppositeSheet, (x, y), (515, 0, 45, 44)) #4th sprite
      
    elif R <= 10: #if R is under or equal to 10 , it will display the 2nd walking right image
      WINDOW.blit(OppositeSheet, (x, y), (470, 0, 45, 44)) #5th sprite
      
    elif R <= 15: #if R is under or equal to 15, it will display the 3rd walking right image
      WINDOW.blit(OppositeSheet, (x,y), (425, 0, 45, 44)) #6th walking left sprite
      if R == 15:#if R reachs 15, it resets to the first walking image again
        R = 1

   #walking up
  elif WalkUp == True and GameLost == False: #if the character is supposed to walk up
    if U <= 5: #if U is under or equal to 5, it will display the 1st sprite walking up image
      WINDOW.blit(SpriteSheet, (x, y), (277, 0, 49, 44)) #7th sprite
      
    elif U <= 10: #if U is under or equal to 10 , it will display the 2nd walking up image
      WINDOW.blit(SpriteSheet, (x, y), (325, 0, 49, 44)) #8th sprite
      
    elif U <= 15: #if U is under or equal to 15, it will display the 3rd walking Up image
      WINDOW.blit(SpriteSheet, (x, y), (373, 0, 49, 44)) #9th walking left sprite
      if U == 15:#if U reachs 15, it resets to the first walking image again
        U = 1
        
  #walking down
  elif WalkDown == True and GameLost == False: #if the character is supposed to walk down
    if D <= 5: #if D is under or equal to 5, it will display the 1st sprite walking up image
      WINDOW.blit(SpriteSheet, (x, y), (0, 0, 45, 44)) #1st sprite
      
    elif D <= 10: #if D is under or equal to 10 , it will display the 2nd walking up image
      WINDOW.blit(SpriteSheet, (x, y), (47, 0, 45, 44)) #2nd sprite
      
    elif D <= 15: #if D is under or equal to 15, it will display the 3rd walking Up image
      WINDOW.blit(SpriteSheet, (x, y), (93, 0, 44, 40)) #3th sprite
      if D == 15:#if D reachs 15, it resets to the first walking image again
        D = 1

  if y == 460: #lowers the pieces for the bottom bun on the bottom floor when stepped on
    if Burger1Level == 1:
      if burger1y1 == Level1:
        if x >= 120 and x<=130:
          burger1y1+=5
      if burger1y2 == Level1:
        if x >= 140 and x<=150:
          burger1y2+=5
      if burger1y3 == Level1:
        if x >= 160 and x<=170:
          burger1y3+=5
      if burger1y4 == Level1:
        if x >= 180 and x<=195:
          burger1y4+=5
      
    if Burger2Level == 1: #lowers the pieces for the burger on the bottom floor when stepped on
      if burger2y1 == Level1:
        if x >= 120 and x<=130:
          burger2y1+=5
      if burger2y2 == Level1:
        if x >= 140 and x<=150:
          burger2y2+=5
      if burger2y3 == Level1:
        if x >= 160 and x<=170:
          burger2y3+=5
      if burger2y4 == Level1:
        if x >= 180 and x<=195:
          burger2y4+=5

    if Burger3Level == 1: #lowers the pieces for the lettuce on the bottom floor when stepped on
      if burger3y1 == Level1:
        if x >= 120 and x<=130:
          burger3y1+=5
      if burger3y2 == Level1:
        if x >= 140 and x<=150:
          burger3y2+=5
      if burger3y3 == Level1:
        if x >= 160 and x<=170:
          burger3y3+=5
      if burger3y4 == Level1:
        if x >= 180 and x<=195:
          burger3y4+=5

    if Burger4Level == 1: #lowers the pieces for the topbun on the bottom floor when stepped on
      if burger4y1 == Level1:
        if x >= 120 and x<=130:
          burger4y1+=5
      if burger4y2 == Level1:
        if x >= 140 and x<=150:
          burger4y2+=5
      if burger4y3 == Level1:
        if x >= 160 and x<=170:
          burger4y3+=5
      if burger4y4 == Level1:
        if x >= 180 and x<=195:
          burger4y4+=5
          
  if y == 325: #lowers the burger when stepped on from the 2nd platform
    if Burger2Level == 2: 
      if burger2y1 == Level2:
        if x >= 120 and x<=130:
          burger2y1+=5
      if burger2y2 == Level2:
        if x >= 140 and x<=150:
          burger2y2+=5
      if burger2y3 == Level2:
        if x >= 160 and x<=170:
          burger2y3+=5
      if burger2y4 == Level2:
        if x >= 180 and x<=195:
          burger2y4+=5

    if Burger3Level == 2: #lowers the lettuce when stepped on from the 2nd platform
      if burger3y1 == Level2:
        if x >= 120 and x<=130:
          burger3y1+=5
      if burger3y2 == Level2:
        if x >= 140 and x<=150:
          burger3y2+=5
      if burger3y3 == Level2:
        if x >= 160 and x<=170:
          burger3y3+=5
      if burger3y4 == Level2:
        if x >= 180 and x<=195:
          burger3y4+=5

    if Burger4Level == 2: #lowers the topbun when stepped on from the 2nd platform
      if burger4y1 == Level2:
        if x >= 120 and x<=130:
          burger4y1+=5
      if burger4y2 == Level2:
        if x >= 140 and x<=150:
          burger4y2+=5
      if burger4y3 == Level2:
        if x >= 160 and x<=170:
          burger4y3+=5
      if burger4y4 == Level2:
        if x >= 180 and x<=195:
          burger4y4+=5
          
  if y == 220: #lowers the lettuce when stepped on from the 3rd platform
    if Burger3Level == 3:
      if burger3y1 == Level3:
        if x >= 120 and x<=130:
          burger3y1+=5
      if burger3y2 == Level3:
        if x >= 140 and x<=150:
          burger3y2+=5
      if burger3y3 == Level3:
        if x >= 160 and x<=170:
          burger3y3+=5
      if burger3y4 == Level3:
        if x >= 180 and x<=195:
          burger3y4+=5
          
    if Burger4Level == 3: #lowers the topbun when stepped on from the 3rd platform
      if burger4y1 == Level3:
        if x >= 120 and x<=130:
          burger4y1+=5
      if burger4y2 == Level3:
        if x >= 140 and x<=150:
          burger4y2+=5
      if burger4y3 == Level3:
        if x >= 160 and x<=170:
          burger4y3+=5
      if burger4y4 == Level3:
        if x >= 180 and x<=195:
          burger4y4+=5
          
  if y == 67: #lowering for top bun from the top floor
    if burger4y1 == Level4:
      if x >= 120 and x<=130:
        burger4y1+=5
    if burger4y2 == Level4:
      if x >= 140 and x<=150:
        burger4y2+=5
    if burger4y3 == Level4:
      if x >= 160 and x<=170:
        burger4y3+=5
    if burger4y4 == Level4:
      if x >= 180 and x<=195:
        burger4y4+=5


  if burger1y1 > Level1 and burger1y2 > Level1 and burger1y3 > Level1 and burger1y4 > Level1: #if the bottom bun should fall onto the plate, adds 50 score if it is true
    if Burger1Level == 1:
      burger1y1 = 625
      burger1y2 = 625
      burger1y3 = 625
      burger1y4 = 625
      Burger1Level = 0
      Score+=50
    
  if burger2y1 > Level2 and burger2y2 > Level2 and burger2y3 > Level2 and burger2y4 > Level2: #if the burger patty should fall onto the bottomplatform, adds 50 score if it is true
    if Burger2Level == 2:
      burger2y1 = Level1
      burger2y4 = Level1
      burger2y2 = Level1
      burger2y3 = Level1
      Burger2Level = 1
      Score+=50
      
  if burger2y1 > Level1 and burger2y2 > Level1 and burger2y3 > Level1 and burger2y4 > Level1: #if the burger patty should fall onto the plate, adds 50 score if it is true
    if Burger2Level == 1:
      burger2y1 = 605
      burger2y4 = 605
      burger2y2 = 605
      burger2y3 = 605
      Burger2Level = 0
      Score+=50
    
  if burger3y1 > Level3 and burger3y2 > Level3 and burger3y3 > Level3 and burger3y4 > Level3:#if the lettuce should fall onto the 2nd floor, adds 50 score if it is true
    if Burger3Level == 3:
      burger3y1 = Level2
      burger3y4 = Level2
      burger3y2 = Level2
      burger3y3 = Level2
      Burger3Level = 2
      Score+=50
      
  if burger3y1 > Level2 and burger3y2 > Level2 and burger3y3 > Level2 and burger3y4 > Level2:#if the lettuce should fall onto the bottom floor, adds 50 score if it is true
    if Burger3Level == 2:
      burger3y1 = Level1
      burger3y4 = Level1
      burger3y2 = Level1
      burger3y3 = Level1
      Burger3Level = 1
      Score+=50
      
  if burger3y1 > Level1 and burger3y2 > Level1 and burger3y3 > Level1 and burger3y4 > Level1:#if the lettuce should fall onto the plate, adds 50 score if it is true
    if Burger3Level == 1:
      burger3y1 = 585
      burger3y4 = 585
      burger3y2 = 585
      burger3y3 = 585
      Burger3Level = 0
      Score+=50
      
  if burger4y1 > Level4 and burger4y2 > Level4 and burger4y3 > Level4 and burger4y4 > Level4:#if the top bun should fall to the 3rd floor, adds 50 score if it is true
    if Burger4Level == 4:
      burger4y1 = Level3
      burger4y4 = Level3
      burger4y2 = Level3
      burger4y3 = Level3
      Burger4Level = 3
      Score+=50
      
  if burger4y1 > Level3 and burger4y2 > Level3 and burger4y3 > Level3 and burger4y4 > Level3:#if the top bun should fall to the 2nd floor, adds 50 score if it is true
    if Burger4Level == 3:
      burger4y1 = Level2
      burger4y4 = Level2
      burger4y2 = Level2
      burger4y3 = Level2
      Burger4Level = 2
      Score+=50
      
  if burger4y1 > Level2 and burger4y2 > Level2 and burger4y3 > Level2 and burger4y4 > Level2:#if the top bun should fall to the 1st floor, adds 50 score if it is true
    if Burger4Level == 2:
      burger4y1 = Level1
      burger4y4 = Level1
      burger4y2 = Level1
      burger4y3 = Level1
      Burger4Level = 1
      Score+=50
      
  if burger4y1 > Level1 and burger4y2 > Level1 and burger4y3 > Level1 and burger4y4 > Level1:#if the top bun should fall to the plate, adds 50 score if it is true
    if Burger4Level == 1:
      burger4y1 = 565
      burger4y4 = 565
      burger4y2 = 565
      burger4y3 = 565
      Burger4Level = 0
      Score+=50
      
  if Burger2Level == 1 and Burger1Level == 1: #if the burgur patty falls on the bottom bun, knocking it down
    burger1y1 = 625
    burger1y2 = 625
    burger1y3 = 625
    burger1y4 = 625
    Burger1Level = 0
    Score+=50
    
  if Burger3Level == 2 and Burger2Level == 2: #if the lettuce falls on the burger patty on floor2, knocking it down to floor 1
    burger2y1 = Level1
    burger2y4 = Level1
    burger2y2 = Level1
    burger2y3 = Level1
    Burger2Level = 1
    Score+=50
    
  if Burger3Level == 1 and Burger2Level == 1:  #if the lettuce falls on the burger patty on floor1, knocking it down to the plate
    burger2y1 = 605
    burger2y4 = 605
    burger2y2 = 605
    burger2y3 = 605
    Burger2Level = 0
    Score+=50
    
  if Burger4Level == 3 and Burger3Level == 3: #if the top bun falls on the lettuce on floor 3, it knocks the lettuce down to floor 2
    burger3y1 = Level2
    burger3y4 = Level2
    burger3y2 = Level2
    burger3y3 = Level2
    Burger3Level = 2
    Score+=50
    
  if Burger4Level == 2 and Burger3Level == 2:#if the top bun falls on the lettuce on floor 2, it knocks the lettuce down to floor 1
    burger3y1 = Level1
    burger3y4 = Level1
    burger3y2 = Level1
    burger3y3 = Level1
    Burger3Level = 1
    Score+=50
    
  if Burger4Level == 1 and Burger3Level == 1: #if the top bun falls on the lettuce on floor 1, it knocks the lettuce down to the plate
    burger3y1 = 585
    burger3y4 = 585
    burger3y2 = 585
    burger3y3 = 585
    Burger3Level = 0
    Score+=50

  if Burger1Level == 0 and Burger2Level == 0 and Burger3Level == 0 and Burger4Level == 0: #if the burger is completed, it adds 500 score
    Score+=500
    Burger1Level = -1
    Burger2Level = -1
    Burger3Level = -1
    Burger4Level = -1

  if Burger1Level == -1: #if the game is won, it displays the winning text
    WINDOW.blit(Winning, (50, 300))

  if x >= 60 and x <= 130: #if the game is lost, these detect if the player has coordinates close enough to the enemy
    if y>= Ey-45 and y<=Ey+45:
      GameLost=True

  if GameLost == True:#if the game is lost, it plays the animation of the player dying
    #WINDOW.blit(Losing, (50, 300))
    LostCostumeInc = 1

    if LostCostume <=40:#1st costume
      WINDOW.blit(SpriteSheet, (x, y), (188, 45, 44, 44))
  
    elif LostCostume <= 50:#2nd costume
      WINDOW.blit(SpriteSheet, (x, y), (232, 46, 47, 44))
  
    elif LostCostume <= 60:#3rd costume
      WINDOW.blit(SpriteSheet, (x, y), (280, 46, 46, 44))
      
    elif LostCostume <= 70:#4th costume
      WINDOW.blit(SpriteSheet, (x, y), (327, 46, 45, 44))
  
    elif LostCostume <=80:#5th costume
      WINDOW.blit(SpriteSheet, (x, y), (375, 46, 46, 44))
  
      if LostCostume == 80:#stops the animation once reached the last costume
        LostCostumeInc = 0

  if LostCostume == 80 and Burger1Level !=-1: #displays the losing screen when the player losing animation is played
    WINDOW.fill(BLACK)
    WINDOW.blit(Losing, (50, 300))
    pygame.draw.rect(WINDOW, WHITE, (498, 0, 2, 680), 0)#right wall line
    pygame.draw.rect(WINDOW, WHITE, (0, 0, 2, 680), 0)#left wall line
    pygame.draw.rect(WINDOW, WHITE, (0, 678, 500, 2), 0)#bottom wall line
    
  #barriers:
  #bottom/top platform barrier horizontal barriers
  if y == 460 or y == 67 and GameLost == False:
    if x <= 455 and x >= 0:
      x+=xinc #adds velocity of x to x
      L+=Linc #starts walking left animation if it should
      R+=Rinc #starts walking right animation if it should
      
    else:
      if x >= 455:
        x-=1
        L = 1
        R = 1
        
      else:
        x+=1
        L = 1
        R = 1

  #middle platform horizontal barrier
  elif y == 325 and GameLost == False:
    if x >= 99 and x <= 355:
      x+=xinc #adds velocity of x to x
      L+=Linc #starts walking left animation if it should
      R+=Rinc #starts walking right animation if it should
  
    else:
      if x >= 355 and x <= 360:
        x-=1
        L = 1
        R = 1
        
      elif x <= 99 and x >= 20:
        x+=1
        L = 1
        R = 1
        
  #left platform horizontal barrier
  elif y == 220 and GameLost == False:
    if x >= 0 and x <= 223:
      x+=xinc #adds velocity of x to x
      L+=Linc #starts walking left animation if it should
      R+=Rinc #starts walking right animation if it should
  
    else:
      if x >= 224 and x<= 229:
        x-=1
        L = 1
        R = 1
        
      elif x <= 0:
        x+=1
        L = 1
        R = 1
        
  #right platform horizontal barrier
  elif y == 155 and GameLost == False:
    if x >= 223 and x <= 455:
      x+=xinc #adds velocity of x to x
      L+=Linc #starts walking left animation if it should
      R+=Rinc #starts walking right animation if it should
  
    else:
      if x >= 455:
        x-=1
        L = 1
        R = 1
        
      elif x <= 223 and x >=215:
        x+=1
        L = 1
        R = 1
        
  #1st big ladder vertical barriers
  if x >= 93 and x <= 103 and GameLost == False:
    if y <= 460 and y >= 67:
      y+=yinc #adds velocity of y to y
      U+=Uinc #starts walking up animation if it should
      D+=Dinc #starts walking down animation if it should 
    
    else:
      if y <= 67:
        y+=1
        U = 8
        D = 7
    
      elif y >= 460:
        y-=1
        U = 7
        D = 7
        
  #2nd big ladder vertical barriers
  elif x >= 217 and x <= 227 and GameLost == False:
    if y <= 460 and y >= 67:
      y+=yinc #adds velocity of y to y
      U+=Uinc #starts walking up animation if it should
      D+=Dinc #starts walking down animation if it should 
    
    else:
      if y <= 67:
        y+=1
        U = 8
        D = 7
    
      elif y >= 460:
        y-=1
        U = 7
        D = 7
        
  #3rd big ladder vertical barriers
  elif x >= 343 and x <= 353 and GameLost == False: 
    if y <= 460 and y >= 67:
      y+=yinc #adds velocity of y to y
      U+=Uinc #starts walking up animation if it should
      D+=Dinc #starts walking down animation if it should 
    
    else:
      if y <= 67:
        y+=1
        U = 8
        D = 7
    
      elif y >= 460:
        y-=1
        U = 7
        D = 7

  #1st small ladder vertical barrier:
  elif x >= 0 and x <= 10 and GameLost == False:
    if y <= 460 and y >= 220:
      y+=yinc #adds velocity of y to y
      U+=Uinc #starts walking up animation if it should
      D+=Dinc #starts walking down animation if it should 
    
    else:
      if y <= 265 and y>=275:
        y+=1
        U = 8
        D = 7
    
      elif y >= 460:
        y-=1
        U = 7
        D = 7

  #2nd small ladder vertical barrier:
  elif x >= 155 and x <= 165 and GameLost == False:#2nd small ladder barrier
    if y <= 220 and y >= 67:
      y+=yinc #adds velocity of y to y
      U+=Uinc #starts walking up animation if it should
      D+=Dinc #starts walking down animation if it should 
    
    else:
      if y <= 67:
        y+=1
        U = 8
        D = 7
    
      elif y >= 220 and y<=225:
        y-=1
        U = 7
        D = 7

  elif x >= 278 and x <= 288 and GameLost == False:#3rd small ladder vertical barrier
    if y <= 325 and y >=  155:
      y+=yinc #adds velocity of y to y
      U+=Uinc #starts walking up animation if it should
      D+=Dinc #starts walking down animation if it should 
    
    else:
      if y <= 155 and y >= 145:
        y+=1
        U = 8
        D = 7
    
      elif y >= 325 and y<=335:
        y-=1
        U = 7
        D = 7

  elif x >= 447 and x <= 455 and GameLost == False:#4th small ladder vertical barrier
    if y <= 460 and y >= 155:
      y+=yinc #adds velocity of y to y
      U+=Uinc #starts walking up animation if it should
      D+=Dinc #starts walking down animation if it should 
    
    else:
      if y <= 155 and y>=145:
        y+=1
        U = 8
        D = 7
    
      elif y > 460:
        y-=1
        U = 7
        D = 7


  #if the game is not lost, it still moves the enemy
  if GameLost == False:
    Ey+=Eyinc
    E+=Einc

  LostCostume+=LostCostumeInc#adds the animation for the costume if the game is lost, if the game is lost, it will start adding because the LostCostumeInc will be set to 1

  pygame.display.update() #redraws after the loop.
  fpsClock.tick(FPS)