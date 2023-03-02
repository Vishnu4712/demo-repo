import pandas as pd
import sys
#1a
df = pd.read_csv("C:\\Users\\hp\\Desktop\\b22144_assignment8\\b22144_assignment8\data\Cars93.csv")
df1 = df.sort_values(['Manufacturer'])
df1 = df['Manufacturer'].unique()
index1 = [i + 1 for i in range (len(df1))]
dict1 = {"Sorted Model":df1}
df1=pd.DataFrame(dict1,index1)

df1.to_csv("C:\\Users\\hp\\Desktop\\b22144_assignment8\\b22144_assignment8\problem1a.csv")

#1b
df1 = df.groupby('Type').get_group('Small')
df2 = df1[df1['Price'] == df1['Price'].max()]
print(df2)

df1 = df.groupby('Type').get_group('Midsize')
df2 = df1[df1['Price'] == df1['Price'].max()]
print(df2)

df1 = df.groupby('Type').get_group('Compact')
df2 = df1[df1['Price'] == df1['Price'].max()]
print(df2)

df1 = df.groupby('Type').get_group('Large')
df2 = df1[df1['Price'] == df1['Price'].max()]
print(df2)

df1 = df.groupby('Type').get_group('Sporty')
df2 = df1[df1['Price'] == df1['Price'].max()]
print(df2)

df1 = df.groupby('Type').get_group('Van')
df2 = df1[df1['Price'] == df1['Price'].max()]
print(df2)

#1c
def Models(Manufacturer):
    df3 = df.groupby(['Manufacturer'])['Model'].get_group(f"{Manufacturer}")
    print(df3)

Models(sys.argv[1])

#1d
df4 = df.groupby('Manufacturer').size()
index4 = [i + 1 for i in range (len(df4))]
dict4 = {'':index4,'Count':df4}
df4 = pd.DataFrame(dict4)
index4 = pd.Index(range(1, len(df4) + 1,1))
df4 = df4.set_index(index4)
df4.to_csv("C:\\Users\\hp\\Desktop\\b22144_assignment8\\b22144_assignment8\problem1d.csv")




