# 통계 모델: 선형회귀 분석 (Linear Regression Analysis)

import pandas as pd
from statsmodels.formula.api import ols
import operator
from itertools import combinations
from datetime import datetime
import time

start = datetime.fromtimestamp(time.time())
print("결과 예측하기")
house = pd.read_csv('Housing.csv',sep=',',header=0)
house.columns = house.columns.str.replace(' ','_')
house.replace('yes',1,inplace=True)
house.replace('no',0,inplace=True)
house = house.drop(house.columns[[0]],axis=1)

colums_list = ['lotsize', 'bedrooms', 'bathrms', 'stories', 'driveway',
       'recroom', 'fullbase', 'gashw', 'airco', 'garagepl', 'prefarea']

best_formula = None
best_score = -1

total_count = 0

# 예측값과 실제값의 차이 마진 비율
delta = 0.25 # 마진 비율의 값은 데이터/조직의 예측 목표에 따라 조절할 수 있다.
START_INDEX = 5
for num in range(START_INDEX,len(colums_list)+1):
    combi_list = list(combinations(colums_list,num))
    for tup in combi_list:
        my_formula = 'price ~ '
        for data in tup:
            my_formula+='%s + '%data
        my_formula = my_formula.strip().rstrip('+')
        lm = ols(my_formula, data=house).fit()
        dependent_variable = house['price']
        # independent_variables = house[house.columns.difference(['quality','type','in_sample'])]
        independent_variables = house[list(tup)] # formula 에 들어간 columns만 골라서 고정 변수로 줌
        y_predicted = lm.predict(independent_variables)

        match_count=0
        for index in range(len(y_predicted)):
            # | 예측값-실제값 | <= 차이를 절대값을 구한다.
            diff = abs(y_predicted[index] - dependent_variable.values[index])

            if (diff / dependent_variable.values[index]) < delta:
                match_count+=1
        acc = match_count / len(y_predicted) * 100
        print('\n>> '+my_formula.replace('price ~ ',''))
        print('>> match count=',match_count)
        print('>> 정답률: %.2f %%'%(match_count/len(y_predicted)*100))

        if acc>best_score:
            best_score = acc
            best_formula = my_formula

        total_count = total_count+1

print("\n\n 독립변수 최적화 분석 결과")
print('총 조합 갯수: %d'%(total_count))
print("MAX 조합: %s >> %.2f %%"%(best_formula,best_score))
end = datetime.fromtimestamp(time.time())
print(f'분석 시작: {start}')
print(f'분석 종료: {end}')
print(f'총 분석 시간: {end-start}')