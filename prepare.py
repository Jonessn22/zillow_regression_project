#  PREPARE              #######################################################################
#Use this module to prepare acquired data for exploration and modeling

## CONTENTS             #######################################################################
'''
    I. IMPORTS
    
    clean_data() FUNCTION
    
    GLOBAL VARIABLES
        - num_cols (numeric values)
        - cat_cols (categorical values)
        - out_cols (columns where outliers will be removed)
    
    visualize_data() FUNCTION
    
    prepare_data() FUNCTION
'''


## IMPORTS              #######################################################################

import acquire

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import sklearn.preprocessing
from sklearn.model_selection import train_test_split

## PREPARE FUNCTION     #######################################################################

def clean_data():
    
    # function from acquire module, that reads sql query (or local .csv file) to DataFrame
    df = acquire.acquire_data()
    
    # change column names
    df.rename(columns = {'bathroomcnt': 'baths', 
                              'bedroomcnt': 'beds', 
                              'calculatedfinishedsquarefeet': 'sqft',
                              'taxvaluedollarcnt':'tax_value'}, inplace = True)
    
    # drop null rows
    df = df.dropna()
    
    # drop rows with zero count for 'beds' or 'baths'
    df = df.drop(df[(df.beds == 0) | (df.baths == 0)].index)
    
    # var with list of columns that the outliers will be removed from
    out_cols = ['beds', 'baths', 'sqft', 'tax_value']
        
    # for loop that will remove outliers from specified columns
    for col in out_cols:
        
        # get quartiles
        q1, q3 = df[col].quantile([.25, .75])
        
        # calculate interquartile range IQR
        iqr = q3 - q1
        
        # get upper and lower bounds
        upper_bound = q3 + 1.5 * iqr
        lower_bound = q1 - 1.5 * iqr
        
        # using boolean mask to filter out columns that fall outside of upper and lower bounds 
        df = df[(df[col] > lower_bound) & (df[col] < upper_bound)]
    
    return df
    
    
## GLOBAL VARIABLES     ####################################################################### 

# list of all cleaned columns
all_columns = clean_data().columns.to_list()
all_columns = clean_data().columns.to_list()

# list of numerical columns
num_cols = ['sqft', 'tax_value', 'baths', 'beds', 'yearbuilt']

# list of categorical columns
cat_cols = ['fips']

# list of columns where outliers were removed
out_cols_raw = ['bathroomcnt', 'bedroomcnt', 'calculatedfinishedsquarefeet', 'taxvaluedollarcnt']
out_cols_clean = ['beds', 'baths', 'sqft', 'tax_value']


## VISUALIZE FUNCTION   #######################################################################
def visualize_data():
    '''
    This function will return two rows of boxplot visualizations of the distributions of columns where 
    outliers were removed. The top column will show the before distributions and, on the bottom,
    the visualizations will show the distributions after outliers were removed.
    '''
    # df of raw data acquired from .acquire module
    raw_data = acquire.acquire_data()
    
    # 1st column of boxplots, shows distributions of vars before outliers removed
    plt.figure(figsize = (18, 5))
    
    # for loop that cycles through list of columns where outliers will be removed (used acquired df names)
    for i, col in enumerate(out_cols_raw):

        # i starts at 0, but plot nos should start at 1
        plot_number = i + 1 

        # Create subplot.
        plt.subplot(1, len(out_cols_raw), plot_number)

        # Title with column name.
        plt.title(f'{col} with Outliers')

        # Display boxplot for column.
        sns.boxplot(data = raw_data, y = raw_data[col])

        # Hide gridlines.
        plt.grid(False)
    
    
    # 2nd column of boxplots, shows distributions of vars after outliers removed
    plt.figure(figsize = (18, 5))
    
    # for loop that cycles through list of columns where outliers will be removed  (uses cleaned df names)
    for i, col in enumerate(out_cols_clean):

        # i starts at 0, but plot nos should start at 1
        plot_number = i + 1 

        # Create subplot.
        plt.subplot(1, len(out_cols_clean), plot_number)

        # Title with column name.
        plt.title(f'{col} no outliers')

        # Display boxplot for column.
        sns.boxplot(data = clean_data(), y = clean_data()[col])
        sns.boxplot(data = clean_data(), y = clean_data()[col])

        # Hide gridlines.
        plt.grid(False)
    

    
## PREPARE FUNCTION   #######################################################################    
def prepare_data():
    '''
    This function splits our data in three, returning a train, validate, and test dataframe.
    '''
    # split
    # var holding df to split
    df = clean_data()
    
    # create test df
    train_validate, test = train_test_split(df, test_size = .2, random_state = 123)
    
    #split remaining data into train and validate
    train, validate = train_test_split(train_validate, test_size = .3, random_state = 123)
    
    return train, validate, test
    
    
    
#    #-------------------------------------------------------------------------------------------------
#    # scale
#    #listing columns to scale, all excepts fips
#    cols_to_scale = ['sqft']
#    
#    #create scaler object
#    scaler = sklearn.preprocessing.MinMaxScaler()
#    
#    #fit scaler object to train
#    scaler = scaler.fit(train[cols_to_scale])
#    
#    #transform data
#    scaled_train = scaler.transform(train[cols_to_scale])
#    scaled_train = pd.DataFrame(scaled_train, columns = ['scaled_sqft'])
#    train = pd.concat([train, scaled_train], axis = 1)
#
#    scaled_validate = scaler.transform(validate[cols_to_scale])
#    scaled_validate = pd.DataFrame(scaled_validate, columns = ['scaled_sqft'])
#    validate = pd.concat([validate, scaled_validate], axis = 1)
#
#    scaled_test = scaler.transform(test[cols_to_scale])
#    scaled_test = pd.DataFrame(scaled_test, columns = ['scaled_sqft'])
#    test = pd.concat([test, scaled_test], axis = 1)
#    
#    return train, validate, test

#-------------------------------------------------------------------------------------------------
# features for model
    

#X_train = train.drop(columns = ['tax_value'])
#y_train = train.tax_value
#    
#X_validate = validate.drop(columns = ['tax_value'])
#y_validate = validate.tax_value
#    
#X_test = test.drop(columns = ['tax_value'])
#y_test = test.tax_value
    
    
    
    
    


