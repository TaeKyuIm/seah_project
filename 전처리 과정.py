#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


# 화학성분 테이블 불러옴
composition = pd.read_excel('chemical composition.xlsx')


# In[3]:


composition.head()


# In[4]:


# 히트넘버 컬럼이름 통일
composition.rename(columns = {'Heat_NO':'HEAT_NO'},inplace=True)

composition.info()


# In[5]:


composition.isna().sum() # NaN값 처리필요


# In[6]:


composition[composition['C'].isna()]


# In[7]:


# 누락행 제거
composition.dropna(inplace=True)


# In[8]:


composition['HEAT_NO'].value_counts()


# In[9]:


# 중복 정보 제거
composition = composition.drop_duplicates()

composition.describe()


# In[10]:


# N 이상치 제거
composition.drop(composition[composition['N']<0].index,inplace=True)


# In[11]:


#거리/경도 데이터 불러옴
jominy = pd.read_excel('jominy.xlsx')


# In[12]:


# 결측치 NaN과 0을 0으로 통합
jominy.fillna(0,inplace=True)


# In[13]:


# 키값을 따온 빈 데이터프레임 설정
jominy_ = pd.DataFrame(jominy['HEAT_NO'])
jominy_.reset_index(drop=True,inplace=True)


# In[14]:


# 두 측정지점의 경도값 차 테이블생성
# 경도값이 0인 부분에서는 경도차이를 계산하지 않음
for i in range(16):
    jominy_['경도차'+str(i+1)]=0
    for j in range(len(jominy_)):
        if jominy['경도'+str(i+1)][j] == 0:
            jominy_['경도차'+str(i+1)][j] = 0
        else:
            jominy_['경도차'+str(i+1)][j] = jominy['경도'+str(i+2)][j] - jominy['경도'+str(i+1)][j]
jominy_


# In[15]:


# 경도값이 상승하는 이상치 모음
# 구체적인 수치는 세아창원특수강 요청으로 삭제
isang = jominy_[(jominy_.iloc[:,1:17]>a).sum(axis=1)>a]


# In[16]:


# 이상치 중 시험2회+평균치로 실시시 같은 추세를 보인 히트넘버의 리스트 작성
ban_1 = dict(isang['HEAT_NO'].value_counts())
ban1 = []
for key, value in ban_1.items():
    if value == 3:
        ban1.append(key)
ban1


# In[17]:


# 2번+평균 모두 같은 추세를 보인 시편은 이상치가 아니라고 판단, 이상치데이터에서 제거
for i in ban1:
    isang.drop(isang[isang['HEAT_NO']==str(i)].index,inplace=True)
isang


# In[18]:


# 이상치 데이터에서 2번 등장한 히트넘버 리스트 작성
ban_3 = dict(isang['HEAT_NO'].value_counts())
ban3 = []
for key, value in ban_3.items():
    if value == 2:
        ban3.append(key)
ban3


# In[19]:


# 시험2번+평균치인히트넘버 리스트 작성
ban_2 = dict(jominy['HEAT_NO'].value_counts())
ban2 = []
for key, value in ban_2.items():
    if value == 3:
        ban2.append(key)
ban2


# In[20]:


# 이상치 데이터에서 2번 등장한 히트넘버중, 시험이 2회와 평균치로 실시된 히트넘버를 제외한 리스트작성
# 시험이 2번시행되었고, 2번다 같은 이상추세를 보인 값은 이상치가 아니라고 판단
ban3_sub_ban2 = [x for x in ban3 if x not in ban2]
ban3_sub_ban2
# 모두 시험3번중 2번의 이상추세를 보인 데이터였음을 알수있음


# In[21]:


# 만약 위의 조건을 만족했다면 이상치 리스트에서 제거
for i in ban3_sub_ban2:
    isang.drop(isang[isang['HEAT_NO']==str(i)],inplace=True)
isang


# In[22]:


# 조미니 데이터에서 이상치 데이터 제거
# 구체적인 수치의 경우 세아창원특수강 요청으로 제거
jominy.drop(isang[(isang.iloc[:,1:17]>p).sum(axis=1)>p].index,inplace = True)
jominy


# In[23]:


# 히트넘버기준 그룹화
jominy_group = jominy.groupby(['HEAT_NO', '제강구분','강종구분', '강종코드','사내강종']).mean()
jominy_group


# In[24]:


# 인덱스 다시 재설정
jominy_group.reset_index(inplace = True)
jominy_group


# In[25]:


# 문자열 데이터 head에 저장
jominy_head = jominy_group.iloc[:,0:5]
jominy_head


# In[26]:


# 거리/경도데이터 tail에 저장
jominy_tail = pd.concat([jominy_group.iloc[:,0], jominy_group.iloc[:,5:]], axis=1)
jominy_tail


# In[27]:


# head에 화학성분 병합
table_head = pd.merge(jominy_head, composition, on='HEAT_NO')
table_head


# In[28]:


# tail까지 병합
table = pd.merge(table_head, jominy_tail, on='HEAT_NO')
table


# In[29]:


# 거리 경도 일렬로 추가
notKs = pd.DataFrame()
for i in range(1,18):
    table_head['거리'] = table['거리'+str(i)]
    table_head['경도'] = table['경도'+str(i)]
    notKs = notKs.append(table_head)
notKs


# In[30]:


# 다시 인덱스 정리
notKs.reset_index(inplace = True,drop=True)
notKs


# In[31]:


# 거리가 0인 결측 행 삭제
notKs.drop(notKs.loc[notKs['거리']==0].index,inplace=True)
notKs


# In[32]:


# 경도가 0인 결측 행 삭제
notKs.drop(notKs.loc[notKs['경도']==0].index,inplace=True)
notKs.describe()


# In[33]:


# 세아에 자문을 구해 공정상 나올 수 없는 성분비의 경우 이상치로 정의하고 제거
# 구체적인 수치의 경우 세아창원특수강의 요청으로 삭제
def outlier(a):
    b = a[(a['C']<securety) & (a['Ca']<securety) & (a['Cr']<securety) 
      & (a['Mn']>securety) & (a['Ni']<securety) & (a['S']<securety) 
      & (a['Si']<securety) & (a['Tol-Al']<securety)]
    return b
data = outlier(notKs)
data


# In[34]:


# KS규격에 맞는 데이터만 수집
def ks(a):
    b = a[(a['거리']==1.5) | (a['거리']==3) | (a['거리']==5) | (a['거리']==7) | (a['거리']==9) | (a['거리']==11) | 
          (a['거리']==13) | (a['거리']==15) | (a['거리']==20) | (a['거리']==25) | (a['거리']==30) | 
          (a['거리']==35) | (a['거리']==40) | (a['거리']==45) | (a['거리']==50)]
    return b
data = ks(data)
data


# In[35]:


data.to_excel('seah_final.xlsx')


# In[36]:


data


# In[ ]:




