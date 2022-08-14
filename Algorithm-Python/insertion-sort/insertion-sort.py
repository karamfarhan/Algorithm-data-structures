def insertion_2(lis):
    for i in range(1, len(lis)):
        rep = lis[i]
        j = i - 1
        while lis[j] > 0 and rep < lis[j]:
            lis[j + 1] = lis[j]
            j = j - 1
        lis[j + 1] = rep
    return lis


my_l2 = [87, 3, 5, 12, 89, 6, 3, 89]
print(insertion_2(my_l2))
