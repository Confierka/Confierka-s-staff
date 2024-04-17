import math

WIDTH, HEIGHT = 500,500




image = [[(255,255,255)]*WIDTH for _ in range(HEIGHT)]

#for x in range(WIDTH):
#    for y in range(HEIGHT):
#        r,g,b=get_pixel_color(x/WIDTH,y/WIDTH)
#        image[y][x]=(b,g,r)
def transform_color(color):
    r,g,b=color
    return(int(b),int(g),int(r))

def draw_line(x0,y0,x1,y1,color):
    x0=int(x0)
    y0=int(y0)
    x1=int(x1)
    y1=int(y1)
    
    if x0==x1 and y0==y1:
        return
    
    
    
    if abs(x0-x1)>abs(y0-y1):
        if x0>x1:
            x0,x1=x1,x0
            y0,y1=y1,y0
        for x in range(x0,x1+1):
            t=(x-x0)/(x1-x0)
            y=y0+(y1-y0)*t
            image[int(y)][int(x)]=color
    else:
        if y0>y1:
            x0,x1=x1,x0
            y0,y1=y1,y0
        for y in range(y0,y1+1):
            t=(y-y0)/(y1-y0)
            x=x0+(x1-x0)*t
            image[int(y)][int(x)]=color

class Turtle:
    def __init__(self,x = WIDTH/2,y=HEIGHT/2,color=(0,0,0),down=True):
        self.x=x
        self.y=y
        self.angle=0.0
        self.color=color
        self.down=down

    def turn(self, angle):
        self.angle+=angle
    
    def move(self,length):
        x1= self.x + length*math.cos(math.radians(self.angle))
        y1= self.y +length*math.sin(math.radians(self.angle))
        if self.down:
            draw_line(self.x,self.y,x1,y1,self.color)
        self.x,self.y=x1,y1
    def set_color(self,color):
        self.color=color
    def pen_up(self):
        self.down=False
    def pen_down(self):
        self.down=True


def tree(t,length,n,a,b):
    t.pen_down()
    color=t.color
    if n < 3:
        t.set_color((10,200,30))
    
    t.move(length)

    if n>0:
        t.turn(a)
        tree(t,length/1.5,n-1,a*0.8,b)
        t.turn(-a -b)
        tree(t,length/1.6,n-1,a*0.5,b*0.7)
        t.turn(b)
    t.pen_up()
    t.move(-length)
    if n<3:
        t.set_color(color)
    
    



t=Turtle(x=WIDTH/2,y=10,color=(156,102,21))
t.turn(90)
tree(t,140,10,30,45)
        

with open ('image.tga','wb') as file:
    file.write(bytearray([0,0,2]))
    file.write(bytearray([0,0,0,0,0]))
    file.write(bytearray([0,0,0,0]))
    file.write(bytearray([WIDTH & 0x00FF,WIDTH >>8,HEIGHT & 0x00FF, HEIGHT>>8]))
    file.write(bytearray([24]))
    file.write(bytearray([0]))
    for y in range(HEIGHT):
        for x in range(WIDTH):
            color=image[y][x]
            file.write(bytearray(transform_color(color)))
    
