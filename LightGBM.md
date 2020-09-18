# LightGBM



`feature_fraction`



`max_features`: 최대 선택할 특성의 수(default=제곱근)

`min_samples_leaf`: 말단 노드가 되기 위한 최소한의 샘플 데이터 수. 과적합 개선.

`min_samples_split`: 노드를 분할하기 위한 최소한의 데이터 수. 



`loss`: 경사하강법에서 사용할 비용 함수

`learning_rate`: 경사하강법에서 사용. 0과 1사이. (default= 0.1)

`subsample`: 학습에 사용하는 데이터 샘플링 비율



`num_iterations`: 계속해서 나무를 부스팅하는데, 몇번을 할 것인가(default=100). 일반적으로 1000 이상 해줌.

`max_depth`: 나무의 깊이.( default=6)

`num_leave`: 잎사귀 수. 

`colsample_bytree`: 컬럼 샘플링으로 정확도가 올라감. (default=1). 보통 0.7~0.9정도로 함.



