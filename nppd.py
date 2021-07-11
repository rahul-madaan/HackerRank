import numpy as np
import pandas as pd

d = {'key':['X','X','Y','Y','Z'],
     'X':np.arange(5), 'Y':[3,4,5,6,7]}

df = pd.DataFrame(d)

grouped_df = df.groupby('key')
mean_df = grouped_df.mean()

# mean_df = mean_df.reset_index()

print(mean_df)

#a = np.array([1,2,3,2,3,4,3,4,5,6])
# b= np.array([7,2,10,2,7,4,9,4,9,8])
#
# intersection = np.intersect1d(a,b)
#
# print(intersection)



#
# dframe = pd.DataFrame([[1,2,3,np.nan,4],
#                        [2,np.nan,5,6,4],
#                        [np.nan,7,np.nan,9,6],
#                        [1,np.nan,np.nan,6,7]])
# dframe = dframe.replace(np.nan, 99)
#
# print(dframe)