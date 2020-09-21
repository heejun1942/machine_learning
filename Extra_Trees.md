# 엑스트라 트리 (Extra Tree, Extremely Randomized Tree)

>과적합을 막기위해 노드에서 독립변수를 랜덤하게 선택한다. 이로 인해 Random Forest 모델보다 학습 속도가 빠르다.



### 랜덤 포레스트 VS 엑스트라 트리

엑스트라 트리는 랜덤 포레스트와 거의 비슷한 모델임

(1) 랜덤 포레스트: 노드 분리시 임의의 독립 변수 중에서 최선의 독립 변수를 선택한다

(2) 엑스트라 트리: 노드에서 랜덤하게 독립변수를 선택한다. 



```python
# 모델 생성
from sklearn.ensemble import ExtraTreesClassifier

xtree = ExtraTreesClassifier(n_estimators=5, random_state=2)
xtree.fit(X_train, y_train)
```





### Hyper Parameter 튜닝

`n_estimators`: 의사결정나무의 개수 (default=10). 클수록 좋음

`max_depth`: 나무의 깊이.

`max_features`: 최대 선택할 특성의 수(default=[분류] 제곱근, [회귀] n_features). 보통 default 사용.

`min_samples_leaf`: 말단 노드가 되기 위한 최소한의 샘플 데이터 수 (default=1). 과적합 개선

`min_samples_split`: 노드를 분할하기 위한 최소한의 데이터 수 (default=2)

`ccp_alpha`: 모델 복잡도를 cost에 얼마나 반영할지. 보통 0.01~0.1사용.

​	(설명은 https://soobarkbar.tistory.com/17 참고)



```python
# 예시
param_rs_et ={
'n_estimators': np.arange(100,400+1,100),
'max_depth': np.arange(10,40+1,10),
'max_features': ['auto','sqrt'],
'ccp_alpha': [0.0, 0.01, 0.05],
}

params_basic_rf_et = {
'random_state': 1
} 
```





