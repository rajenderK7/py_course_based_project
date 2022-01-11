from project import display_array_handler


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


def selectionSort(visualizer, ascending=True):
    lst = visualizer.lst
    for i in range(len(lst) - 1):
        for i in range(len(lst) - 1):
            if (lst[i] > lst[i + 1] and ascending) or (lst[i] < lst[i + 1] and not ascending):
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                display_array_handler(visualizer, swappers={
                    i: visualizer.RED, i+1: visualizer.YELLOW}, refresh=True)
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
