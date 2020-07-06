class Block():
    def __init__(self,x_,y_,w_):
        self.isMine = False;
        self.isOpened = False;
        self.x = x_
        self.y = y_
        self.w = w_
        self.c = 255
        self.Number = 0
        
    def update(self):
        if(self.isOpened):
            self.c = 100
        fill(self.c)
        rect(self.x,self.y,self.w,self.w)
        fill(0)
        if self.isOpened:
            if (not self.isMine) and self.Number:
                textAlign(CENTER)
                textSize(17);
                text(self.Number,self.x+self.w/2,self.y+self.w/2+5); 
            if(self.isMine):
                fill(255,0,0)
                ellipse(self.x+self.w/2,self.y+self.w/2,self.w/2,self.w/2)
        

    #not Used Since Mouse presed is divived by scl and return the relative positon in the grid
    def isClicked(self,mx_,my_):
        if ((self.x < mx_) and ((self.x+self.w) > mx_) and (self.y < my_) and ((self.y+self.w) > my_)):
            self.isOpened = True
        else:
            pass
