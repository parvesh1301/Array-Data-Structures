def LargestNumber(arr):
    if not arr:
        return None
    
    largest = arr[0]
    for num in arr :
        if num > largest:
            largest = num
    return largest

array = list(map(int,input("Enter the elements to list inside the array :").split()))
Largest_num = LargestNumber(array)
print (f"The largest element from the array {array} is: {Largest_num} ")
    
