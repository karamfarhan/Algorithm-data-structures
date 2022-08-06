def binary_search(number_list, number_to_found, left_indx, right_indx):
    if right_indx < left_indx:
        return -1  # means not found

    mind_indx = left_indx + ((right_indx - left_indx) // 2)
    mind_num = number_list[mind_indx]

    if mind_num == number_to_found:
        return f"found in index {mind_indx}"
    if mind_num < number_to_found:
        left_indx = mind_indx + 1
    else:
        right_indx = mind_indx - 1
    return binary_search(number_list, number_to_found, left_indx, right_indx)


# l = [2, 44, 88, 9, 546, 35, 7, 10]
my_list = [i for i in range(25000000)]

print(binary_search(my_list, 20000000, 0, len(my_list)))
