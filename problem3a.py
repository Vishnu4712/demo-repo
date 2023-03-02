import sys
import time

#3a

def BinarySearch (InputFile):
    with open (InputFile) as f:
        lines = f.read()
        values = lines.split()

        for i in range (len(values)):
            values[i] = int(values[i])
        search = values[0]
        array = values[1:]
        
    start = time.time()
    low,high = 0,len(array) - 1
    while (low <= high):
        for i in range (low,high + 1):
            mid = (low + high)//2
            if search == array[mid]:
                print("Found at index", mid)
                end = time.time()
                low = high + 1
            elif search < array[mid]:
                high = mid - 1
                break
            else:
                low = mid + 1
                break

    if search not in array:
        print("Not Found")
        end = time.time()
    
    print(end - start)

BinarySearch(sys.argv[1])

  
