import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.ensemble import RandomForestRegressor
import pickle

df = pd.read_csv("/Users/delaldeniztomruk/Desktop/ml-projects/bulldozer/bluebook-for-bulldozers/TrainAndValid.csv", 
                      low_memory=False, parse_dates=["saledate"])


df["SaleYear"] = df.saledate.dt.year
df["SaleMonth"] = df.saledate.dt.month
df["SaleDay"] = df.saledate.dt.day
df["DayOfWeek"] = df.saledate.dt.dayofweek
df["DayOfYear"] = df.saledate.dt.dayofyear
df.drop("saledate", axis = 1, inplace = True)
    
relevant_features = ["SalePrice", "SaleYear", "YearMade", "ProductSize", "Enclosure"]
cols_to_drop = set(df.columns) - set(relevant_features)

for i in cols_to_drop:
    df.drop(i, axis = 1, inplace = True)

df = df.reset_index(drop=True)


# categorical
for label, content in df.items():
    if not pd.api.types.is_numeric_dtype(content):
        df[label] = pd.Categorical(content).codes + 1   

# handling numerical missing values for df_train

missing_cat_train = []
for label, content in df.items():
    if pd.api.types.is_string_dtype(content):
        missing_cat_train.append(label)

missing_num_train = list(set(df.columns) - set(missing_cat_train))

for i in missing_num_train:
    df[i].fillna(df[i].mean(), inplace=True)

    
X, y = df.drop("SalePrice", axis=1), df.SalePrice


from sklearn.model_selection import RandomizedSearchCV

rf_grid = {"n_estimators": np.arange(10, 100, 10), 
          "max_depth": [None, 3, 5, 10],
          "min_samples_split": np.arange(2, 20, 2),
          "min_samples_leaf": np.arange(1, 20, 2),
           "max_features": [0.5, 1, "sqrt", "auto"],
           "max_samples": [1000]
          }


rs_model = RandomizedSearchCV(RandomForestRegressor(n_jobs = -1, random_state = 42), 
                                                    param_distributions = rf_grid, 
                                                    n_iter = 100,
                                                    verbose = True)

rs_model.fit(X, y)

pickle.dump(rs_model, open("rs_model.pkl", 'wb'))

loaded_model = pickle.load(open("rs_model.pkl", 'rb'))