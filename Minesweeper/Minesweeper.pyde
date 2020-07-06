from Blocks import *
import random

scl = 40
noMines = 20
Grid = list();
msg = "Easy"  
default = 0
theoMines = 0
gc=255

def placeIcons():
    global msg,gc
    rect(40,20,scl*3,scl)
    fill(gc)
    rect(360,20,scl*3,scl)
    fill(255)
    textAlign(CENTER)
    textSize(30);
    text(msg,260,50); 
    fill(0)
    textAlign(CENTER)
    textSize(18);
    text("Restart",100,50); 
    fill(0)
    textAlign(CENTER)
    textSize(18);
    text("Show All",420,50); 
    fill(0)
    textAlign(CENTER)
    textSize(14);
    text("Contains "+str(theoMines)+" Mines",260,75); 

def countMines():
    global theoMines 
    theoMines = 0
    for i in range(len(Grid)):
        for j in range(len(Grid[0])):
            if Grid[i][j].isMine:
                theoMines += 1

def openNext(x_,y_):
    if(Grid[x_][y_].Number == 0):
        for a in range(-1,2):
            for b in range(-1,2):
                x,y = x_+a,y_+b
                if (x>-1 and x<width/scl and y<width/scl and y>-1):
                    if(not Grid[x][y].isOpened):
                        Grid[x][y].isOpened = True
                        openNext(x,y)

def gameOver():
    global msg,gc
    msg = "Game Over"
    gc = 180
    for i in range(len(Grid)):
        for j in range(len(Grid[0])):
            Grid[i][j].isOpened = True

def mousePressed():
    global msg,default
    if mouseY < 80:
        x = (mouseX-40)/scl
        y = (mouseY+20)/scl
        if y == 1:
            if (x == 0) or (x == 1) or (x == 2):
                Main(default)
            if ((x == 4) or (x == 5) or (x == 6)):
                default +=1
                if default > 2:
                    default = 0
                gameOver()
                Main(default)
            if (x == 8) or (x == 9) or (x == 10):
                gameOver()
                
    if mouseY > 80:
        x = int((mouseX/scl))
        y = int((mouseY-80)/scl)
        if Grid[x][y].isOpened:
            return
        
        if Grid[x][y].isMine:
            gameOver()
            
        Grid[x][y].isOpened = True
        if (not Grid[x][y].Number) and (not Grid[x][y].isMine):
            openNext(x,y)
        
def setMine():
    global noMines
    temp = [[i,j] for i in range(width/scl) for j in range(floor(width/scl))]
    Mines = []
    for i in range(noMines):
        Mines.append(random.choice(temp))
    for i in Mines:
        Grid[i[0]][i[1]].isMine = True
    countMines()
    
def setValues():
    count = 0
    for i in range(len(Grid)):
        for j in range(len(Grid[0])):
            if (not Grid[i][j].isMine):    
                for a in range(-1,2):
                    for b in range(-1,2):
                        x,y = i+a,j+b
                        if (x>-1 and x<width/scl and y<width/scl and y>-1):
                            try:
                                if Grid[x][y].isMine:
                                    count = count+1 
                            except IndexError:
                                pass
                            
            Grid[i][j].Number = count
            count = 0                

def Main(diff):
    global noMines,msg,Grid,gc
    gc = 255
    if diff == 0:
        noMines = 20
        msg = "Easy"
    if diff == 1:
        noMines = 30
        msg = "Medium"
    if diff == 2:
        noMines = 45
        msg = "Hard"
        
    background(150)
    Grid = [[0 for i in range(floor(width/scl))] for j in range(floor(width/scl))]
    for i in range(len(Grid)):
        for j in range(len(Grid[0])):
            Grid[i][j] = Block((i*scl),(j*scl)+80,scl)
    setMine()
    setValues()
    

def setup():
    global Grid
    size(520,600)
    Main(default)
    
def draw():
    background(150)
    fill(255)
    placeIcons()
    for i in range(len(Grid)):
        for j in range(len(Grid[0])):
            Grid[i][j].update()
