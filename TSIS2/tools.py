import pygame

def flood_fill(surface, pos, new_color):
    target_color = surface.get_at(pos)
    if target_color == new_color:
        return

    w, h = surface.get_size()
    stack = [pos]

    while stack:
        x, y = stack.pop()

        if x < 0 or x >= w or y < 0 or y >= h:
            continue

        if surface.get_at((x, y)) != target_color:
            continue

        surface.set_at((x, y), new_color)

        stack.append((x+1, y))
        stack.append((x-1, y))
        stack.append((x, y+1))
        stack.append((x, y-1))