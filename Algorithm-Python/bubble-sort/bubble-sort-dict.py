# how to sort a list of dictionaries with bubble sort?

def bubble_sort(elements,sort_by): # sort_by = the key of the vlaue you want to sort by
    size = len(elements)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j][sort_by] > elements[j+1][sort_by]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True

        if not swapped:
            break


if __name__ == '__main__':
    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]


    bubble_sort(elements,'transaction_amount') 
    for i in elements:
    	print(i)
