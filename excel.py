import pandas as pd

df = pd.read_excel (r'C:\Users\Aamer\OneDrive\Documents\Python\hepevento\excel.xlsx')

list  = df.values.tolist()



for i in range(len(list)):
    print("user #" + str(i+1))
    for n in list[i]:
        print(n)

