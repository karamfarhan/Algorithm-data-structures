# first of all, how to find the less item in a list
def less_item(my_list):
    smalest_item = my_list[0]
    for i in my_list:
        if i < smalest_item:
            smalest_item = i
    return smalest_item


# selectin sort is the repeat of less_item function many times to sort the list
def selection(my_list):
    size = len(my_list)
    for i in range(size - 1):
        min = i
        for j in range(min + 1, size):
            if my_list[j] < my_list[min]:
                min = j
        if i != min:
            my_list[i], my_list[min] = my_list[min], my_list[i]
    return my_list


my_list = [[5, 9, 2, 4, 5], [], [12, 10, 7, 6, 4, 2, 1], [5], [646, 567, 23, 989, 24, 477, 3454]]
for i in my_list:
    print(selection(i))
