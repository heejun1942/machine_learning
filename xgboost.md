# xgboost



## 1. GBM(Gradient boosting)

>(1) __부스팅__ 알고리즘: 순차적으로 학습-예측하면서 잘못 예측한 데이터에 가중치를 부여해 오류를 개선하는 학습방식.
>
>(2) 가중치 업데이트를 경사하강법을 통해 함.
>
>(3) 랜덤 포레스트와 달리 이전 tree의 오차를 보완하는 방식으로 순차적으로 tree를 만듬.



- 무작위성이 없음. 가지치기 사용.1~5정도의 얕은 깊이의 트리 사용. 





`max_features`: 최대 선택할 특성의 수(default=제곱근)

`min_samples_leaf`: 말단 노드가 되기 위한 최소한의 샘플 데이터 수. 과적합 개선.

`min_samples_split`: 노드를 분할하기 위한 최소한의 데이터 수. 



`loss`: 경사하강법에서 사용할 비용 함수

`eta`: learning rate. 경사하강법에서 사용. 0과 1사이. (default= 0.1)

`subsample`: 학습에 사용하는 데이터 샘플링 비율



`num_iterations`: 계속해서 나무를 부스팅하는데, 몇번을 할 것인가(default=100). 일반적으로 1000 이상 해줌.

`max_depth`: 나무의 깊이.

`num_leave`: 잎사귀 수. 

`colsample_bytree`: 컬럼 샘플링으로 정확도가 올라감. (default=1). 보통 0.7~0.9정도로 함.

