import pygame
import time
import random
import sys


#This sets the colour black using the rgb colour codes
black = (0,0,0)
#This sets the colour white using the rgb colour codes
white = (255,255,255)
#This sets the colour green using the rgb colour codes
green = (0,128,0)
#This sets the colour red using rgb colour codes
red = (100,00,00)
#This sets the colour bright red using rgb colour codes
bright_red = (255,0,0)
#This sets the colour bright green using rgb colour codes
bright_green = (0,255,0)

#This sets the variable car_width to 40 pixels wide
car_width = 40
#This sets the variable car_height to 40 pixels high
car_height = 40


#This starts the clock and changes the variable to clock
clock = pygame.time.Clock()
    
#This loads the image 'Block' into pygame
carImg = pygame.image.load('block.jpg')


#This draws the car onto the pygame display
def car(x,y):
    gameDisplay.blit(carImg,(x,y))


#This intitiates the pygame sequence
pygame.init()
#This sets the caption on the screen to Maze Game
pygame.display.set_caption('Maze Game')

gameIcon = pygame.image.load('block.jpg')
pygame.display.set_icon(gameIcon)


#This sets the variable display_width to 800 and sets the other variable display_height to 600
display_width = 800
display_height = 600
#This will set gameDisplay to display_width * display_height
gameDisplay = pygame.display.set_mode((display_width,display_height))
#This sets the colour green using rgb colour codes
Green = (20,215,65)
#This sets the colour red using rgb colour codes
Red = (100,00,00)

#This creates the class LevelOneBlocks and is used to create defintions specifically to those blocks
class Blocks:
    # Initializer / Instance Attributes. This creates initial attributes of BlockNumber, BlockXStart, BlockYStart,BlockWidth and BlockHeight specific to LevelOneBlocks
    def __init__(self, BlockNumber, BlockXStart, BlockYStart, BlockWidth, BlockHeight,):
        self.BlockNumber = BlockNumber
        self.BlockXStart = BlockXStart
        self.BlockYStart = BlockYStart
        self.BlockWidth = BlockWidth
        self.BlockHeight = BlockHeight
    #This is the draw function that will create blocks specific to level one blocks
    def BlockDraw(self):
        pygame.draw.rect(gameDisplay,Green,(self.BlockXStart,self.BlockYStart,self.BlockWidth,self.BlockHeight))
    #This is a draw function that is specific to the final EndGameBlock
    def EndBlockDraw(self):
        pygame.draw.rect(gameDisplay,Red,(self.BlockXStart,self.BlockYStart,self.BlockWidth,self.BlockHeight))
    #This is the crossover function for all the level one blocks to make sure that the blocks physically exist and aren't just drawn there.
    def Crossover(self):
        #This adds self.BlockWidth and self.BlockXStart to create the variable BlockXCrossover
        BlockXCrossover = self.BlockWidth + self.BlockXStart
        #This adds self.BlockHeight and self.BlockYStart to create the variable BlockYCrossover
        BlockYCrossover = self.BlockHeight + self.BlockYStart
        #This will continue the code if x is less than BlockXCrossover and y is less than BlockYCrossover
        if x < BlockXCrossover and y < BlockYCrossover:
            #This will continue the code if BlockYStart + 60 is greater than y which is greater than BlockYStart - 20.
            if self.BlockYStart + 60 > y > self.BlockYStart - 20:
                #This will continue the code if x is greater than blockxstart and x is less than blockystart + blockwidth blockYstart + BlockWidth or x+ car_width is greater than BlockXStart and x+ car_width is less than BlockXstart +BlockWidth
                if x > self.BlockXStart and x < self.BlockYStart + self.BlockWidth or x+car_width > self.BlockXStart and x + car_width < self.BlockXStart+self.BlockWidth:
                    #This will print 'XCrossover1 with Block' and the number that has been inputed for that block
                    print("XCrossover1 with Block{}".format(self.BlockNumber))
                    #This runs the crash sequence
                    crash()
                #This will continue the code else if x is greater than BlockXStart and x is greater than BlockYStart + BlockWidth or x - Car_width is greater than BlockXStart - BlockWidth
                elif x > self.BlockXStart and x > self.BlockYStart + self.BlockWidth or x-car_width >self.BlockXStart and x - car_width > self.BlockXStart-self.BlockWidth:
                    #This will print 'XCrossover2 with Block' and the number that has been inputed for that block
                    print("XCrossover2 with Block{}".format(self.BlockNumber))
                    #This runs the crash sequence
                    crash()
            #This will continue the code is BlockXStart +60 is greater than x and x is greater than BlockXStart -20
            elif self.BlockXStart + 60 > x > self.BlockXStart - 20:
                #This will continue the code is y is greater than BlockYStart and y is greater than BlockYStart - BlockHeight or y+car_height is greater than BlockYStart and y+car_height is less than BlockYStart +BlockHeight
                if y > self.BlockYStart and  y > self.BlockYStart - self.BlockHeight or y+car_height > self.BlockYStart and y+car_height < self.BlockYStart+self.BlockHeight:
                    #This will print 'YCrossover1 with Block' and the number that has been inputed for that block
                    print("YCrossover1 with Block{}".format(self.BlockNumber))
                    #This runs the crash sequence
                    crash()
                #This will continue the code is y is greater than BlockYStart and y is less than BlockYStart + BlockHeight or y+car_height is greater than BlockYStart and y+car_height is less than BlockYStart +BlockHeight
                elif y > self.BlockYStart and  y < self.BlockYStart + self.BlockHeight or y+car_height > self.BlockYStart and y+car_height < self.BlockYStart+self.BlockHeight:
                    #This will print 'YCrossover2 with Block' and the number that has been inputed for that block
                    print("YCrossover1 with Block{}".format(self.BlockNumber))
                    #This runs the crash sequence
                    crash()

                 
                
    #This is the end crossover function which will change to the next l;evel if the car hits the block.
    def EndCrossover1(self):
        #This creates the variable BlockXCrossover by adding blockwidth and blockxstart together
        BlockXCrossover = self.BlockWidth + self.BlockXStart
        #This creates the variable BlockYCrossover by adding BlockHeight and BlockYStart together
        BlockYCrossover = self.BlockHeight + self.BlockYStart
        #This globalises the variables LevelOneChecker, LevelOneOver and LevelTwoOver so that they can be used outside the function
        global LevelOneChecker
        global LevelOneOver
        global LevelTwoOver
        #This continues the function if LevelOneChecker = 10
        if LevelOneChecker > 10:
            #This sets LevelOneChecker to 0
            LevelOneChecker = 0
            #This continues the code is x is less than BlockXCrossover and y is less than BlockYCrossover
            if x < BlockXCrossover and y < BlockYCrossover:
                #This will continue the code if BlockYStart + 60 is greater than y which is greater than BlockYStart - 20.
                if self.BlockYStart + 60 > y > self.BlockYStart - 20:
                    #This will continue the code if x is greater than blockxstart and x is less than blockystart + blockwidth blockYstart + BlockWidth or x+ car_width is greater than BlockXStart and x+ car_width is less than BlockXstart +BlockWidth
                    if x > self.BlockXStart and x < self.BlockYStart + self.BlockWidth or x+car_width > self.BlockXStart and x + car_width < self.BlockXStart+self.BlockWidth:
                        #This will print 'XCrossover1 with EndBlock' and the number that has been inputed for that block
                        print("XCrossover1 with EndBlock{}".format(self.BlockNumber))
                        #This stops the code for 100 milliseconds
                        pygame.time.delay(100)
                        #This adds one to LevelOneOver
                        LevelOneOver += 1
                        #This adds one to LevelTwoOver
                        LevelTwoOver += 1
                        #This runs the EndLevel function
                        EndLevel()
                    #This will continue the code else if x is greater than BlockXStart and x is greater than BlockYStart + BlockWidth or x - Car_width is greater than BlockXStart - BlockWidth
                    elif x > self.BlockXStart and x > self.BlockYStart + self.BlockWidth or x-car_width < self.BlockXStart and x - car_width > self.BlockXStart-self.BlockWidth:
                        #This will print 'XCrossover2 with EndBlock' and the number that has been inputed for that block
                        print("XCrossover2 with EndBlock{}".format(self.BlockNumber))
                        #This stops the code for 100 milliseconds
                        pygame.time.delay(100)
                        #This adds one to LevelOneOver
                        LevelOneOver += 1
                        #This adds one to LevelTwoOver
                        LevelTwoOver += 1
                        #This runs the EndLevel function
                        EndLevel()
                #This will continue the code is BlockXStart +60 is greater than x and x is greater than BlockXStart -20
                elif self.BlockXStart + 60 > x > self.BlockXStart - 20:
                    #This will continue the code is y is greater than BlockYStart and y is greater than BlockYStart - BlockHeight or y+car_height is greater than BlockYStart and y+car_height is less than BlockYStart +BlockHeight
                    if y > self.BlockYStart and  y > self.BlockYStart - self.BlockHeight or y+car_height > self.BlockYStart and y+car_height < self.BlockYStart+self.BlockHeight:
                        #This will print 'YCrossover1 with EndBlock' and the number that has been inputed for that block
                        print("YCrossover1 with EndBlock{}".format(self.BlockNumber))
                        #This stops the code for 100 milliseconds
                        pygame.time.delay(100)
                        #This adds one to LevelOneOver
                        LevelOneOver += 1
                        #This adds one to LevelTwoOver
                        LevelTwoOver += 1
                        #This runs the EndLevel function
                        EndLevel()
                    #This will continue the code is y is greater than BlockYStart and y is less than BlockYStart + BlockHeight or y+car_height is greater than BlockYStart and y+car_height is less than BlockYStart +BlockHeight
                    elif y > self.BlockYStart and  y < self.BlockYStart + self.BlockHeight or y+car_height > self.BlockYStart and y+car_height < self.BlockYStart+self.BlockHeight:
                        #This will print 'YCrossover2 with EndBlock' and the number that has been inputed for that block
                        print("YCrossover2 with EndBlock{}".format(self.BlockNumber))
                        #This stops the code for 100 milliseconds
                        pygame.time.delay(100)
                        #This adds one to LevelOneOver
                        LevelOneOver += 1
                        #This adds one to LevelTwoOver
                        LevelTwoOver += 1
                        #This runs the EndLevel function
    #This is the end crossover function which will change to the next l;evel if the car hits the block.
    def EndCrossover2(self):
        #This creates the variable BlockXCrossover by adding blockwidth and blockxstart together
        BlockXCrossover = self.BlockWidth + self.BlockXStart
        #This creates the variable BlockYCrossover by adding BlockHeight and BlockYStart together
        BlockYCrossover = self.BlockHeight + self.BlockYStart
        #This globalises the variables LevelTwoChecker, LevelTwoOver and LevelThreeOver so that they can be used outside the function
        global LevelTwoChecker
        global LevelTwoOver
        global LevelThreeOver
         #This continues the function if LevelOneChecker = 10
        if LevelTwoChecker > 10:
            #This sets LevelOneChecker to 0
            LevelTwoChecker = 0
            #This continues the code is x is less than BlockXCrossover and y is less than BlockYCrossover
            if x < BlockXCrossover and y < BlockYCrossover:
                #This will continue the code if BlockYStart + 60 is greater than y which is greater than BlockYStart - 20.
                if self.BlockYStart + 60 > y > self.BlockYStart - 20:
                    #This will continue the code if x is greater than blockxstart and x is less than blockystart + blockwidth blockYstart + BlockWidth or x+ car_width is greater than BlockXStart and x+ car_width is less than BlockXstart +BlockWidth
                    if x > self.BlockXStart and x < self.BlockYStart + self.BlockWidth or x+car_width > self.BlockXStart and x + car_width < self.BlockXStart+self.BlockWidth:
                        #This will print 'XCrossover1 with EndBlock' and the number that has been inputed for that block
                        print("XCrossover1 with EndBlock{}".format(self.BlockNumber))
                        #This stops the code for 100 milliseconds
                        pygame.time.delay(100)
                        #This adds one to the variable LevelTwoOver
                        LevelTwoOver += 1
                        #This adds one to LevelThreeOver
                        LevelThreeOver += 1
                        #This runs the Info function
                        Info()
                        #This puts the code to sleep for 2 seconds
                        time.sleep(2)
                        #This runs the EndLevel function
                        EndLevel()
                    #This will continue the code else if x is greater than BlockXStart and x is greater than BlockYStart + BlockWidth or x - Car_width is greater than BlockXStart - BlockWidth
                    elif x > self.BlockXStart and x > self.BlockYStart + self.BlockWidth or x-car_width < self.BlockXStart and x - car_width > self.BlockXStart-self.BlockWidth:
                        #This will print 'XCrossover1 with EndBlock' and the number that has been inputed for that block
                        print("XCrossover1 with EndBlock{}".format(self.BlockNumber))
                        #This stops the code for 100 milliseconds
                        pygame.time.delay(100)
                        #This adds one to the variable LevelTwoOver
                        LevelTwoOver += 1
                        #This adds one to LevelThreeOver
                        LevelThreeOver += 1
                        #This runs the Info function
                        Info()
                        #This puts the code to sleep for 2 seconds
                        time.sleep(2)
                        #This runs the EndLevel function
                        EndLevel()
                #This will continue the code is BlockXStart +60 is greater than x and x is greater than BlockXStart -20
                elif self.BlockXStart + 60 > x > self.BlockXStart - 20:
                    #This will continue the code is y is greater than BlockYStart and y is greater than BlockYStart - BlockHeight or y+car_height is greater than BlockYStart and y+car_height is less than BlockYStart +BlockHeight
                    if y > self.BlockYStart and  y > self.BlockYStart - self.BlockHeight or y+car_height > self.BlockYStart and y+car_height < self.BlockYStart+self.BlockHeight:
                        #This will print 'XCrossover1 with EndBlock' and the number that has been inputed for that block
                        print("XCrossover1 with EndBlock{}".format(self.BlockNumber))
                        #This stops the code for 100 milliseconds
                        pygame.time.delay(100)
                        #This adds one to the variable LevelTwoOver
                        LevelTwoOver += 1
                        #This adds one to LevelThreeOver
                        LevelThreeOver += 1
                        #This runs the Info function
                        Info()
                        #This puts the code to sleep for 2 seconds
                        time.sleep(2)
                        #This runs the EndLevel function
                        EndLevel()
                    #This will continue the code is y is greater than BlockYStart and y is less than BlockYStart + BlockHeight or y+car_height is greater than BlockYStart and y+car_height is less than BlockYStart +BlockHeight
                    elif y > self.BlockYStart and  y < self.BlockYStart + self.BlockHeight or y+car_height > self.BlockYStart and y+car_height < self.BlockYStart+self.BlockHeight:
                        #This will print 'XCrossover1 with EndBlock' and the number that has been inputed for that block
                        print("XCrossover1 with EndBlock{}".format(self.BlockNumber))
                        #This stops the code for 100 milliseconds
                        pygame.time.delay(100)
                        #This adds one to the variable LevelTwoOver
                        LevelTwoOver += 1
                        #This adds one to LevelThreeOver
                        LevelThreeOver += 1
                        #This runs the Info function
                        Info()
                        #This puts the code to sleep for 2 seconds
                        time.sleep(2)
                        #This runs the EndLevel function
                        EndLevel()
    #This is the end crossover function which will change to the next l;evel if the car hits the block.
    def EndCrossover3(self):
        #This creates the variable BlockXCrossover by adding blockwidth and blockxstart together
        BlockXCrossover = self.BlockWidth + self.BlockXStart
        #This creates the variable BlockYCrossover by adding BlockHeight and BlockYStart together
        BlockYCrossover = self.BlockHeight + self.BlockYStart
        #This globalises the variables LevelTwoChecker, LevelTwoOver and LevelThreeOver so that they can be used outside the function
        global LevelThreeChecker
        global LevelThreeOver
         #This continues the function if LevelOneChecker = 10
        if LevelThreeChecker > 10:
            #This sets LevelOneChecker to 0
            LevelThreeChecker = 0
            
            #This continues the code is x is less than BlockXCrossover and y is less than BlockYCrossover
            if x < BlockXCrossover and y < BlockYCrossover:
                #This will continue the code if BlockYStart + 60 is greater than y which is greater than BlockYStart - 20.
                if self.BlockYStart + 60 > y > self.BlockYStart - 20:
                    #This will continue the code if x is greater than blockxstart and x is less than blockystart + blockwidth blockYstart + BlockWidth or x+ car_width is greater than BlockXStart and x+ car_width is less than BlockXstart +BlockWidth
                    if x > self.BlockXStart and x < self.BlockYStart + self.BlockWidth or x+car_width > self.BlockXStart and x + car_width < self.BlockXStart+self.BlockWidth:
                        #This will print 'XCrossover1 with EndBlock' and the number that has been inputed for that block
                        print("XCrossover1 with EndBlock{}".format(self.BlockNumber))
                        #This will delay the code from running for 100 milliseconds
                        pygame.time.delay(100)
                        #This adds one to the variable LevelThreeOver
                        LevelThreeOver += 1
                        #This runs the EndLevel function
                        EndLevel()
                        #This runs the WinGame function
                        WinGame()
                    #This will continue the code else if x is greater than BlockXStart and x is greater than BlockYStart + BlockWidth or x - Car_width is greater than BlockXStart - BlockWidth
                    elif x > self.BlockXStart and x > self.BlockYStart + self.BlockWidth or x-car_width < self.BlockXStart and x - car_width > self.BlockXStart-self.BlockWidth:
                        #This will print 'XCrossover2 with EndBlock' and the number that has been inputed for that block
                        print("XCrossover2 with EndBlock{}".format(self.BlockNumber))
                        #This will delay the code from running for 100 milliseconds
                        pygame.time.delay(100)
                        #This adds one to the variable LevelThreeOver
                        LevelThreeOver += 1
                        #This runs the EndLevel function
                        EndLevel()
                        #This runs the WinGame function
                        WinGame()
                #This will continue the code is BlockXStart +60 is greater than x and x is greater than BlockXStart -20
                elif self.BlockXStart + 60 > x > self.BlockXStart - 20:
                    #This will continue the code is y is greater than BlockYStart and y is greater than BlockYStart - BlockHeight or y+car_height is greater than BlockYStart and y+car_height is less than BlockYStart +BlockHeight
                    if y > self.BlockYStart and  y > self.BlockYStart - self.BlockHeight or y+car_height > self.BlockYStart and y+car_height < self.BlockYStart+self.BlockHeight:
                        #This will print 'XCrossover2 with EndBlock' and the number that has been inputed for that block
                        print("YCrossover1 with EndBlock{}".format(self.BlockNumber))
                        #This will delay the code from running for 100 milliseconds
                        pygame.time.delay(100)
                        #This adds one to the variable LevelThreeOver
                        LevelThreeOver += 1
                        #This runs the EndLevel function
                        EndLevel()
                        #This runs the WinGame function
                        WinGame()
                    #This will continue the code is y is greater than BlockYStart and y is less than BlockYStart + BlockHeight or y+car_height is greater than BlockYStart and y+car_height is less than BlockYStart +BlockHeight
                    elif y > self.BlockYStart and  y < self.BlockYStart + self.BlockHeight or y+car_height > self.BlockYStart and y+car_height < self.BlockYStart+self.BlockHeight:
                        #This will print 'XCrossover2 with EndBlock' and the number that has been inputed for that block
                        print("YCrossover1 with EndBlock{}".format(self.BlockNumber))
                        #This will delay the code from running for 100 milliseconds
                        pygame.time.delay(100)
                        #This adds one to the variable LevelThreeOver
                        LevelThreeOver += 1
                        #This runs the EndLevel function
                        EndLevel()
                        #This runs the WinGame function
                        WinGame()
                        

#This sets the variables for all the level one blocks with the pattern (BlockNumber,BlockXStart,BlockYStart,BlockWidth,BlockHeight)
#############################################################
LevelOneBlock1 = Blocks(1,1, 1, 800, 25)
LevelOneBlock2 = Blocks(2,1, 25, 25, 600)
LevelOneBlock3 = Blocks(3,775, 0, 25, 600)
LevelOneBlock4 = Blocks(4,425, 0, 25, 250)
LevelOneBlock5 = Blocks(5,300, 25, 25, 500)
LevelOneBlock6 = Blocks(6,200, 150, 25, 625)
LevelOneBlock7 = Blocks(7,425, 340, 25, 300)
LevelOneBlock8 = Blocks(8,1, 575, 800, 25)
LevelOneBlock9 = Blocks(9,100, 25, 25, 300)
LevelOneBlock10 = Blocks(10,100, 375, 25, 145)
LevelOneBlock11 = Blocks(11,125, 375, 100, 25)
LevelOneBlock12 = Blocks(12,600,200,200,25)
LevelOneBlock13 = Blocks(13,500,25,25,400)
LevelOneBlock14 = Blocks(14,500,500,300,25)
LevelOneBlock15 = Blocks(15,600,300,25,200)
LevelOneBlock16 = Blocks(16,700,200,25,200)
EndGameBlockOne = Blocks(1,715, 25, 60, 175)
#This sets the variables for all the level two blocks with the pattern (BlockNumber,BlockXStart,BlockYStart,BlockWidth,BlockHeight)
##################################################################
LevelTwoBlock1 = Blocks(1,1, 1, 800, 25)
LevelTwoBlock2 = Blocks(2,1, 25, 25, 600)
LevelTwoBlock3 = Blocks(3,1, 575, 800, 25)
LevelTwoBlock4 = Blocks(4,775, 0, 25, 600)
LevelTwoBlock5 = Blocks(5,600,200,200,25)
LevelTwoBlock6 = Blocks(6,500,25,25,200)
LevelTwoBlock7 = Blocks(7,75,400,25,300)
LevelTwoBlock8 = Blocks(8,25,300,300,25)
LevelTwoBlock9 = Blocks(9,175,300,25,200)
LevelTwoBlock10 = Blocks(10,275,400,25,300)
LevelTwoBlock11 = Blocks(11,400,25,25,300)
LevelTwoBlock12 = Blocks(12,600,300,200,25)
LevelTwoBlock13 = Blocks(13,400,300,125,25)
LevelTwoBlock14 = Blocks(14,600,325,25,175)
LevelTwoBlock15 = Blocks(15,450,325,25,175)
LevelTwoBlock16 = Blocks(16,687.5,400,25,175)
LevelTwoBlock17 = Blocks(17,250,125,150,25)
LevelTwoBlock18 = Blocks(18,250,225,25,75)
LevelTwoBlock19 = Blocks(19,150,225,100,25)
LevelTwoBlock20 = Blocks(20,150,150,25,75)
LevelTwoBlock21 = Blocks(21,125,125,50,25)
LevelTwoBlock22 = Blocks(22,125,75,25,75)
LevelTwoBlock23 = Blocks(23,25,200,75,25)
EndGameBlockTwo = Blocks(2,25, 525, 50, 50)
#This sets the variables for all the level three blocks with the pattern (BlockNumber,BlockXStart,BlockYStart,BlockWidth,BlockHeight)
#############################################################
LevelThreeBlock1 = Blocks(1,1, 1, 800, 25)
LevelThreeBlock2 = Blocks(2,1, 25, 25, 600)
LevelThreeBlock3 = Blocks(3,775, 0, 25, 600)
LevelThreeBlock4 = Blocks(4,425, 0, 25, 250)
LevelThreeBlock5 = Blocks(5,300, 25, 25, 500)
LevelThreeBlock6 = Blocks(6,200, 150, 25, 625)
LevelThreeBlock7 = Blocks(7,425, 340, 25, 300)
LevelThreeBlock8 = Blocks(8,1, 575, 800, 25)
LevelThreeBlock9 = Blocks(9,100, 25, 25, 300)
LevelThreeBlock10 = Blocks(10,100, 375, 25, 145)
LevelThreeBlock11 = Blocks(11,125, 375, 100, 25)
LevelThreeBlock12 = Blocks(12,600,200,200,25)
LevelThreeBlock13 = Blocks(13,500,25,25,400)
LevelThreeBlock14 = Blocks(14,500,500,300,25)
LevelThreeBlock15 = Blocks(15,600,300,25,200)
LevelThreeBlock16 = Blocks(16,700,200,25,200)
EndGameBlockThree = Blocks(3,715, 25, 60, 175)
#This is the game_intro function this is used to create the main menu screen.
def game_intro():
    #This sets the variable intro to true
    intro = True
    #This is a while loop which will continue running until intro = false
    while intro:
        for event in pygame.event.get():
            #This will quit both pygame and the python shell when the x button is pressed.
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        #This fills the screen with a white background        
        gameDisplay.fill(white)
        #This sets the variable LargeText to the font Comicsansms at a font size of 115
        largeText = pygame.font.SysFont("comicsansms",115)
        #This sets the text that will be rendered is Maze Game with what is set for largetext.
        TextSurf, TextRect = text_objects("Maze Game", largeText)
        #This makes sure that the text will render in the middle
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        #This runs the button function with the words go and quit which will turn bright green and bright red when the mouse hovers over them. This will also run GameLoop if there is a mouse click on the go button. It will run the quitgame function if you mouseclick on the quit button.
        button("GO!",150,450,100,50,green,bright_green,GameLoop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        #This updates the pygame display screen
        pygame.display.update()
        #This sets the frame rate to 15 frames
        clock.tick(15)

#This is the button function which is used on the main screen to continue or quite the game.
def button(msg,x,y,w,h,ic,ac,action=None):
    #This gets the mouse positon
    mouse = pygame.mouse.get_pos()
    #This will set click to whether or not it is being pressed or not
    click = pygame.mouse.get_pressed()
    #This will print whether or not it clicks to the python shell
    print(click)
    #This will turn the buttons bright green and bright red if the mouse hovers over the buttons. 
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        #If click equals 1 and action = none then it will run the action function.
        if click[0] == 1 and action != None:
            action()         
    #If this doesn't meet the if statement requirements it will just print the buttons as green or red.
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    #This sets small text to comicsansms and at a font size of 20
    smallText = pygame.font.SysFont("comicsansms",20)
    #This sets the text that will be rendered is msg with what is set for smalltext
    textSurf, textRect = text_objects(msg, smallText)
    #This sets the place where the text will draw in the center of the buttons.
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

#This is the quitgame function which is used to quit the game
def quitgame():
    pygame.quit()
    quit()

#This is the EndLevel function which is used to clear the sceen after each level
def EndLevel():
    #This puts a white background and then draws the car after
    gameDisplay.fill(white)

    #This will render the car on the pygame display
    car(x,y)        

#This is used to render the text on the pygame window 
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

#This is where we set the font size, font and set the location to the centre for message_display
def message_display(text):
    #This sets the variable largeText to the font freesansbold and a font size of 115
    largeText = pygame.font.Font('freesansbold.ttf',115)
    #This sets the text which will be rendered to the largeText inputs
    TextSurf, TextRect = text_objects(text, largeText)
    #This renders the text into the center of the screen
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    #This will update the pygame display
    pygame.display.update()
    #This stops the code for 2 seconds
    time.sleep(2)

#This is where we set the font size, font and set the location to the centre for small_message_display
def small_message_display(text):
    #This sets the variable largeText to the font freesansbold and a font size of 115
    largeText = pygame.font.Font('freesansbold.ttf',45)
    #This sets the text which will be rendered to the largeText inputs
    TextSurf, TextRect = text_objects(text, largeText)
    #This renders the text into the center of the screen
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    #This will update the pygame display
    pygame.display.update()
    #This stops the code for 2 seconds
    time.sleep(2)

#This is used to unpause the game
def unpause():
    #This globalises the variable pause
    global pause
    #This sets pause to false
    pause = False

#This is the function used to pause the game.
def paused():
    #This sets the variable largeText to the font freesansbold and a font size of 115
    largeText = pygame.font.Font('freesansbold.ttf',115)
    #This sets the Pause which will be rendered to the largeText inputs
    TextSurf, TextRect = text_objects("Pause", largeText)
    #This renders the text into the center of the screen
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    #This loop will run while the variable pause=False
    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        
        #This runs the button function with the words go and quit which will turn bright green and bright red when the mouse hovers over them. This will also run Unpause if there is a mouse click on the go button. It will run the quitgame function if you mouseclick on the quit button.
        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("Quit",550,450,100,50,red,bright_red,quitgame)
        #This will update the pygame display
        pygame.display.update()
        #This will set the frame rate to 15 frames per second
        clock.tick(15)  

#This will display the message 'You Crashed
def crash():
    #This sets the variable largeText to the font freesansbold and a font size of 115
    largeText = pygame.font.Font('freesansbold.ttf',115)
    #This sets the You Crashed which will be rendered to the largeText inputs
    TextSurf, TextRect = text_objects("You Crashed", largeText)
    #This renders the text into the center of the screen
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    #This will continuously run the function while True 
    while True:
        for event in pygame.event.get():
            #This will quit pygame and the python shell when the x button is pressed
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                

        
        #This runs the button function with the words go and quit which will turn bright green and bright red when the mouse hovers over them. This will also run GameLoop if there is a mouse click on the go button. It will run the quitgame function if you mouseclick on the quit button.
        button("Play Again",150,450,100,50,green,bright_green,GameLoop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)
        #This will update the pygame screen 
        pygame.display.update()
        #This sets the frame rate to 15ps
        clock.tick(15)

#This is for where you win the game and will print You Win
def WinGame():

    message_display('You Win')
    #This puts the code to sleep for 5 seconds
    time.sleep(5)
    #This runs the quitGame function
    quitgame()

#This is the info function which is to ask you if you remember level one
def Info():
    EndLevel()
    small_message_display('Do You Remember Level One?')

#This is the GameLoop where it is continuously running and is the main code
def GameLoop():
    #This globalises x,y,LevelOneChecker,LevelTwoChecker,LevelThreeChecker,LevelOneOver,LevelTwoOver,LevelThreeOver and pause.
    global x,y
    global LevelOneChecker
    global LevelTwoChecker
    global LevelThreeChecker
    global LevelOneOver
    global LevelTwoOver
    global LevelThreeOver
    global pause
    #This defines the points for where the car is going to spawn  
    x = (display_width * 0.04)
    y = (display_height * 0.7)
    #This sets these variables to zero
    LevelOneChecker = 0
    LevelTwoChecker = 0
    LevelThreeChecker = 0
    LevelOneOver = 0
    LevelTwoOver = 0
    LevelThreeOver = 0
    x_change = 0
    y_change = 0


    #This sets gameExit as false at the start meaning that it won't break the while not loop
    gameExit = False
    #This is a while not loop which means it will continuously run until it is changed till True
    while not gameExit:
        #If the user presses the x it will exit both pygame and python
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            #If any key is pressed down then it will move onto the other parts of the if statements
            if event.type == pygame.KEYDOWN:
                    
                #If the key that is pressed down is left then it will change the x_change variable to -5 meaning that the car will go left
                if event.key == pygame.K_LEFT:
                    x_change = -5
                #If the key that is pressed down is up then it will change the y_change variable to -5 meaning that the car will go up
                if event.key == pygame.K_UP:
                    y_change = -5
                #If the key that is pressed down is down then it will change the y_change variable to 5 meaning that the car will go down
                if event.key == pygame.K_DOWN:
                    y_change = 5
                    
                #If the key that is pressed down is right then it will change the x_change variable to 5 meaning that the car will go right
                if event.key == pygame.K_RIGHT:
                    x_change = 5
            
                #If the d key is pressed down then the car then it will change the x_change variable by 15 meaning that it will go right  
                if event.key == pygame.K_d:
                    x_change = 15
                #If the a key is pressed down then the car then it will change the x_change variable by -15 meaning that it will go left
                if event.key == pygame.K_a:
                    x_change = -15
                #If the s key is pressed down then the car then it will change the y_change variable by 15 meaning that it will go down
                if event.key == pygame.K_s:
                    y_change = 15
                #If the p key is pressed down then it will pause the game
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                #If the w key is pressed down then the car then it will change the y_change variable by -15 meaning that it will go up
                if event.key == pygame.K_w:
                    y_change = -15
                #If the space key is pressed down then it will take you back to the start of the game
                if event.key == pygame.K_SPACE:
                    gameExit = True
                #If the esc key is pressed down then the pygame window and the python shell will close
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
           
            #If there is no key pressed down then then it won't change the x_change and y _change variable
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0
                if event.key == pygame.K_s or event.key == pygame.K_w:
                    y_change = 0



        #This adds x_change to = x
        x += x_change
        #This adds y_change to x
        y += y_change
        
        
        #This puts a white background and then draws the car after
        gameDisplay.fill(white)
        
        if x > display_width - car_width or x < 0:
            crash()
        if y > display_height - car_height or y < 0:
            crash()
        
        #This will render the car on the pygame display
        car(x,y)

        #This will continue the code if LevelOneOver equals zero
        if LevelOneOver == 0:
            #This runs the blockdraw functions for the individual level one blocks
            LevelOneBlock1.BlockDraw()
            LevelOneBlock2.BlockDraw()
            LevelOneBlock3.BlockDraw()
            LevelOneBlock4.BlockDraw()
            LevelOneBlock5.BlockDraw()
            LevelOneBlock6.BlockDraw()
            LevelOneBlock7.BlockDraw()
            LevelOneBlock8.BlockDraw()
            LevelOneBlock9.BlockDraw()
            LevelOneBlock10.BlockDraw()
            LevelOneBlock11.BlockDraw()
            LevelOneBlock12.BlockDraw()
            LevelOneBlock13.BlockDraw()
            LevelOneBlock14.BlockDraw()
            LevelOneBlock15.BlockDraw()
            LevelOneBlock16.BlockDraw()
            #This runs the endblock draw function for level one
            EndGameBlockOne.EndBlockDraw()
            #This will run the individual level one block crossovers
            LevelOneBlock1.Crossover()
            LevelOneBlock2.Crossover()
            LevelOneBlock3.Crossover()
            LevelOneBlock4.Crossover()
            LevelOneBlock5.Crossover()
            LevelOneBlock6.Crossover()
            LevelOneBlock7.Crossover()
            LevelOneBlock8.Crossover()
            LevelOneBlock9.Crossover()
            LevelOneBlock10.Crossover()
            LevelOneBlock11.Crossover()
            LevelOneBlock12.Crossover()
            LevelOneBlock13.Crossover()
            LevelOneBlock14.Crossover()
            LevelOneBlock15.Crossover()
            LevelOneBlock16.Crossover()
            #This will run the level one end block crossover
            EndGameBlockOne.EndCrossover1()
        #This will continue the code if LevelTwoOver equals one
        if LevelTwoOver == 1:
            #This runs the blockdraw functions for the individual level two blocks
            LevelTwoBlock1.BlockDraw()
            LevelTwoBlock2.BlockDraw()
            LevelTwoBlock3.BlockDraw()
            LevelTwoBlock4.BlockDraw()
            LevelTwoBlock5.BlockDraw()
            LevelTwoBlock6.BlockDraw()
            LevelTwoBlock7.BlockDraw()
            LevelTwoBlock8.BlockDraw()
            LevelTwoBlock9.BlockDraw()
            LevelTwoBlock10.BlockDraw()
            LevelTwoBlock11.BlockDraw()
            LevelTwoBlock12.BlockDraw()
            LevelTwoBlock13.BlockDraw()
            LevelTwoBlock14.BlockDraw()
            LevelTwoBlock15.BlockDraw()
            LevelTwoBlock16.BlockDraw()
            LevelTwoBlock17.BlockDraw()
            LevelTwoBlock18.BlockDraw()
            LevelTwoBlock19.BlockDraw()
            LevelTwoBlock20.BlockDraw()
            LevelTwoBlock21.BlockDraw()
            LevelTwoBlock22.BlockDraw()
            LevelTwoBlock23.BlockDraw()
            #This runs the endblock draw function for level two
            EndGameBlockTwo.EndBlockDraw()
            #This will run the individual level two block crossovers
            LevelTwoBlock1.Crossover()
            LevelTwoBlock2.Crossover()
            LevelTwoBlock3.Crossover()
            LevelTwoBlock4.Crossover()
            LevelTwoBlock5.Crossover()
            LevelTwoBlock6.Crossover()
            LevelTwoBlock7.Crossover()
            LevelTwoBlock8.Crossover()
            LevelTwoBlock9.Crossover()
            LevelTwoBlock10.Crossover()
            LevelTwoBlock11.Crossover()
            LevelTwoBlock12.Crossover()
            LevelTwoBlock13.Crossover()
            LevelTwoBlock14.Crossover()
            LevelTwoBlock15.Crossover()
            LevelTwoBlock16.Crossover()
            LevelTwoBlock17.Crossover()
            LevelTwoBlock18.Crossover()
            LevelTwoBlock19.Crossover()
            LevelTwoBlock20.Crossover()
            LevelTwoBlock21.Crossover()
            LevelTwoBlock22.Crossover()
            LevelTwoBlock23.Crossover()
            #This will run the level two end block crossover
            EndGameBlockTwo.EndCrossover2()
        #This will continue the code if LevelThreeOver equals one
        if LevelThreeOver == 1:
            #This runs the blockdraw functions for the individual level three blocks
            LevelThreeBlock1.BlockDraw()
            LevelThreeBlock2.BlockDraw()
            LevelThreeBlock3.BlockDraw()
            LevelThreeBlock4.BlockDraw()
            LevelThreeBlock5.BlockDraw()
            LevelThreeBlock6.BlockDraw()
            LevelThreeBlock7.BlockDraw()
            LevelThreeBlock8.BlockDraw()
            LevelThreeBlock9.BlockDraw()
            LevelThreeBlock10.BlockDraw()
            LevelThreeBlock11.BlockDraw()
            LevelThreeBlock12.BlockDraw()
            LevelThreeBlock13.BlockDraw()
            LevelThreeBlock14.BlockDraw()
            LevelThreeBlock15.BlockDraw()
            LevelThreeBlock16.BlockDraw()
            #This runs the endblock draw function for level three
            EndGameBlockThree.EndBlockDraw()

            LevelThreeBlock1.Crossover()
            LevelThreeBlock2.Crossover()
            LevelThreeBlock3.Crossover()
            LevelThreeBlock4.Crossover()
            LevelThreeBlock5.Crossover()
            LevelThreeBlock6.Crossover()
            LevelThreeBlock7.Crossover()
            LevelThreeBlock8.Crossover()
            LevelThreeBlock9.Crossover()
            LevelThreeBlock10.Crossover()
            LevelThreeBlock11.Crossover()
            LevelThreeBlock12.Crossover()
            LevelThreeBlock13.Crossover()
            LevelThreeBlock14.Crossover()
            LevelThreeBlock15.Crossover()
            LevelThreeBlock16.Crossover()
            #This will run the level three end block crossover           
            EndGameBlockThree.EndCrossover3()
        
        #This adds one to each of the three variables
        LevelOneChecker += 1
        LevelTwoChecker += 1
        LevelThreeChecker += 1
        #This updates the pygame screen
        pygame.display.update()
        
        #This sets the clock tick rate to 60
        clock.tick(60)

#This initiates the game_loop
game_intro()
GameLoop()




#This quits pygame and then continues to quit python
pygame.quit()
quit()
