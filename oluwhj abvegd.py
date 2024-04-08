import pandas as pd
df=pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv")
print(df)

y=df["logS"]
print(y)

x=df.drop("logS",axis=1)
print(x)

from sklearn.model_selection import train_test_split


X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2, random_state=100)
print(X_test)
print(X_train)  

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X_train,Y_train)

LinearRegression()

y_lr_train_pred = lr.predict(X_train)
y_lr_test_pred = lr.predict(X_test)
print(y_lr_train_pred)
print(y_lr_test_pred)

from sklearn.metrics import mean_squared_error, r2_score

lr_train_mse = mean_squared_error(Y_train, y_lr_train_pred)
lr_train_r2 = r2_score(Y_train, y_lr_train_pred)

lr_test_mse = mean_squared_error(Y_test, y_lr_test_pred)
lr_test_r2 = r2_score(Y_test, y_lr_test_pred)

print(lr_train_mse)
print(lr_train_r2)
print(lr_test_mse)
print(lr_test_r2)



from sklearn.ensemble import RandomForestRegressor

rf= RandomForestRegressor(max_depth=2, random_state=100)
rf.fit(X_train, Y_train)

y_rf_train_pred = rf.predict(X_train)
y_rf_test_pred = rf.predict(X_test)

from sklearn.metrics import mean_squared_error, r2_score

rf_train_mse = mean_squared_error(Y_train, y_rf_train_pred)
rf_train_r2 = r2_score(Y_train, y_rf_train_pred)

rf_test_mse = mean_squared_error(Y_test, y_rf_test_pred)
rf_test_r2 = r2_score(Y_test, y_rf_test_pred)
print("")
print(rf_train_mse)
print(rf_train_r2)
print(rf_test_mse)
print(rf_test_r2)