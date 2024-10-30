import py5

logo = None
x, y  = 0, 0 
X_speed, y_speed = 0, 0
x = py5.width / 2
y = py5.height / 2

def setup():
    
 py5.size(1000, 650)
    
 global logo, x, y, x_speed, y_speed
    
 logo = py5.load_image("asd.png")
    
 x_speed= 2
 y_speed= 2
    
def draw():
 global logo, x, y, x_speed, y_speed
 py5.background(0)

 py5.image(logo,x, y)
        
 x += x_speed
 y += y_speed
        
 if x <= 0 or x + logo.width >= py5.width:
    x_speed *= -1
 if y <= 0 or y + logo.height >= py5.height:
    y_speed *= -1
            
py5.run_sketch()
