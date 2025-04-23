"""
Simple Canvas Eraser

This program draws a grid of blue rectangles. An eraser box follows the mouse,
and turns any touched rectangles white.
"""

from graphics import Canvas 
import time

# Constants
WIDTH = 400
HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase(canvas, eraser):
    x = canvas.get_mouse_x()
    y = canvas.get_mouse_y()

    x_end = x + ERASER_SIZE
    y_end = y + ERASER_SIZE

    items = canvas.find_overlapping(x, y, x_end, y_end)

    for item in items:
        if item != eraser:
            canvas.set_color(item, 'white')

def draw_grid(canvas):
    rows = HEIGHT // CELL_SIZE
    cols = WIDTH // CELL_SIZE

    for row in range(rows):
        for col in range(cols):
            x1 = col * CELL_SIZE
            y1 = row * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            canvas.create_rectangle(x1, y1, x2, y2, 'blue')

def main():
    canvas = Canvas(WIDTH, HEIGHT)
    draw_grid(canvas)

    canvas.wait_for_click()
    click_x, click_y = canvas.get_last_click()

    eraser = canvas.create_rectangle(
        click_x, click_y,
        click_x + ERASER_SIZE,
        click_y + ERASER_SIZE,
        'pink'
    )

    while True:
        mx = canvas.get_mouse_x()
        my = canvas.get_mouse_y()
        canvas.moveto(eraser, mx, my)
        erase(canvas, eraser)
        time.sleep(0.05)

if __name__ == '__main__':
    main()
