# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 14:05:34 2020

@author: ust21
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split

x, y = make_moons(n_samples=100, noise=0.25, random_state=3) # noise: Standard deviation of Gaussian noise added to the data.

x_train, x_test, y_train, y_test = train_test_split(x, y, stratify=y, random_state=42)

forest = RandomForestClassifier(n_estimators=5, n_jobs=-1, random_state=42) # n_estimators: 사용할 tree수

forest.fit(x_train, y_train)



import matplotlib.pyplot as plt
import numpy as np
from mglearn.plots import plot_2d_classification

_, axes = plt.subplots(2, 3)
marker_set = ['o', '^']

for i, (axe, tree) in enumerate(zip(axes.ravel(), forest.estimators_)):
    axe.set_title('tree {}'.format(i))
    plot_2d_classification(tree, x, fill=True, ax=axe, alpha=0.4)

    for i, m in zip(np.unique(y), marker_set):
        axe.scatter(x[y==i][:, 0], x[y==i][:, 1], marker=m, label='class {}'.format(i), edgecolors='k')
        axe.set_xlabel('feature 0')
        axe.set_ylabel('feature 1')

axes[-1, -1].set_title('random forest')
axes[-1, -1].set_xlabel('feature 0')
axes[-1, -1].set_ylabel('feature 1')
plot_2d_classification(forest, x, fill=True, ax=axes[-1, -1], alpha=0.4)

for i, m in zip(np.unique(y), marker_set):
    plt.scatter(x[y==i][:, 0], x[y==i][:, 1], marker=m, label='class {}'.format(i), edgecolors='k')

plt.show()