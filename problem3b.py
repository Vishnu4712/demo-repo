import sys
import time

def LinearSearch (InputFile):
    with open (InputFile) as f:
        lines = f.read()
        values = lines.split()

        for i in range (len(values)):
            values[i] = int(values[i])
        search = values[0]
        array = values[1:]

        start = time.time()
        for i in range (len(array)):
            if search == array[i]:
                print("Found at index",i)
                end = time.time()
                break
        else:
            print("Not Found")
            end = time.time()
    
    print(end - start)

LinearSearch(sys.argv[1])
