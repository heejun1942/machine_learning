# Random Forest

>앙상블 머신러닝 모델.
>
>다수의 의사결정나무를 만들어 다수결의 원칙으로 최종값을 결정.

의사결정나무는 가지치기를 하지만 학습데이터에 오버피팅되는 경향이 있음

복원추출





```python
from sklearn.ensemble import RandomForestClassifier

classifier = RandomForestClassifier(n_estimators = 100)
```





### Hyper Parameter

>랜덤 포레스트는 하이퍼파라미터의 튜닝이 많이 필요하지 않다. 일반적으로 유일한 튜닝은 n_estimators임 

`n_estimators`: 의사결정나무의 개수 (default=10). 클수록 좋음

`max_features`: 최대 선택할 특성의 수(default=[분류] 제곱근, [회귀] n_features). 보통 default 사용.

`max_depth`: 나무의 깊이.

`min_samples_leaf`: 말단 노드가 되기 위한 최소한의 샘플 데이터 수 (default=1). 과적합 개선

`min_samples_split`: 노드를 분할하기 위한 최소한의 데이터 수 (default=2)

`ccp_alpha`: 비용 복잡도(cost complexity)에 들어가는 변수. 보통 0.01~0.1사용.

- https://soobarkbar.tistory.com/17 참고









`forest.estimators_`: 랜덤포레스트의 나무들 확인가능.









[출처]

https://woolulu.tistory.com/28

