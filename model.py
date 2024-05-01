import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
import os
import pickle
import numpy as np

df=pd.read_csv("data.csv")
filename="model.sav"
# Cleaned Data
# Separating target and features

df=df.replace({'diagnosis':{'M':1, 'B':0}})
mean_values=[]

''' 
Used features
1- Radius Mean
2- Texture Mean
3- Perimeter Mean
4- Area Mean
 '''

features=df.loc[:, 'radius_mean':'area_mean']
target=df['diagnosis']

for col in features.columns:
    mean_values.append(float(features[col].mean()))
print(mean_values)

# splitting dataset
x_train, x_test, y_train, y_test=train_test_split(features, target, test_size=0.25, random_state=16)
def model_design():
    model=svm.SVC()

    model.fit(x_train, y_train)

    pred=model.predict(x_test)


    correct=0
    for i in range(y_test.shape[0]):
        if(int(y_test.iloc[i])==pred[i]):
            correct+=1
    print("Test Results--")
    print("Total examples: ", y_test.shape[0])
    print("Correct Predictions: ", correct)
    print("Accuracy: ", (correct*100)/y_test.shape[0])
    return model
class SVMBreastPredictor:
    def __init__(self):
        if not os.path.isfile("model.sav"):
            self.model=model_design()
            pickle.dump(self.model, open(filename, "wb"))
        else:
            train_choice=input("Want to train again(y/n)")
            if train_choice=='y':
                self.model = model_design()
                pickle.dump(self.model, open(filename, "wb"))
            else:
                self.model=pickle.load(open(filename, "rb"))
    def predict(self, rm=mean_values[0], tm=mean_values[1], pm=mean_values[2], am=mean_values[3]):
        return (self.model.predict(np.array([rm,tm,pm,am]).reshape(1,-1))[0])
