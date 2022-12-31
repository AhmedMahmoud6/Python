def unique(array):
    for num in array:
        if array.count(num) == 1:
            return num
print(unique([2, 5, 7, 8, 2, 5, 7]))