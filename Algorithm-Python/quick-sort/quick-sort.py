def quicksort(my_list, start, end):
    if start >= end:  # to make this code stoped at len of list
        return
    mid = start + ((end - start) // 2)  # import the mid
    povit = my_list[mid]  # make povit is mid
    s = start  # put start in verable
    e = end  # same
    while s <= e:  # to make this code stop when it be like len of list
        while my_list[s] < povit:  # to find in left of povit for items lees than povit
            s += 1  # continue
        while my_list[e] > povit:  # right of povit for item biger than povit
            e -= 1
        if s <= e:  # if index for s less than index for e make this
            tmp = my_list[s]
            my_list[s] = my_list[e]  # chinge the items and replace it
            my_list[e] = tmp
            s += 1  # the continue to find another items to replact it from left
            e -= 1  # right

    # att this point we have now all the items in left of povit
    # is smaler than povit and all items in right is biger than povit

    if start < e:
        # do the sort agin in left of povit (make new povit)
        quicksort(my_list, start, e)
    if end > s:
        quicksort(my_list, s, end)  # do the sort in right of povit (mak anew povit)


my_list = [11, 9, 29, 7, 2, 15, 28]
quicksort(my_list, 0, len(my_list) - 1)
print(my_list)
