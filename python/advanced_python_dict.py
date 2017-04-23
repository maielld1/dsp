import pandas as pd
import itertools

df = pd.read_csv("faculty.csv")

#Q6
df['name'] = df['name'].apply(lambda s: s.split()[-1])
df[' title'] = df[' title'].str.replace(' of Biostatistics| is Biostatistics', '')

df = df.set_index('name').transpose()

q6_dict = df.to_dict('list')

x = itertools.islice(q6_dict.items(), 0, 3)

for key, value in x:
    print(key, value)
    
#Q7
df = pd.read_csv("faculty.csv")
df['first_name'] = tuple(df['name'].apply(lambda s: s.split()[0]))
df['last_name'] = tuple(df['name'].apply(lambda s: s.split()[-1]))
df['name'] = df[['first_name', 'last_name']].apply(tuple, axis = 1)
del df['first_name']
del df['last_name']

df = df.set_index('name').transpose()
q7_dict = df.to_dict('list')
print(q7_dict)

#Q8

q8_dict = df.to_dict('list')

for key, value in sorted(q8_dict.items(), key = lambda x: x[0][1]):
    print(key, ':', value)
