def binary(to_found, my_list):
    low_left = 0
    high_right = len(my_list) - 1
    mid_item = 0
    nub_try = 0
    found_if = False
    while not found_if:  # we can use this code  if mid_item > len(l):
        if low_left > high_right:  # and put it after define mid_item(K)
            print("Not Found")
            break

        mid_item = low_left + ((high_right - low_left) // 2)
        # (K) here
        nub_try += 1
        if my_list[mid_item] == to_found:
            print("Number Is Found")
            print(f"{nub_try} Try To Find {my_list[mid_item]}")
            found_if = True
        if my_list[mid_item] < to_found:
            low_left = mid_item + 1
        if my_list[mid_item] > to_found:
            high_right = mid_item - 1


my_list = [i for i in range(25000000)]
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
binary(20000000, my_list)
