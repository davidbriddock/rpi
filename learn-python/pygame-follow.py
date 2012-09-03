# Follow That Mouse - PyGame Animation Program
# Created by David in July
 
import pygame, sys
 
def check_events():
   # loop through all events
   for event in pygame.event.get():
      # window close event?
      if event.type == pygame.QUIT:
         sys.quit()
      # mouse button clicked?
      if event.type == pygame.MOUSEBUTTONDOWN:
         global discCol
         discCol = [255,0,0]   # red
      
def follow():          
   # check events
   check_events()

   # set the screen background
   screen.fill(bgCol)
   
   # get mouse position
   pos = pygame.mouse.get_pos()
   
   # draw a disc at the current mouse position
   pygame.draw.circle(screen, discCol, pos, discRadius)
                  
   # update the screen with what we've drawn
   pygame.display.flip()
   
   # control the draw update speed
   clock.tick(50)

# initialise variables
bgCol = [0,0,0]       # black
discCol = [0,0,255]   # blue
discRadius = 20       # 20 pixels

# initialise pygame
pygame.init()
screen = pygame.display.set_mode([500,400])
pygame.display.set_caption("Follow That Mouse")
clock = pygame.time.Clock()
 
# loop until the user clicks the close button
while True:
   follow()