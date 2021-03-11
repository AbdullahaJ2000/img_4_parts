from PIL import Image 

def gray_cyan():
    red = 0
    green = 0
    blue = 0
    
    img=Image.open('sor.png','r')
    pixels = img.load()
    w,h = img.size
    
    for i in range(w//2):
        for j in range(h//2):
            rgb = pixels[i,j]
            red = rgb[0]
            green = rgb[1]
            blue = rgb[2]
            gray = (red+green+blue)//3
            pixels[i,j] = (gray,gray,gray)
            
        for a in range(h//2,h):
            rgb = pixels[i,a]
            red = rgb[0]
            green = rgb[1]
            blue = rgb[2]
            new = (red+blue)//3
            pixels[i,a] = (new,0,new)
      
    for x in range(w//2,w):
        for y in range(h//2):
            rgb = pixels[x,y]
            red = rgb[0]
            green = rgb[1]
            blue = rgb[2]
            cyan = (green+blue)
            pixels[x,y] = (0,cyan,cyan)
            
        for b in range(h//2,h):
            rgb = pixels[x,b]
            red = rgb[0]
            green = rgb[1]
            blue = rgb[2]
            new2 = (green+red)
            pixels[x,b] = (new2,new2,0)
    img.save('res.png')
    img.show()
    
gray_cyan()

            
    






