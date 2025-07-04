import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

#sample dataframe
df = pd.DataFrame({'Branch':['Entc','Textile','Textile','Entc','Ee','Mech','Mech','Ee'],'Score':[85,90,78,88,96,30,75,85]})
                             

#plot a boxplot

sns.boxplot(x='Branch',y='Score',data=df)
plt.show()