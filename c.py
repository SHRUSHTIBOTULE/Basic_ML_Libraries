import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

#sample dataframe
df = pd.DataFrame({'Gender':['Male','Female','Female','Male'],'Score':[85,90,78,88]})
                             

#plot a boxplot

sns.boxplot(x='Gender',y='Score',data=df)
plt.show()