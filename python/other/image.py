from PIL import Image
import numpy as np



Resolution = np.array([200,200])


def mainImage(fragCoord: np.array):
    uv = fragCoord / Resolution

    color1=np.array([1,0,0])
    color2=np.array([0,1,0])
    
    

    return color1+(color2-color1)*uv[0]

def fixColor(color: np.array):
    return tuple(int(x) for x in tuple(color*255))

#img = Image.new('HSV', tuple(Resolution), (0,255,128))

#for x in range(img.size[0]):
#    for y in range(img.size[1]):
#        coords = np.array([x, y])
#        #img.putpixel((x, y), fixColor(mainImage((coords))))

def lerp(a,b,t):
    return a+(b-a)*t


img_rgb = Image.open('forest.jpg').convert('RGB')
#img_rgb.save('cat.jpeg')
img_lab=img_rgb.convert("LAB")

for x in range(img_lab.size[0]):
    for y in range(img_lab.size[1]):
        l,a,b = img_lab.getpixel((x,y))
        
        #a=a>>3<<3
        #b=b>>3<<3
        t=0.2
        p=int(lerp(a,b,t))
        q=int(lerp(b,a,t))
        img_lab.putpixel((x,y),(l,p,q))

img_lab.convert('RGB').save('lab.png')


#for x in range(img_rgb.size[0]):
#    for y in range(img_rgb.size[1]):
#        r,g,b = img_rgb.getpixel((x,y))
#        r=r>> 2 << 2
#        g=g>>2<<2
#        b=b>>2<<2
        
        
        
#        img_rgb.putpixel((x,y),(r,g,b))

#img_rgb.convert("RGB").save('rgb.png')







