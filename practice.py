with open ('C:\\Users\\hp\\Desktop\\b22144_assignment8\\b22144_assignment8\\notepractice.txt') as f:
    lines = f.read()
    values = lines.split()
    for i in range (len(values)):
        values[i] = int(values[i])
        search = values[0]
        array = values[1:]
        