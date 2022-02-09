# seah_project

Project Seah Changwon TeukSueGang in Changwon. Republic of South korea

make AI based Jominy hardness prediction support system with BigLeader AI academy(https://bigleader.net/)

Jominy Hardness(https://en.wikipedia.org/wiki/Hardenability)

some codes are deleted for securety

# 세아창원특수강 조미니 경도 예측 보조시스템

경상남도에 있는 특수강 전문 기업인 세아창원특수강과 함께 조미니 경도 예측 보조시스템을 진행했습니다.

학습모델의 평가의 경우 (실제값 - 예측값)이 특정 수치보다 낮은 것의 비율로 정의를 하였습니다.

단순 예측뿐만 아니라, Abnormal Detection이나 component recommendation도 구현을 하였습니다.

학습의 데이터나 결과나 코드 중간에 있는 특정 수치의 경우 기업의 기밀유지서약서에 의해 공개될 수 없음을 알려드립니다.

# 아쉬운 것들
## 기업의 최종목표 : AutoMative System

-전처리 과정\
--데이터를 특정 성분으로 나눈다는 것? okay. 그러나 어느 지표를 사용하여 자동화?? -> P-value or 분산???\
--특정 성분을 선택하는 것도 자동으로 하고싶으면 어떻게 할까?? -> 비지도학습을 통해 묶어 볼 수 있을지 않을까??\

-모델링\
--stratified k-fold 교차검정 : k검정 진행을 해볼 것. k의 mini-batch에 대해서만 잘 나올 경우 가중치를 계속 유지하고, 비슷하게 나올 경우 지속적인 가중치 갱신 가능!!!!\

## 어떻게 확장이 가능할까?\
-Outlier Detection : Variational Encoder 등을 활용해볼 것.\
-성분비 추천 : 결국은 다양한 objective function을 만족하는 최적화 문제. 어떻게 자동화 시켜서 다 구할까?\
-냉각변수 활용 : 다중공산성 문제? 이것을 어떻게 해결할지..
