class UPDOWN:
    def __init__(self):
        self.gangjong = "0"
        self.component = "0"
        self.distance = "0"
        self.prediction = "0"
    def updown(self, gangjong, component, distance, prediction):
        self.gangjong = gangjong
        self.component = component
        self.distance = distance
        self.prediction = prediction

        if distance == 0:
            return '이상치 없음'

        import joblib
        import numpy as np

        le = joblib.load('C:/seahFFF/static/model/gubun.pkl') # 세아창원특수강 요청으로 이상치 유무 판별하는 학습기 객체 삭제. 실제의 경우 성분비들을 바탕으로 이상치 유무 판별
        gangjonggubun = le.transform([gangjong])[0]
        test_set = []
        test_set.append(gangjonggubun)
        for i in component:
            test_set.append(i)
        test_set.append(distance)
        test_set.append(prediction)
        test = np.asarray(test_set, dtype=float)
        test = np.array([test])
        lgb = joblib.load('C:/seahFFF/static/model/updown.pkl') # 세아창원특수강 요청으로 이상치 유무 판별하는 학습기 객체 삭제. 실제의 경우 어느 방식으로 이상치 인지 삭제

        result = lgb.predict(test)

        if result[0] == 1:
            esang = '상승이상치'
        else:
            esang = '하강이상치'

        if esang == '상승이상치':
            return (prediction +delta) # 세아창원특수강 요청으로 구체적인 수치 가림
        else:
            return (prediction - delta) # # 세아창원특수강 요청으로 구체적인 수치 가림