#Functional Prompt
#Implement a function that will flatten and sort an array of integers in ascending order, 
# and which adheres to a functional programming paradigm.

def flatten_and_sort(array):
    arr = []
    for i in array:
        for j in i:
            arr.append(j)
    return sorted(arr)

    
print(flatten_and_sort([[3, 2, 1], [7, 9, 8], [6, 4, 5]])) # [1, 2, 3, 4, 5, 6, 7, 8, 9]