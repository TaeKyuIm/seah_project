#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
# 경고창 무시
from sklearn.model_selection import train_test_split
from catboost import CatBoostRegressor
import matplotlib.pyplot as plt
import seaborn as sns

import platform

path = 'C:/Windows/Fonts/malgun.ttf'
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname=path).get_name()
rc('font', family = font_name)


# In[2]:


data = pd.read_excel('seah_final.xlsx')
data.head()


# In[3]:


data.drop(columns=['Unnamed: 0', 'HEAT_NO', '제강구분', '강종구분', '강종코드', '사내강종'], inplace=True)
data.head()


# In[4]:


def make_cool_rate(df):
    df['cool_rate']=0.0
    df['cool_rate'][df['B'] >= 0.0005] = 2.94 - 0.75*(2.7*df['C'] + 0.4*df['Si']+df['Mn']+0.45*df['Ni']+0.8*df['Cr']+2*df['Mo'])
    df['cool_rate'][df['B'] < 0.0005] = 3.69 - 0.75*(2.7*df['C'] + 0.4*df['Si']+df['Mn']+0.45*df['Ni']+0.8*df['Cr']+df['Mo'])
    return df
# domain 지식을 활용한 feature engineering


# In[5]:


make_cool_rate(data)


# In[6]:


print(data['경도'].corr(data['cool_rate']))
print(data['경도'].cov(data['cool_rate']))


# In[7]:


def score(test, pred):
    print('+-1  :',sum(abs(test.values-pred) < 1)/len(test))
    print('+-2:',sum(abs(test.values-pred) < 2)/len(test))
    print('+-3  :',sum(abs(test.values-pred) < 3)/len(test))


# In[8]:


securety = data[data['Nb'] >= a] # 세아창원특수강 요청으로 구체적인 수치 가림
securety.shape


# In[9]:


seed = 100
# 난수발생시드 고정


# In[10]:


sns.scatterplot(data[securety], data['경도']) # 산점도를 그려 EDA 진행


# In[11]:


from sklearn.model_selection import train_test_split
y_hnb = securety['경도']
X_hnb = securety.drop(columns = '경도')
X_train, X_test, y_train, y_test = train_test_split(securety, securety, test_size=0.2, random_state=seed)

from catboost import CatBoostRegressor
cat_hnb = CatBoostRegressor(learning_rate = 0.085, subsample=0.8 ,depth = 10, eval_metric = 'MAE'
                        , thread_count=4, grow_policy = 'Lossguide',max_leaves =1023, early_stopping_rounds = 4
                        , leaf_estimation_method= 'Gradient', leaf_estimation_iterations = 64
                        ,mvs_reg = 16, bootstrap_type='MVS', boosting_type = 'Plain', iterations= 1000,random_state=seed, one_hot_max_size=15)
securety.fit(X_train, y_train)
securety = securety.predict(X_test)

score(y_test,securety)


# In[12]:


sns.scatterplot(data[securety], data['경도']) # 산점도를 그려 EDA 진행


# In[13]:


low_Nb = data[data[securety] < b] # 세아창원특수강 요청으로 구체적인 수치 제거
low_Nb.shape


# In[14]:


sns.scatterplot(securety[securety], low_Nb['경도']) # 산점도를 그려 EDA 진행


# In[15]:


sns.distplot(securety[securety]) # 산점도를 그려 EDA 진행


# In[16]:


securety = low_Nb[low_Nb[securety] >= c] # 세아창원특수강 요청으로 구체적인 수치 삭제
securety.shape


# In[17]:


from sklearn.model_selection import train_test_split
securety = securety['경도']
securety = securety.drop(columns = '경도')
X_train, X_test, y_train, y_test = train_test_split(X_lnb_hignMo, y_lnb_highMo, test_size=0.2, random_state=seed)

from catboost import CatBoostRegressor
securety = CatBoostRegressor(learning_rate = 0.085, subsample=0.8 ,depth = 10, eval_metric = 'MAE'
                        , thread_count=4, grow_policy = 'Lossguide',max_leaves =1023, early_stopping_rounds = 4
                        , leaf_estimation_method= 'Gradient', leaf_estimation_iterations = 64
                        ,mvs_reg = 16, bootstrap_type='MVS', boosting_type = 'Plain', iterations= 1000,random_state=seed, one_hot_max_size=15)
securety.fit(X_train, y_train)
securety = securety.predict(X_test)

score(y_test, securety)


# In[18]:


securety = securety[securety[securety] < c] # 세아창원특수강 요청으로 구체적인 수치 삭제
securety = securety[securety[securety] >= d]
securety.shape


# In[19]:


from sklearn.model_selection import train_test_split
securety = low_Nb_mid_Mo['경도']
securety = low_Nb_mid_Mo.drop(columns = '경도')
X_train, X_test, y_train, y_test = train_test_split(X_lnb_midMo, y_lnb_midMo, test_size=0.2, random_state=seed)

from catboost import CatBoostRegressor
securety = CatBoostRegressor(learning_rate = 0.085, subsample=0.8 ,depth = 10, eval_metric = 'MAE'
                        , thread_count=4, grow_policy = 'Lossguide',max_leaves =1023, early_stopping_rounds = 4
                        , leaf_estimation_method= 'Gradient', leaf_estimation_iterations = 64
                        ,mvs_reg = 16, bootstrap_type='MVS', boosting_type = 'Plain', iterations= 1000,random_state=seed, one_hot_max_size=15)
securety.fit(X_train, y_train)
securety = securety.predict(X_test)

score(y_test, securety)


# In[20]:


securety = securety[securety[securety] < e] # 세아창원특수강 요청으로 구체적인 수치 제거
securety.shape


# In[21]:


from sklearn.model_selection import train_test_split
securety = securety['경도']
securety = securety.drop(columns = '경도')
X_train, X_test, y_train, y_test = train_test_split(securety, securety, test_size=0.2, random_state=seed)

from catboost import CatBoostRegressor
cat_lnb_low_Mo = CatBoostRegressor(learning_rate = 0.085, subsample=0.8 ,depth = 10, eval_metric = 'MAE'
                        , thread_count=4, grow_policy = 'Lossguide',max_leaves =1023, early_stopping_rounds = 4
                        , leaf_estimation_method= 'Gradient', leaf_estimation_iterations = 64
                        ,mvs_reg = 16, bootstrap_type='MVS', boosting_type = 'Plain', iterations= 1000,random_state=seed, one_hot_max_size=15)
securety.fit(X_train, y_train)
securety = securety.predict(X_test)

score(y_test, securety)


# In[22]:


import joblib
joblib.dump(cat_hnb, securety)
joblib.dump(cat_lnb_high_Mo, securety)
joblib.dump(cat_lnb_mid_Mo, securety)
joblib.dump(cat_lnb_low_Mo, securety)

# pickle 형태로 학습기 객체 저장

