"""
SVM Classification
Created on Sun Apr 23 18:56:14 2023

@author: QV-137
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('dataset.csv')
x = dataset.iloc[:, [2,3]].values # Characteristics vector
y = dataset.iloc[:, 4].values # Predictable vector

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)

# Adjust classifier on the training set
from sklearn.svm import SVC
classifier = SVC(kernel = 'linear', random_state = 0) # kernel = 'rbf' got a better fit
classifier.fit(x_train, y_train)

# Predict results with testing set
y_pred = classifier.predict(x_test)

# Create a Confusion Matrix (Matriz de Confusión)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

"""
 cm = | guesses var_1   errores var_1 |
      | errores var_2   guesses var_2 |
"""

# Plot algorithm results from training set
from matplotlib.colors import ListedColormap
x_set, y_set = x_train, y_train
x1, x2 = np.meshgrid(np.arange(start = x_set[:,0].min() - 1, stop = x_set[:,0].max() + 1, step = 0.01),
                     np.arange(start = x_set[:,1].min() - 1, stop = x_set[:,1].max() + 1, step = 0.01))
plt.contourf(x1, x2, classifier.predict(np.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(x1.min(), x1.max())
plt.ylim(x2.min(), x2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1],
                c = ListedColormap(('darkred', 'darkgreen'))(i), label = j)
plt.title('SVM (Training Set)')
plt.xlabel('x_variable')
plt.ylabel('y_predictable_variable')
plt.legend()
plt.show()

from matplotlib.colors import ListedColormap
x_set, y_set = x_test, y_test
x1, x2 = np.meshgrid(np.arange(start = x_set[:,0].min() - 1, stop = x_set[:,0].max() + 1, step = 0.01),
                     np.arange(start = x_set[:,1].min() - 1, stop = x_set[:,1].max() + 1, step = 0.01))
plt.contourf(x1, x2, classifier.predict(np.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(x1.min(), x1.max())
plt.ylim(x2.min(), x2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1],
                c = ListedColormap(('darkred', 'darkgreen'))(i), label = j)
plt.title('SVM (Testing Set)')
plt.xlabel('x_variable')
plt.ylabel('y_predictable_variable')
plt.legend()
plt.show()
