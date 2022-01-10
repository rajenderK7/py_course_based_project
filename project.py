import pygame
import math as mt
import random as rd

pygame.init()


class SortingVisualizer:
    BG_COLOR = 255, 255, 255
    SIDE_MARGIN = 100
    TOP_MARGIN = 100
    BAR_COLORS = [
        (0, 255, 239),
        (77, 226, 235),
        (58, 190, 255),
        # (0, 0, 0),
        # (0, 0, 0),
        # (0, 0, 0),
    ]

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height
        self.lst = lst
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Visualizer")

        self.starting_x_cordinate = self.SIDE_MARGIN // 2
        # self.starting_y_cordinate = 150
        self.max_val = max(self.lst)
        self.min_val = min(self.lst)
        self.bar_width = round((self.width - self.SIDE_MARGIN) / len(lst))
        self.bar_height = mt.floor((
            self.height - self.TOP_MARGIN) / (self.max_val - self.min_val))


def display_handler(visualizer):
    visualizer.window.fill(visualizer.BG_COLOR)
    display_array_handler(visualizer)
    pygame.display.update()


def create_array(min_val, max_val, n):
    lst = [rd.randint(min_val, max_val) for _ in range(n)]
    return lst


def display_array_handler(visualizer):
    # for i, item in range(len(visualizer.lst)):
    for i, item in enumerate(visualizer.lst):
        color = visualizer.BAR_COLORS[i % 3]
        x_coordinate = visualizer.starting_x_cordinate + i * visualizer.bar_width
        y_coordinate = visualizer.height - \
            ((item - visualizer.min_val) * visualizer.bar_height)

        pygame.draw.rect(visualizer.window, color, (x_coordinate,
                         y_coordinate, visualizer.bar_width, visualizer.height))


def main_loop():
    lst = create_array(50, 500, 100)
    isRunning = True
    visualizer = SortingVisualizer(1000, 600, lst)
    clock = pygame.time.Clock()

    while isRunning:
        clock.tick(60)
        display_handler(visualizer)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                isRunning = False

    pygame.quit()


if __name__ == "__main__":
    main_loop()
