#73. Implement selection sort.
def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        mini_index=i
        for j in range(i+1,n):
            if arr[mini_index] > arr[j]:
                mini_index=j
        arr[i],arr[mini_index]=arr[mini_index],arr[i]

    return arr

arr=list(map(int,input("enter a list of no. : ").split(",")))
print(f"the list of sorted arr are: {selection_sort(arr)}")

