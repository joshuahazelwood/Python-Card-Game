import pygame
from Characters.constants import WIDTH, HEIGHT, WHITE, BLACK, RED, BLUE, CHARHE, CHARWI
from Backdrops.constants import x, y
from Cpu.constants import AIHE, AIWI
from Cards.constants import deck, attack, shield, W, H, base_energy
from random import seed
from random import randint

FPS = 30


#Displays my window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Deadliest Dungeon")


#Places the images
class imageplacer:
    def imgdim(imagename, t, y ):
        image =  pygame.image.load(imagename)
        
        window.blit(image, (t, y))

#Used to display the 5 randomly chosen cards on the screen.
class cardR:
    def cardrandomizer(count1, count2):
        long = 140
        for _ in range (count1):
            imageplacer.imgdim("Cards/Strike.png", long, 470)
            long += 100
        for _ in range (count2):
            imageplacer.imgdim("Cards/Defend.png", long, 470)
            long += 100

        
def main():
    run = True
    clock = pygame.time.Clock()
    
    #Some variables initialized in the main because 
    #they are constantly changing within the while loop
    CHARHE = 175
    bctr = 0
    bctr2 = 0
    AIHE = 175
    count1, count2 = 0, 0
    seed()
    j = 0

    
    while run:
        clock.tick(FPS)
        pygame.display.update()

        #Constanly changing card choices in case of shuffling needed
        if (j < 5):
            i = 0
            if (i == 0):
                value = randint(0,1)
            if (value == 1):
                count1 += 1
            else:   
                count2 += 1 
            j += 1

        #Bobbing for P1
        if (CHARHE <= 195 and bctr != 15): 
            CHARHE = CHARHE + 1
            bctr += 1
        if (bctr == 15):
            CHARHE = CHARHE - 1
            if (CHARHE == 175 and bctr == 15):
                bctr -= 15
                
        #Bobbing for AI
        if (AIHE <= 200 and bctr2 != 25): 
            AIHE = AIHE + 1
            bctr2 += 1
        if (bctr2 == 25):
            AIHE = AIHE - 1
            if (AIHE == 170 and bctr2 == 25):
                bctr2 -= 25

        #Placed Images
        window.fill(WHITE)
        imageplacer.imgdim("Backdrops/DungeonA.png", x, y)
        imageplacer.imgdim("Characters/doll.png",CHARWI, CHARHE)
        imageplacer.imgdim("Cpu/evileye.png", AIWI, AIHE)
        cardR.cardrandomizer(count1, count2) #Places the random hand of 5 cards
        
            
        #Closes the game if the X is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #Everything that will happen due to a button click will be under here
        #For now it just randomizes your hand
            if event.type == pygame.MOUSEBUTTONDOWN:
                j, count1, count2 = 0, 0, 0
                cardR.cardrandomizer(count1, count2)
                
                

    pygame.quit()

main()