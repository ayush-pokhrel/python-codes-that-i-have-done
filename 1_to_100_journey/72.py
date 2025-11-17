#72. Implement linear search.

def linear_search(arr,target):
    
    for index,value in enumerate(arr):
        if value == target:
            return index
    return -1

arr=[23,234,64,67,24,678,27,68]
target=int(input("enter an integet: "))
result=linear_search(arr,target)
if result != -1:
    print(f"the index value is: {result}")
else:
    print("the value was not found: ")



