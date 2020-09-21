# xgboost



## 1. GBM(Gradient boosting)

>(1) __부스팅__ 알고리즘: 순차적으로 학습-예측하면서 잘못 예측한 데이터에 가중치를 부여해 오류를 개선하는 학습방식.
>
>(2) 가중치 업데이트를 경사하강법을 통해 함.
>
>(3) 랜덤 포레스트와 달리 이전 tree의 오차를 보완하는 방식으로 순차적으로 tree를 만듬.



- 무작위성이 없음. 가지치기 사용.1~5정도의 얕은 깊이의 트리 사용. 





### 하이퍼 파라미터 튜닝 

`random_state`: 고정값을 주자.



`n_estimators`: 계속해서 나무를 부스팅하는데, 몇번을 할 것인가(default=100). 일반적으로 1000 이상 해줌.

`max_depth`: 나무의 깊이(defult=6). 보통 3~10 사이로 사용.

`min_child_weight`:  과적합 방지를 위해 사용. 너무 높은 값은 과소적합을 야기하므로 CV에 의해 조절함. 대략 1~20정도?

`subsample`: 학습에 사용하는 데이터 샘플링 비율

`colsample_bytree`: 컬럼 샘플링으로 정확도가 올라감. (default=1). 보통 0.7~0.9정도로 함.



`loss`: 경사하강법에서 사용할 비용 함수

`learning rate(또는 eta)`:  경사하강법에서 사용. 0과 1사이. (default=0.3)



```python
# 예시
params_rs_xgb = {
'booster': ['dart','gbtree'],
'n_estimators': [1000,2000],
'min_child_weight':[1,5,10],
'max_depth': [10,15,20],
'colsample_bytree': [0.7, 0.8],
'subsample': [0.7, 0.8],
'learning_rate':[0.05,0.1,0.2],  # learning rate
}

params_basic_xgb={
'random_state': 1
}
```







[참고]

- https://statkclee.github.io/model/model-python-xgboost-hyper.html