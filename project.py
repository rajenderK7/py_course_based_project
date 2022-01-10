from pickle import TRUE
import pygame
import math as mt
import random as rd

pygame.init()


class SortingVisualizer:
    BG_COLOR = 0, 0, 0
    # BG_COLOR = 247, 147, 30  # GOLD
    # BG_COLOR = 128, 128, 128  # GREY
    WHITE = 255, 255, 255
    BLACK = 0, 0, 0
    SIDE_MARGIN = 100
    TOP_MARGIN = 100
    RED = 255, 0, 0
    BLUE = 0, 0, 255
    YELLOW = 255, 255, 0
    BAR_COLORS = [
        (0, 255, 239),
        (77, 226, 235),
        (58, 190, 255),
    ]
    FONT = pygame.font.SysFont("verdana", 30)
    MENU_FONT = pygame.font.SysFont("verdana", 20)

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Visualizer")
        self.starting_x_cordinate = self.SIDE_MARGIN // 2
        self.update_array(lst)

    def update_array(self, lst):
        self.lst = lst
        self.max_val = max(lst)
        self.min_val = min(lst)
        self.bar_width = round((self.width - self.SIDE_MARGIN) / len(lst))
        self.bar_height = mt.floor((
            self.height - self.TOP_MARGIN) / (self.max_val - self.min_val))


def display_handler(visualizer, sort_name, ascending):
    visualizer.window.fill(visualizer.BG_COLOR)
    current_sort = visualizer.FONT.render(
        f"{sort_name} - {'Ascending' if ascending else 'Descending'}", 1, visualizer.YELLOW)
    visualizer.window.blit(
        current_sort, (visualizer.width // 2 - current_sort.get_width() // 2, 5))
    menu = visualizer.MENU_FONT.render(
        "X - Reset | Enter - Start | A - Ascending | D - Descending | B - Bubble Sort | I - Insertion Sort", 1, visualizer.WHITE)
    visualizer.window.blit(
        menu, (visualizer.width // 2 - menu.get_width() // 2, 45))
    display_array_handler(visualizer)
    pygame.display.update()


def create_array(min_val, max_val, n):
    lst = [rd.randint(min_val, max_val) for _ in range(n)]
    rd.shuffle(lst)
    return lst


def display_array_handler(visualizer, swappers={}, refresh=False):
    if refresh:
        current_area = (visualizer.SIDE_MARGIN // 2, visualizer.TOP_MARGIN, visualizer.width -
                        visualizer.SIDE_MARGIN, visualizer.height - visualizer.TOP_MARGIN)
        pygame.draw.rect(visualizer.window, visualizer.BG_COLOR, current_area)

    for i, item in enumerate(visualizer.lst):
        color = visualizer.BAR_COLORS[i % 3]
        x_coordinate = visualizer.starting_x_cordinate + i * visualizer.bar_width
        y_coordinate = visualizer.height - \
            ((item - visualizer.min_val) * visualizer.bar_height)

        # color ovveride if it is present in the dictionary
        if i in swappers.keys():
            color = swappers[i]

        pygame.draw.rect(visualizer.window, color, (x_coordinate,
                         y_coordinate, visualizer.bar_width, visualizer.height))

    if refresh:
        pygame.display.update()


def bubbleSort(visualizer, ascending=True):
    lst = visualizer.lst
    for i in range(len(lst) - 1):
        for j in range(len(lst) - i - 1):
            n1 = lst[j]
            n2 = lst[j+1]
            if (n1 > n2 and ascending) or (n1 < n2 and not ascending):
                lst[j], lst[j+1] = lst[j+1], lst[j]
                display_array_handler(visualizer, swappers={
                                      j: visualizer.RED, j+1: visualizer.YELLOW}, refresh=True)
                yield True
    return lst


def insertionSort(visualizer, ascending=True):
    lst = visualizer.lst
    for i in range(1, len(lst)):
        temp = lst[i]
        j = i - 1
        while True:
            ascending_sort = i > 0 and lst[i-1] > temp and ascending
            descending_sort = i > 0 and lst[i-1] < temp and not ascending
            if not ascending_sort and not descending_sort:
                break

            lst[i] = lst[i-1]
            i -= 1
            lst[i] = temp
            display_array_handler(visualizer, swappers={
                j: visualizer.RED, j+1: visualizer.YELLOW}, refresh=True)
            yield True

    return lst


def main_loop():
    isRunning = True
    clock = pygame.time.Clock()

    curr_min = 0
    curr_max = 500
    curr_range = 100

    # For Sorting process
    isSorting = False
    ascending = True
    # current_sort = insertionSort
    current_sort = bubbleSort
    current_sort_name = "Bubble Sort"
    current_sort_func = None
    lst = create_array(curr_min, curr_max, curr_range)
    visualizer = SortingVisualizer(1000, 600, lst)

    while isRunning:
        clock.tick(60)
        display_handler(visualizer, current_sort_name, ascending)

        if isSorting:
            try:
                next(current_sort_func)
            except StopIteration:
                isSorting = False

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                isRunning = False

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_x and not isSorting:
                lst = create_array(curr_min, curr_max, curr_range)
                visualizer.update_array(lst)
                isSorting = False
            elif event.key == pygame.K_a and not isSorting:
                ascending = True
            elif event.key == pygame.K_d and not isSorting:
                ascending = False
            elif event.key == pygame.K_RETURN:
                isSorting = True
                current_sort_func = current_sort(visualizer, ascending)
                # current_sort_func = current_sort(visualizer, 0, curr_range - 1)
            elif event.key == pygame.K_i and not isSorting:
                current_sort = insertionSort
                current_sort_name = "Insertion Sort"
            elif event.key == pygame.K_b and not isSorting:
                current_sort = bubbleSort
                current_sort_name = "Bubble Sort"

    pygame.quit()


if __name__ == "__main__":
    main_loop()
