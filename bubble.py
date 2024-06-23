def sort(l: list[int]):
    n = len(l)
    for i in range(n):
        for j in range(0, n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sort(arr)
print(arr)