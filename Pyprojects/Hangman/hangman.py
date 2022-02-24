import pygame
import string
pygame.init()

screen_width = 800
screen_heigth = 600
screen = pygame.display.set_mode((screen_width,screen_heigth))
pygame.display.set_caption('Hangman')
clock = pygame.time.Clock()
# images = [pygame.image.load('hangman0.png'),pygame.image.load('hangman1.png'),pygame.image.load('hangman2.png'),pygame.image.load('hangman3.png'),pygame.image.load('hangman4.png'),pygame.image.load('hangman5.png'),pygame.image.load('hangman6.png')]

images = []
for i in range(7):
    images.append(pygame.image.load("hangman" + str(i) + ".png"))

class Letter:
    def __init__(self, letter2,x,y):
        self.letter2 = letter2
        self.x = x
        self.y = y
        self.length = 15    # line length
        self.width = 5    # line width
        self.visible = False

    def drawletter(self):
        if self.letter2 != ' ':
            pygame.draw.line(screen,(255,0,0),(self.x,self.y),(self.x + self.length,self.y),self.width)
        if self.visible:
            letter = font.render(self.letter2,True,(0,0,0))
            screen.blit(letter, (self.x , self.y - 20))

class Button:
    def __init__(self,x,y,text,radius):
        self.x = x
        self.y = y
        self.text = text
        self.radius = radius
        self.visible = True

    def drawbutton(self):
        if self.visible:
            self.b = pygame.draw.circle(screen,(0,255,0),(self.x,self.y),self.radius)
            letter = font.render(self.text,False,(0,0,0))
            screen.blit(letter, (self.x-7,self.y-7))


def redraw():
    pygame.display.update()
    screen.fill((190,190,190))
    font2 = pygame.font.SysFont(None, 80, False, True)
    msg = font2.render('PERDISTE MONO QLO!!', False, (255, 0, 0))
    msg2 = font2.render('GANASTE SAPO CTM!!', False, (0, 255, 0))

    screen.blit(images[6-lives], (300, 150))

    if win == True:
        screen.blit(msg2, (20, screen_heigth // 2))
    if lose == True:
        screen.blit(msg, (20, screen_heigth // 2))

# Variables/Classes
font = pygame.font.SysFont(None, 24, False, True)

# Word
Palabra = 'PERRO VERDE'   # <----------------------------------------------INPUT HERE TO PLAY (MAYUS NEEDED)
word = []
x_w = 40
y_w = 500

for i in Palabra:
    word.append(Letter(i,x_w,y_w))
    x_w += 20

# Buttons
alphabet = []
x_b = 30
y_b = 30
counter_b = 0
for i in string.ascii_uppercase:
    if counter_b == 13:
        y_b = 80
        x_b = 30
    alphabet.append(Button(x_b,y_b,i,20))
    x_b += 50
    counter_b += 1

# LIFE
lives = 6
win = False
lose = False

# WIN CONDITION
word_counter = 0
word_length = len(Palabra) - Palabra.count(' ')

# MAIN LOOP
run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if win == False and lose == False:

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                for i in alphabet:
                    # if i.x - i.radius < pos[0] < (i.x + i.radius) and i.y - i.radius < pos[1] < (i.y + i.radius):
                    if i.b.collidepoint(pos) and i.visible:
                        i.visible = False
                        if i.text in Palabra:
                            for a in word:
                                if i.text == a.letter2:
                                    a.visible = True
                                    word_counter += 1
                                if word_counter == word_length:
                                    win = True
                        else:
                            lives -= 1
                            if lives == 0:
                                lose = True

    for i in alphabet:
        i.drawbutton()

    for i in word:
        i.drawletter()

    redraw()

pygame.quit()
