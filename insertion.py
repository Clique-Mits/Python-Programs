# Python program for implementation of Insertion Sort

# Function to do insertion sort
def insertionSort(arr):
    for i in range(1, len(arr)):

        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


arr = list(map(int, list(input().split())))
insertionSort(arr)
print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i])
