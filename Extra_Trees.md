# 엑스트라 트리 (Extra Tree, Extremely Randomized Tree)

>- 랜덤 포레스트: 노드 분리시 임의의 독립 변수 중에서 최선의 독립 변수를 선택한다
>
>- 엑스트라 트리: 노드에서 랜덤하게 독립변수를 선택한다. 



```python
# 분류
from sklearn.ensemble import ExtraTreesClassifier

xtree = ExtraTreesClassifier(n_estimators=5, random_state=2)
xtree.fit(X_train, y_train)
```

