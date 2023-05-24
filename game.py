import pygame

pygame.init() # load all the pygame packages
# create a window
window = pygame.display.set_mode((500,500))
# adding image 
image = pygame.image.load('mario.jpg')
window.blit(image, (90, 90))

#add some music
pygame.mixer.music.load('superm.mp3')
pygame.mixer.music.play(-1)
done = False
x=60
y= 60

while not done: 
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.quit:
            done= True

    pygame.display.set_caption("Yosh Game") 

    #code goes here
    # code to draw a rectangle
    pygame.draw.rect(window, (0,128,255), pygame.Rect(160, 160, 90, 90))        

    
    
    pygame.display.flip()
