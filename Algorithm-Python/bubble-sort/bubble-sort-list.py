# it's taking the big number to the end of the list and so and forth 

def bubble_sort(element):
	tryed=0
	size = len(element)
	swapped = False
	for j in range(size-1):
	
		for i in range(size-1-j): 
		
			if element[i] > element[i+1]:
				
				element[i],element[i+1] = element[i+1],element[i]
				swapped = True
				tryed+=1
		
		if not swapped:
			break
	print (f"{tryed} operation to complete")
			
		
	
if __name__ == '__main__':

	element = [6,3,8,1,3,56,98,23,45,46,234,875,80]
	bubble_sort(element)
	print(element)
	