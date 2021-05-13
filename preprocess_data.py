def preprocess_data(df):
    df["SaleYear"] = df.saledate.dt.year
    df["SaleMonth"] = df.saledate.dt.month
    df["SaleDay"] = df.saledate.dt.day
    df["DayOfWeek"] = df.saledate.dt.dayofweek
    df["DayOfYear"] = df.saledate.dt.dayofyear
    df.drop("saledate", axis = 1, inplace = True)
    
    relevant_features = ["SalePrice", "MachineID", "SaleYear", "YearMade", "DayOfWeek"]
    cat_cols = list(set(df.columns) - set(df._get_numeric_data().columns))
    cols_to_drop = set(df.columns) - set(cat_cols + relevant_num)

    for i in cols_to_drop:
        df.drop(i, axis = 1, inplace = True)
        
    df = df.reset_index(drop=True)
    
    # categorical
    for label, content in df.items():
        if not pd.api.types.is_numeric_dtype(content):
            df[label] = pd.Categorical(content).codes + 1 
            
    missing_cat_train = []
    for label, content in df_train.items():
        if pd.api.types.is_string_dtype(content):
            missing_cat_train.append(label)
    
    # handling numerical missing values for df_train
    missing_num_train = list(set(df.columns) - set(missing_cat_train))
    for i in missing_num_train:
        df[i].fillna(df[i].mean(), inplace=True)
        
    return df
