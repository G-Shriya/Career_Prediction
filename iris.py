from numpy import mean
from numpy import std
import pandas as pd
import pickle
import numpy as np
import sklearn

from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.ensemble import BaggingClassifier
df = pd.read_csv('career.csv')

import pandas as pd 
import numpy as np 
import sklearn

from sklearn.preprocessing import LabelEncoder 
from sklearn.metrics import accuracy_score 
df = pd.read_csv('career.csv') 
print(df.shape) 
col_names = df.columns

le = LabelEncoder()

for col in col_names:
    if col in col_names:
        i = df.columns.get_loc(col)
        df.iloc[:,i] = df.apply(lambda i:le.fit_transform(i.astype(str)), axis=0, result_type='expand')

X = np.array(df.iloc[:,0:-1]) 
y = np.array(df.iloc[:,-1:])

from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

from sklearn.tree import DecisionTreeClassifier 
sv = DecisionTreeClassifier(criterion="entropy").fit(X_train,y_train) 
predict=sv.predict(X_test) 
print(accuracy_score(y_test,predict))

pickle.dump(sv, open('iri.pkl', 'wb'))