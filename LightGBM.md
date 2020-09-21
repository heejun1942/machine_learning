# LightGBM





### 하이퍼파라미터 튜닝

>과적합 방지를 위해  `num_leave`를 작게 주거나,  `bagging_fraction`과 `feature_fraction`을 사용한다.

`num_iterations`: 계속해서 나무를 부스팅하는데, 몇번을 할 것인가(default=100). 일반적으로 1000 이상 해줌.

`max_depth`: 나무의 깊이.( default=-1)

`num_leave`: 잎사귀 수. 

`subsample( 또는 bagging_fraction)`: 학습에 사용하는 데이터 샘플 비율

`colsample_bytree(또는 feature_fraction)`: 컬럼 샘플링으로 정확도가 올라감. (default=1). 보통 0.7~0.9정도로 함.

`loss`: 경사하강법에서 사용할 비용 함수

`learning_rate`: 경사하강법에서 사용. 0과 1사이. (default= 0.1)



```python
# 예시
params_rs_lgbm = {
'boosting_type': ['gbdt','dart'],
'learning_rate':[0.05 ,0.1, 0.2],
'num_leaves': np.arange(30 ,50+1, 10),
'max_depth' : np.arange(30, 120+1, 30),
'colsample_bytree': [0.7, 0.8],
'subsample': [0.7, 0.8],        
}

params_lgbm = {
'random_seed': 1,
'n_estimators': 2000
} 
```



