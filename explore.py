import wrangle

import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

from scipy import stats

from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression, LassoLars, TweedieRegressor
from sklearn.preprocessing import PolynomialFeatures


def explore_data(df):
    '''
THIS FUNCTION WILL PLOT A SCATTERPLOT OF THE TAX_VALUE AND SQFT, BEDS AND BATHS, 
ALONG WITH A REGRESSION LINE. IT WILL PLOT 3 COLUMNS, SEPARATED BY FIPS COUNTY.
    '''
    
    sns.lmplot(data = df, y = 'tax_value', 
               x = 'sqft', 
               hue = 'county', 
               line_kws={'color': 'red'}, 
               col = 'county')
    
    
    sns.lmplot(data = df, y = 'tax_value', x = 'beds', hue = 'county', 
           line_kws={'color': 'red'}, col = 'county')
    
    sns.lmplot(data = df, y = 'tax_value', x = 'baths', hue = 'county', 
           line_kws={'color': 'red'}, col = 'county')
    
def test_data(df):
    '''
CORR TESTS 
    '''
    
    corr_sqft, p_sqft = stats.pearsonr(df.sqft, df.tax_value)
    
    corr_beds, p_beds = stats.pearsonr(df.beds, df.tax_value)
    
    corr_baths, p_baths = stats.pearsonr(df.baths, df.tax_value)
    
    return corr_sqft, corr_beds, corr_baths
    

#def model():
#    
#    X_train, y_train, X_validate, y_validate, X_test, y_test = wrangle.feature_select(train, validate, test)
#
#    # baseline
#    baseline = y_train.tax_value.median()
#    y_train['baseline_pred'] = baseline_pred
#    y_validate['baseline_pred'] = baseline_pred
#    baseline_rsme_train = sqrt(mean_squared_error(y_train.tax_value, y_train.baseline_pred))
#    
#    # model 1
#    lm = LinearRegression(normalize=True)
#    lm.fit(X_train, y_train['tax_value'])
#    y_train['model1_pred'] = lm.predict(X_train)
#    model1_rsme_train = sqrt(mean_squared_error(y_validate.tax_value, y_validate.model1_pred))
    
    
    
    
    
    
    

