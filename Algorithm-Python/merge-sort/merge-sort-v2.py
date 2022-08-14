#  This version of merege sort use less space because it will sort numbers in the same list


def merge_sort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_2sorted(left, right, arr)


def merge_2sorted(a, b, arr):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1

    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1


####################
arr = [6, 3, 9, 6, 2, 80, 65, 3, 4, 9, 7, 5, 443, 5]
merge_sort(arr)
print(arr)
