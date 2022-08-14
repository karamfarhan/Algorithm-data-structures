# it like binary search but in this we use it for dict and book index and phone number


def interpoliation(my_list, num_found):
    low = 0
    hig = len(my_list) - 1
    mid = 0
    try_to = 0
    if_found = False
    while not if_found:
        # if low > hig:   # FROM YOUTUEB CODE
        # print ("not found")
        # break
        mid = ((hig - low) // (my_list[hig] - my_list[low])) * (num_found - my_list[low])  # interpoliation code
        if mid > len(my_list):  # İ MAKE İT
            print("not found")
            break
        try_to += 1
        if my_list[mid] == num_found:
            print("number is found")
            print(try_to, "tried")
            if_found = True
        if my_list[mid] < num_found:
            low = mid + 1
        if my_list[mid] > num_found:
            hig = mid - 1


# Test
my_list = [i for i in range(10_000_000 + 1)]
interpoliation(my_list, 4_792_375)
