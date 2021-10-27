class Detection:
    def __init__(self):
        self.gubun = "0"
        self.component = "0"

    def outlier(self,gubun,component):
        self.gubun = gubun
        self.component = component
        import pandas as pd
        esangchi = pd.read_excel('C:/seahFFF/static/model/OutLier.xlsx') # 세아창원특수강 요청으로 파일 삭제. Outlier인 데이터만을 모은 파일 존재
        esangchi.drop(columns=['HEAT_NO', '제강구분', '강종코드', '사내강종', 'cool_rate', 'Unnamed: 0'], inplace=True)
        gubun_table = esangchi[esangchi['강종구분'] == gubun]

        # def chulruk(x):
        #     for i in range(len(x)):
        #         print(f'{x[i]}mm에서 이상치 발생가능')

        def cosine(x, y):
            from numpy import dot
            from numpy.linalg import norm
            result = dot(x, y) / (norm(x) * norm(y))
            return result

        gubun_table.reset_index(drop=True, inplace=True)

        cosine_list = []
        for i in range(len(gubun_table)):
            cosine_list.append(cosine(self.component, gubun_table.iloc[i, 1:18]))

        gubun_table['유사도'] = pd.Series(cosine_list)
        gubun_table['cosine_rank'] = gubun_table['유사도'].rank(method='min', ascending=False)
        if gubun_table['유사도'].max() > alpha: # 세아창원특수강 요청으로 구체적인 수치 가림
            outlier_distance = list(gubun_table[gubun_table['cosine_rank'] == 1].iloc[:, 18])
            return outlier_distance
        else:
            return [0]