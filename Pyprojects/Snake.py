import math
import random
import pygame

class cube(object):
    rows=20
    w=500
    def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        self.pos = start
        self.dirnx = 0
        self.dirny = 0
        self.color = color

    def move(self,dirnx,dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)  # change our position

    def draw(self, surface, eyes=False):
        dis = self.w // self.rows  # Width/Height of each cube
        i = self.pos[0]  # Current row
        j = self.pos[1]  # Current Column

        pygame.draw.rect(surface, self.color, (i * dis, j * dis, dis, dis))   #pygame.draw.rect(screen,color,(coord x, coord y,widht,height))   # By multiplying the row and column value of our cube by the width and height of each cube we can determine where to draw it

        if eyes: # Draws the eyes
            centre = dis//2
            radius = 3
            circleMiddle = (i*dis+centre-radius,j*dis+8)
            circleMiddle2 = (i*dis + dis -radius*2, j*dis+8)
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)


class snake(object):
    body=[]                         # creates the body from many "cube" objects
    turns={}                        # creates a dictionary to remember where the snake turned as well as its tail
    def __init__(self,color,pos):
        self.color=color
        self.head=cube(pos)                 # The head will be the front of the snake
        self.body.append(self.head)         # We will add head (which is a cube object)
        self.dirnx=0                        # These will represent the direction our snake is moving
        self.dirny=1

    def move(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:           # Check if user hit the red x
                pygame.quit()

            keys=pygame.key.get_pressed()         # It gives us a list with all the keys if a value was pressed or not (1 or 0) in the keyboard. See which keys are being pressed
            for key in keys:                      # Loop through all the keys
                if keys[pygame.K_LEFT]:           # Top right corner is (0,0); thats why dirnx--> -1
                    self.dirnx=-1
                    self.dirny=0                  # dirny=0 because i just want to move one way at a time
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]      # "[:]" is used to create a copy and not change the original

                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i,c in enumerate(self.body):            # Loop through every cube in our body
            p=c.pos[:]                              # This stores the cubes position on the grid
            if p in self.turns:                     # If the cubes current position is one where we turned
                turn = self.turns[p]                # Get the direction we should turn
                c.move(turn[0], turn[1])            # Move our cube in that direction
                if i == len(self.body) - 1:         # If this is the last cube in our body remove the turn from the dict
                    self.turns.pop(p)               # Eliminate the last element
            else:                                           # If we are not turning the cube
                if c.dirnx == -1 and c.pos[0] <= 0:         # If the cube reaches the edge of the screen we will make it appear on the opposite side
                    c.pos = (c.rows - 1, c.pos[1])          # Last position is "the last element - 1" since python starts counting from 0
                elif c.dirnx == 1 and c.pos[0] >= c.rows - 1:
                    c.pos = (0, c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows - 1:
                    c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0:
                    c.pos = (c.pos[0], c.rows - 1)
                else:
                    c.move(c.dirnx, c.dirny)                # If we haven't reached the edge just move in our current direction

    def reset(self,pos):
        pass
    def addCube(self):
        tail=self.body[-1]
        dx,dy=tail.dirnx,tail.dirny
        # We need to know which side of the snake to add the cube to.
        # So we check what direction we are currently moving in to determine if we need to add the cube to the left, right, above or below.
        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0]-1,tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0]+1,tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0],tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0],tail.pos[1]+1)))
        self.body[-1].dirnx = dx                # We then set the cubes direction to the direction of the snake.
        self.body[-1].dirny = dy

    def draw(self,surface):
        for i, c in enumerate(self.body):
            if i == 0:                          # for the first cube in the list we want to draw eyes
                c.draw(surface, True)           # adding the true as an argument will tell us to draw eyes
            else:
                c.draw(surface)                 # otherwise we will just draw a cube

def drawGrid(w,rows,surface):       # We will draw one vertical and one horizontal line each loop
    sizebtw=w//rows                 # Gives us the distance between the lines
    x=0
    y=0
    for line in range(rows):
        x=x+sizebtw
        y=y+sizebtw
        pygame.draw.line(surface,(255,255,255),(x,0),(x,w))   # Draws a line in each loop;(255,255,255)=white color; (x,0)start position of the line;(x,w) end position
        pygame.draw.line(surface,(255,255,255),(0,y),(w,y))   # Horizontal lines

def redrawWindow(surface):
    #global rows,width,s
    surface.fill((0,0,0))               # (0,0,0)=black color; Fills the screen with black
    s.draw(surface)                     # Draw our snake
    #drawGrid(width,rows,surface)        # Will draw our grid lines
    snack.draw(surface)
    pygame.display.update()             # Updates the screen

def randomSnack(rows,snake):
    positions = snake.body  # Get all the positions of cubes in our snake
    while True:  # Keep generating random positions until we get a valid one
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue        # This wll check if the position we generated is occupied by the snake
        else:
            break
    return (x, y)

def main():
    global rows,width,s,snack
    width=500
    height=500
    rows=20
    win=pygame.display.set_mode((width,height))     # Creates our screen object
    s=snake((255,0,0),(6,6))                        # Creates a snake object; with color and start position
    snack=cube(randomSnack(rows, s),color=(0, 255, 0))
    clock=pygame.time.Clock()                       # Creating a clock object

    flag=True
    while flag:                 # STARTING MAIN LOOP
        pygame.time.delay(50)   # Delay the speed so the game wont be extremely fast. the lower --> the faster the game
        clock.tick(10)          # This will ensure the game runs at run 10 frames per sec. Speed is also related to clock: the lower --> the slower the game
        s.move()
        if s.body[0].pos==snack.pos:
            s.addCube()
            snack=cube(randomSnack(rows, s),color=(0, 255, 0))
        redrawWindow(win)       # This will refresh our screen

        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z:z.pos,s.body[x+1:])):
                print('Score: ', len(s.body))
                message_box('You Lost!', 'Play again...')
                s.reset((10,10))
                break

main()

