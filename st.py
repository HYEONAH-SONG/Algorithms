import numpy as np
import pandas as pd

#sample data
np.random.seed(48)
df = pd.DataFrame(10*np.random.rand(4,2).round(2))
df.columns = ["A","B"]
df.A[1] = np.nan # adding nan'
df.isnull() #check missing value
df.isnull().sum()
df2 = df.dropna() # delete row
df3 = df.dropna(axis=1) # delete col
df4 = df.dropna(how="all") # show all
df.B[1]= np.nan
print(df.dropna(how="all")) # 행, 열이 전체 nan이면 삭제 아니면 그대로
df5 =pd.DataFrame([[np.nan,np.nan,np.nan],[1,np.nan,np.nan],[2,3,np.nan],[4,5,6],[np.nan,7,8]])
print(df5.dropna(thresh=3,axis=1)) # col에 nan이 아닌 데이터가 3개 이상 존재: 삭제x/ 아닌 경우 col 삭제
df.fillna(0).head() #nan부분을 0으로 채움
df.fillna(method="ffill").head() # 위의(이전)값이 들어온다
df.fillna(method="bfill").head() # 아래(다음)값이 들어온다
df.fillna(method="bfill", axis=1).head() # 오른쪽 값이 들어온다
print(df.mean(axis=0).round(2))
print(df.mean(axis=1).round(2))
df.fillna(df.mean().round(2)).head()

