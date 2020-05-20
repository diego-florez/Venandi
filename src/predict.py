import pandas as pd
from sklearn.ensemble import RandomForestClassifier 
from src.gitapi import reqUser
from src.constants import labels_dict

#load final df
df = pd.read_csv("OUTPUT/final_df.csv")

#split X and y
X = df[["repos_number", "followers"]]
y = df.label

#fit the choosed model
rf_model = RandomForestClassifier().fit(X, y)

def predictUser(user):
    rf_pred = rf_model.predict(reqUser(user))
    for e in rf_pred:
        seniority = labels_dict[e]
        return seniority

