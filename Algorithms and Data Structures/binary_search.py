def binary_search(lst, target):
    first = 0
    last = len(lst) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if lst[midpoint] == target:
            return midpoint
        elif lst[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None


def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target was not found in list")


print(binary_search([1, 2, 3, 4], 3))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# result = binary_search(numbers, 16)
# verify(result)
lst = [1, 2, 3, 4, 10]
print(sum(1 for x in lst))
