def swap_halves(array):
    middle = len(array) // 2

    if len(array) % 2 != 0:
        middle += 1


    swapped_array = array[middle:] + array[:middle]

    return swapped_array


print(swap_halves([1, 2, 5, 6, 7, 8]))
print(swap_halves([6, 7, 8, 9, 1, 2]))