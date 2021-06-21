import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(5)
n_sample = 1000
height = 4*np.random.randn(n_sample).round(2) + 170 #mean : 170 표준편차 :4
weight = 5*np.random.randn(n_sample).round(2) + 65
df_raw=pd.DataFrame({"height":height,"weight":weight})
print(df_raw[:5])
#copy data
df=df_raw.copy()
sns.distplot(df.height.values)

#standardization
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()
df[['h_sc','v_sc']]=scale.fit_transform(df[['height','weight']])
print(df[:5])
#reverse transform
scale.inverse_transform(df[['h_sc','v_sc']])[:5]
#히스토다이어그램
sns.distplot(df.h_sc.values)
df[['height','weight']].plot.kde()
df[['h_sc','v_sc']].plot.kde() # 표준화 그래프 비교