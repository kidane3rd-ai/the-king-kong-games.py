import pygame
pygame.init()
screen=pygame.display.set_mode((600,600))
screen.fill((255,0,0))
subay=pygame.image.load("images/subay.png")
block_blast=pygame.image.load("images/block blast.jpg")
sudoku=pygame.image.load("images/sudoku.jpg")
toca_boca=pygame.image.load("images/toca boca.jpg")
screen.blit(subay,(150,100))
screen.blit(toca_boca,(150,210))
screen.blit(sudoku,(150,310))
screen.blit(block_blast,(150,410))
font=pygame.font.SysFont("Times New Roman",36)
text=font.render("sudoku",True,(0,0,0))
screen.blit(text,(350,100))
font=pygame.font.SysFont("Time New Roman",36)
text2=font.render("block_blast",True,(0,0,0))
screen.blit(text2,(350,210))

while 1:
    for event in pygame.event.get():
           if event.type == pygame.QUIT:
                pygame.quit()



    pygame.display.update ()