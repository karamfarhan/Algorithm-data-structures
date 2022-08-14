# merge sort with list of dict(objects) based on one of the values


def merge_2sorted_list(arr, a, b, key, descending):
    # sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0
    if descending:

        while i < len_a and j < len_b:
            if a[i][key] > b[j][key]:
                arr[k] = a[i]
                i += 1
            else:
                arr[k] = b[j]
                j += 1
            k += 1
    else:
        while i < len_a and j < len_b:
            if a[i][key] < b[j][key]:
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
    return arr


def merge_sort(arr, sorted_by=None, descending=False):

    size = len(arr)

    if len(arr) <= 1:
        return arr

    left = merge_sort(arr[0 : size // 2], sorted_by, descending)
    right = merge_sort(arr[size // 2 :], sorted_by, descending)

    return merge_2sorted_list(arr, left, right, sorted_by, descending)


elements = [
    {"name": "vedanth", "age": 17, "time_hours": 1},
    {"name": "rajab", "age": 12, "time_hours": 3},
    {"name": "vignesh", "age": 21, "time_hours": 2.5},
    {"name": "chinmay", "age": 24, "time_hours": 1.5},
]

sorted_elements = merge_sort(elements, "time_hours", descending=True)
for i in sorted_elements:
    print(i)
