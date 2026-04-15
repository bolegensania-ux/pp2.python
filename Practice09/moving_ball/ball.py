WIDTH = 600
HEIGHT = 400

RADIUS = 25
STEP = 20

x = WIDTH // 2
y = HEIGHT // 2

def move(dx, dy):
    global x, y

    new_x = x + dx
    new_y = y + dy


    if new_x - RADIUS >= 0 and new_x + RADIUS <= WIDTH:
        x = new_x

    if new_y - RADIUS >= 0 and new_y + RADIUS <= HEIGHT:
        y = new_y