import prepare

import pandas as pd
import numpy as np
import wrangle
import matplotlib.pyplot as plt
from math import sqrt

# modeling methods
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression, LassoLars, TweedieRegressor
from sklearn.preprocessing import PolynomialFeatures

import warnings
warnings.filterwarnings("ignore")

def feature_select():
    '''
    This function returns X DataFrame with model features and y DataFrame with targets for 
    train, validate, and test data.
    '''
    
    # pulling in prepared dfs
    train, validate, test = prepare.prepare_data()
    
    # splitting into X_train and y for each
    X_train = train[['baths', 'beds', 'sqft']]
    y_train = train[['tax_value']]

    X_validate = validate[['baths', 'beds', 'sqft']]
    y_validate = validate[['tax_value']]

    X_test = test[['baths', 'beds', 'sqft']]
    y_test = test[['tax_value']]
    
    return X_train, y_train, X_validate, y_validate, X_test, y_test

X_train, y_train, X_validate, y_validate, X_test, y_test = feature_select()

def visualize_target():
    '''
    This function returns a histogram of the target variable from the train data.
    '''
    
    plt.hist(y_train)
    plt.title('Distribution of Tax Values')
    plt.show()


#def baseline_pred():
#    '''
#    This function calculates the baseline prediction using the median tax value, appends the train
#    and validate df's with that baseline prediction, and then calculates the rmse of the baseline 
#    predictions against the actual y_train values.
#    '''
#    # finds the median tax value
#    baseline_pred = y_train.median()
#    
#    # adding the median tax value to the y train and validate df
#    y_train['baseline_pred'] = baseline_pred
#    y_validate['baseline_pred'] = baseline_pred
#    
#    # Baseline RMSE for train and validate data
#    baseline_rmse_train = sqrt(mean_squared_error(y_train.tax_value, y_train.baseline_pred))
#    baseline_rmse_validate = sqrt(mean_squared_error(y_validate.tax_value, y_validate.baseline_pred))
#    
#    return baseline_rmse_train, baseline_rmse_validate

def model1_pred():
    '''
    This function fits the train and validate data to Model 1 | Linear Regression OLS Model
    and then calculates the RMSE for each. 
    '''
    
    # create the model object
    lm = LinearRegression(normalize=True)
    
    # fit the model to our training data. We must specify the column in y_train, because y_train is a df
    lm.fit(X_train, y_train['tax_value'])
    
    # predict train and validate
    y_train['model1_pred'] = lm.predict(X_train)
    y_validate['model1_pred'] = lm.predict(X_validate)
    
    # Model 1 RMSE for train and validate
    model1_rsme_train = sqrt(mean_squared_error(y_train.tax_value, y_train.model1_pred))
    model1_rsme_validate = sqrt(mean_squared_error(y_validate.tax_value, y_validate.model1_pred))
    
    return model1_rsme_train, model1_rsme_validate

def model2_pred():
    '''
    This function fits the train to Model 2 | LassoLars, makes predictions on the train 
    and validate data, and then calculates the RMSE for each. 
    '''
    
    # create the model object
    lars = LassoLars(alpha=1.0)

    # fit the model to our training data
    lars.fit(X_train, y_train.tax_value)

    # predict train and validate
    y_train['model2_pred'] = lars.predict(X_train)
    y_validate['model2_pred'] = lars.predict(X_validate)

    # calculate model 2 rsme for train and validate
    model2_rsme_train = sqrt(mean_squared_error(y_train.tax_value, y_train.model2_pred))
    model2_rsme_validate = sqrt(mean_squared_error(y_validate.tax_value, y_validate.model2_pred))
    
    return model2_rsme_train, model2_rsme_validate

def model3_pred():
    '''
    This function fits the train data to Model 3 | TweedieRegressor (GLM), makes predictions on the
    train and validate data, and then calculates the RMSE for each. 
    '''
    
    # create the model object
    glm = TweedieRegressor(power=1, alpha=0)

    # fit the model to our training data
    glm.fit(X_train, y_train.tax_value)

    # predict train and validate
    y_train['model3_pred'] = glm.predict(X_train)
    y_validate['model3_pred'] = glm.predict(X_validate)

    # calculate model 2 rsme for train and validate
    model3_rsme_train = sqrt(mean_squared_error(y_train.tax_value, y_train.model3_pred))
    model3_rsme_validate = sqrt(mean_squared_error(y_validate.tax_value, y_validate.model3_pred))

    return model3_rsme_train, model3_rsme_validate

def test():
    '''
    This function uses the top performing model ---> Model 2 | Lasso Lars
    to make predictions on the target using the fresh train data.
    '''
  
    # predict test
    y_test['model2_pred'] = lars.predict(X_test)


    # calculate model 2 rsme for test
    model2_rsme_test = sqrt(mean_squared_error(y_test.tax_value, y_test.model2_pred))
    
    return model2_rsme_test

    
def metrics():
    
    baseline_rmse_train, baseline_rmse_validate = baseline_pred()
    print(f'Baseline RMSE | Train = {round(model.baseline_rmse_train)}')
#    print(f'Model 1 RMSE | Train = {round(model1_rsme_train)}')
#    print(f'Model 2 RMSE | Train = {round(model.model2_rsme_train)}')
#    print(f'Model 3 RMSE | Train = {round(model.model3_rsme_train)}')
#    print()
#    print(f'Baseline RMSE | Validate = {round(model.baseline_rmse_validate)}')
#    print(f'Model 1 RMSE | Validate = {round(model.model1_rsme_validate)}')
#    print(f'Model 2 RMSE | Validate = {round(model.model2_rsme_validate)}')
#    print(f'Model 3 RMSE | Validate = {round(model.model3_rsme_validate)}')
    
    
    
    
    
    
    
    
    
    
    
    
    