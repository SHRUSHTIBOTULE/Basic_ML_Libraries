import pandas as pd

#create a simple dataframe
data={
    'Name':['ALice','Bob','Charlie','ishuuu','harshuu'],
    'Age':[25,30,35,21,28],
    'City':['New York','Paris','London','turkey','bangalore'],
    'College':['Coep','Jdiet','Vnit','Vjt','Dy patil']
}
df = pd.DataFrame(data)

#Display the DataFrame
print(df)

#Access a column
print(df['Name'])

#Basic statistics
print(df['Age'].mean())   #Average age

#Filter rows
print(df[df['Age']>28])

print(df['College'].median())