import joblib
import numpy as np
import app
import catboost as cat
from lightgbm import LGBMClassifier as lgb
import pandas as pd
from flask import Flask, render_template, request
from flask_googlecharts import GoogleCharts
from detection import Detection
from esang import UPDOWN
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta
app = Flask(__name__)

@app.before_first_request
def load_model_to_app():
    app.predictor1 = joblib.load('C:/seahFFF/static/model/high_Nb_model.pkl')
    app.predictor2 = joblib.load('C:/seahFFF/static/model/low_Nb_big_Mo_model.pkl')
    app.predictor3 = joblib.load('C:/seahFFF/static/model/low_Nb_mid_Mo_model.pkl')
    app.predictor4 = joblib.load('C:/seahFFF/static/model/low_Nb_small_Mo_model.pkl')
    # 세아창원특수강 요청으로 구체적인 학습기 객체 저장한 파일 삭제.실제의 경우 pkl 형태로 학습기 객체를 불러와서 경도 예측 진행


@app.route('/suggest', methods=['POST'])
def suggest():
    steel = str(request.values.get("strongbell"))
    geori = float(request.values.get("rjfl"))
    gyeongdo = float(request.values.get("rudeh"))
    suggest = list(db.seahdata.find({'강종구분': steel, '거리': geori},{'_id': False}))
    ac = []
    for i in range(len(suggest)):
        if gyeongdo-suggest[i]['경도'] ==0:
            ac.append(suggest[i])


    return render_template('suggest.html', ac= ac)



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/interval', methods=['POST'])
def interval():
        dic1={'C':[request.form["C"]],
              'Si': [request.form["Si"]],
              'Mn': [request.form["Mn"]],
              'P': [request.form["P"]],
              'S': [request.form["S"]],
              'Ni': [request.form["Ni"]],
              'Cr': [request.form["Cr"]],
              'Mo': [request.form["Mo"]],
              'Cu': [request.form["Cu"]],
              'Sn': [request.form["Sn"]],
              'Tol-Al': [request.form["Al"]],
              'V': [request.form["V"]],
              'Ti': [request.form["Ti"]],
              'B': [request.form["B"]],
              'N': [request.form["N"]],
              'Nb': [request.form["Nb"]],
              'Ca': [request.form["Ca"]]}
        KS = np.array([1.5, 3, 5, 7, 9, 11, 13, 15, 20, 25, 30, 35, 40, 45, 50])
        data = pd.DataFrame(dic1, index = range(15))
        data['거리'] = KS


        dic = {'Chemical': 'numerical',
               'C': float(request.values.get("C")),
               'Si': float(request.values.get("Si")),
               'Mn': float(request.values.get("Mn")),
               'P': float(request.values.get("P")),
               'S': float(request.values.get("S")),
               'Ni': float(request.values.get("Ni")),
               'Cr': float(request.values.get("Cr")),
               'Mo': float(request.values.get("Mo")),
               'Cu': float(request.values.get("Cu")),
               'Sn': float(request.values.get("Sn")),
               'Tol-Al': float(request.values.get("Al")),
               'V': float(request.values.get("V")),
               'Ti': float(request.values.get("Ti")),
               'B': float(request.values.get("B")),
               'N': float(request.values.get("N")),
               'Nb': float(request.values.get("Nb")),
               'Ca': float(request.values.get("Ca"))}
        chemic_list = list(dic.values())
        del chemic_list[0]
        steel = str(request.values.get("strongbell"))
        a = Detection()
        b = UPDOWN()
        result = a.outlier(steel, chemic_list)


        if float(data['B'][0]) >=0.005 :
            cool_rate = 2.94 - 0.75*(2.7*float(data['C'][0])+0.4*float(data['Si'][0])+float(data['Mn'][0])
                                      +0.45*float(data['Ni'][0])+0.8*float(data['Cr'][0])+2*float(data['Mo'][0]))
            data['cool_rate'] = cool_rate
        else :
            cool_rate = 3.69 - 0.75*(2.7*float(data['C'][0])+0.4*float(data['Si'][0])+float(data['Mn'][0])
                                      +0.45*float(data['Ni'][0])+0.8*float(data['Cr'][0])+2*float(data['Mo'][0]))
            data['cool_rate'] = cool_rate
        test_dic = {}
        bojung_lst = []
        ks_lst = [1.5, 3, 5, 7, 9, 11, 13, 15, 20, 25, 30, 35, 40, 45, 50]
        indexlist = np.where(np.isin(ks_lst, result), 1, 0)
        empty = []
        count = 0


        if float(data[securety][0]) >p :# 세아창원특수강 요청으로 구체적인 성분 및 수치 가림
            predictions = app.predictor1.predict(data)
            test_lst = list(predictions)
            if type(result[0]) == float:
                for i in result:
                    test_dic[i] = test_lst[ks_lst.index(i)]
                key = list(test_dic.keys())
                value = list(test_dic.values())
                for j in range(len(key)):
                    temp = b.updown(steel, chemic_list, key[j], value[j])
                    bojung_lst.append(temp)
                for k in range(15):
                    if indexlist[k] == 1:
                        empty.append(bojung_lst[count])
                        count += 1
                    else:
                        empty.append(predictions[k])
            return render_template('intervalgraph.html', pred=predictions, dis=data['거리'],data=dic,test=result,
                                    test_1=bojung_lst, number=indexlist, msg=1, graph = empty)

        else:
            if float(data[securety][0]) >= q:# 세아창원특수강 요청으로 구체적인 성분 및 수치 가림
                predictions = app.predictor2.predict(data)
                test_lst = list(predictions)
                if type(result[0]) == float:
                    for i in result:
                        test_dic[i] = test_lst[ks_lst.index(i)]
                    key = list(test_dic.keys())
                    value = list(test_dic.values())
                    for j in range(len(key)):
                        temp = b.updown(steel, chemic_list, key[j], value[j])
                        bojung_lst.append(temp)
                    for k in range(15):
                        if indexlist[k] == 1:
                            empty.append(bojung_lst[count])
                            count += 1
                        else:
                            empty.append(predictions[k])
                return render_template('intervalgraph.html', pred=predictions, dis=data['거리'], data=dic, test=result,
                                        test_1=bojung_lst, number=indexlist, msg=2, graph=empty)

            elif float(data[securety][0]) >= r:# 세아창원특수강 요청으로 구체적인 수치 가림
                predictions = app.predictor3.predict(data)
                test_lst = list(predictions)
                if type(result[0]) == float:
                    for i in result:
                        test_dic[i] = test_lst[ks_lst.index(i)]
                    key = list(test_dic.keys())
                    value = list(test_dic.values())
                    for j in range(len(key)):
                        temp = b.updown(steel, chemic_list, key[j], value[j])
                        bojung_lst.append(temp)
                    for k in range(15):
                        if indexlist[k] == 1:
                            empty.append(bojung_lst[count])
                            count += 1
                        else:
                            empty.append(predictions[k])
                else:
                    bojung_lst.append("이상치없음")
                return render_template('intervalgraph.html', pred=predictions, dis=data['거리'], data=dic, test=result,
                                       test_1=bojung_lst, number=indexlist, msg = 3, graph = empty)
            else:
                predictions = app.predictor4.predict(data)
                test_lst = list(predictions)
                if type(result[0]) == float:
                    for i in result:
                        test_dic[i] = test_lst[ks_lst.index(i)]
                    key = list(test_dic.keys())
                    value = list(test_dic.values())
                    for j in range(len(key)):
                        temp = b.updown(steel, chemic_list, key[j], value[j])
                        bojung_lst.append(temp)
                    for k in range(15):
                        if indexlist[k] == 1:
                            empty.append(bojung_lst[count])
                            count += 1
                        else:
                            empty.append(predictions[k])
                else:
                    bojung_lst.append("이상치없음")
                return render_template('intervalgraph.html', pred=predictions, dis=data['거리'], data=dic, test=result
                                        ,test_1=bojung_lst, number=indexlist, msg=4, graph=empty)

if __name__=='__main__':
    app.run(debug=True)