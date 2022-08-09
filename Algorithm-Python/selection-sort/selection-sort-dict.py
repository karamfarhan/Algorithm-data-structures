# selection sort with a list of dictionaries
# sort the dict based on a value in it


def selection_sort_dict(my_list, key):
    size = len(my_list)
    for i in range(size - 1):
        min = i
        for j in range(min + 1, size):
            if my_list[j][key] < my_list[min][key]:
                min = j
        if i != min:
            my_list[i], my_list[min] = my_list[min], my_list[i]
    return my_list


students = [
    {"First Name": "Raj", "Last Name": "Nayyar", "Age": 44},
    {"First Name": "Suraj", "Last Name": "Sharma", "Age": 21},
    {"First Name": "Karan", "Last Name": "Kumar", "Age": 33},
    {"First Name": "Jade", "Last Name": "Canary", "Age": 12},
    {"First Name": "Raj", "Last Name": "Thakur", "Age": 65},
    {"First Name": "Raj", "Last Name": "Sharma", "Age": 4},
    {"First Name": "Kiran", "Last Name": "Kamla", "Age": 2},
    {"First Name": "Armaan", "Last Name": "Kumar", "Age": 13},
    {"First Name": "Jaya", "Last Name": "Sharma", "Age": 76},
    {"First Name": "Ingrid", "Last Name": "Galore", "Age": 24},
    {"First Name": "Jaya", "Last Name": "Seth", "Age": 42},
    {"First Name": "Armaan", "Last Name": "Dadra", "Age": 32},
    {"First Name": "Ingrid", "Last Name": "Maverick", "Age": 57},
    {"First Name": "Aahana", "Last Name": "Arora", "Age": 2},
]


selection_sort_dict(students, "Age")
for student in students:
    print(student)
