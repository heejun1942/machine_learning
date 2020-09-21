# Random Forest

>앙상블 머신러닝 모델.
>
>다수의 의사결정나무를 만들어 다수결의 원칙으로 최종값을 결정.

의사결정나무는 가지치기를 하지만 학습데이터에 오버피팅되는 경향이 있음

복원추출



### 1. 분류와 회귀

의사결정나무는 **분류(classification)**와 **회귀(regression)** 모두 가능합니다. 즉, 범주나 연속형 수치 모두 예측할 수 있습니다. 의사결정나무의 범주예측, 즉 분류 과정은 이렇습니다. 새로운 데이터가 특정 terminal node에 속한다는 정보를 확인한 뒤 해당 terminal node에서 가장 빈도가 높은 범주에 새로운 데이터를 분류하게 됩니다. 운동경기 예시를 기준으로 말씀드리면 날씨는 맑은데 습도가 70을 넘는 날은 경기가 열리지 않을 거라고 예측합니다.

회귀의 경우 해당 terminal node의 종속변수(y)의 평균을 예측값으로 반환하게 되는데요, 이 때 __예측값의 종류는 terminal node 개수와 일치합니다.__ 만약 terminal node 수가 3개뿐이라면 새로운 데이터가 100개, 아니 1000개가 주어진다고 해도 의사결정나무는 딱 3종류의 답만을 출력하게 될 겁니다.



```python
# 모델 생성
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators = 100)
model.fit(train_X, train_y)
```

`model.estimators_`: 랜덤포레스트의 나무들 확인가능.



### Hyper Parameter

>랜덤 포레스트는 하이퍼파라미터의 튜닝이 많이 필요하지 않다. 일반적으로 유일한 튜닝은 `n_estimators` 이다.

`n_estimators`: 의사결정나무의 개수 (default=10). 클수록 좋음

`max_depth`: 나무의 깊이.

`max_features`: 최대 선택할 특성의 수(default=[분류] 제곱근, [회귀] n_features). 보통 default 사용.

`min_samples_leaf`: 말단 노드가 되기 위한 최소한의 샘플 데이터 수 (default=1). 과적합 개선

`min_samples_split`: 노드를 분할하기 위한 최소한의 데이터 수 (default=2)

`ccp_alpha`: 모델 복잡도를 cost에 얼마나 반영할지. 보통 0.01~0.1사용.

​	(설명은 https://soobarkbar.tistory.com/17 참고)



```python
# 예시
params_rs_rf = {
'n_estimators': np.arange(100,400+1,100),
'max_depth':np.arange(10,40+1,10),
'max_features': ['auto','sqrt'],
'ccp_alpha': [0.0, 0.01, 0.05],
} 

params_basic_rf_et = {
'random_state': 1
} 
```











[출처]

https://woolulu.tistory.com/28

