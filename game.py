WIDTH = 800
HEIGHT = 600
TITLE = "Mi primer juego"
FPS = 60

listaColores = ["red", "green", "blue", "yellow", "purple", "orange"]

player = Rect(50, 50, 50, 50)
balon = Circle(100, 100, 20)

def draw():
    screen.clear()
    screen.fill(listaColores[0]) 
    
    screen.draw.filled_rect(player, "white")
    screen.draw.filled_circle(balon, "white")


def update():
    pass

def on_key_down(key):
    pass
