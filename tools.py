def BSort(lst):
    # lst = visualizer.lst
    for i in range(len(lst) - 1):
        for j in range(i, len(lst) - 1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    print(lst)


BSort([1, 4, 64, 67, 787, 8])


def partition(visualizer, arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:

            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
            yield True

    arr[i+1], arr[high] = arr[high], arr[i+1]
    display_array_handler(visualizer, swappers={
        i+1: visualizer.RED, high: visualizer.YELLOW}, refresh=True)

    return (i+1)


def quickSort(visualizer, low, high):
    arr = visualizer.lst
    if len(arr) == 1:
        return arr
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(visualizer, arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(visualizer, arr, low, pi-1)
        quickSort(visualizer, arr, pi+1, high)
    return arr
