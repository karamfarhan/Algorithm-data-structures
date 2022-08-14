# This version of merege sort use more space because it will define sorted_list


# first we make the method how will merge 2 sorted list


def merge_2sorted_list(a, b):
    sorted_list = []  # empty list to append the items
    len_a = len(a)  # we import len of a list to make code rebet hemsself = item
    len_b = len(b)
    i = j = 0
    while i < len_a and j < len_b:  #
        if a[i] <= b[j]:  # if  first item in a list is less first item in b  list
            sorted_list.append(a[i])  # append thid item (a item ) in sorted list
            i += 1  # and go to next item from a list
        else:  #
            sorted_list.append(b[j])
            j += 1
    while i < len_a:  # if that some list have items more than the else list
        sorted_list.append(a[i])  # just append thid items in the end of my sorted l
        i += 1
    while j < len_b:
        sorted_list.append(b[j])
        j += 1
    return sorted_list  # then return the sorted list


# now her we have to make method that make my big arry to apart of arry have 1 item
def merge_sort(arr):
    if len(arr) <= 1:  # if len for arry = 1 stoop
        return arr
    mid = len(arr) // 2  # if it not = 1 import th mid
    left = arr[:mid]  # then make 2 arrys first (left) from start to mid
    right = arr[mid:]  # and the second one from mid to end

    left = merge_sort(left)  # now do same method for left and right part
    right = merge_sort(right)  #
    # then at this point we have arrys one of them have 1 item ..
    # do my method to make it agin in one arry by my method (merge_2sorted_list)
    return merge_2sorted_list(left, right)


#####################################
my_l = [8, 3, 87, 5, 90, 2, 343, 56]
print(merge_sort(my_l))
