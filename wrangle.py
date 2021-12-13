
import os
from env import host, user, password

import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split

## IMPORTS              #######################################################################
import pandas as pd
import numpy as np

from env import user, password, host

import os

## GLOBAL VARIABLES     #######################################################################

#database to use to pull the data from SQL server
db = 'zillow'

#url string with connection credentials used to access Zillow database from SQL server 
url = f'mysql+pymysql://{user}:{password}@{host}/{db}'

#SQL query that returns selected data from server
query = '''
SELECT bathroomcnt,
        bedroomcnt,
        calculatedfinishedsquarefeet,
        fips,
        yearbuilt,
        taxvaluedollarcnt
FROM properties_2017
JOIN predictions_2017 USING(parcelid)
WHERE propertylandusetypeid = 261;
'''

#name of the .csv file with project data
file_name = 'zillow.csv'


## ACQUIRE FUNCTION     #######################################################################

def acquire_data():
    '''
    This function checks for the .csv file with the raw project data and, if the file exists
    locally, writes its contents to a pandas df.
    
    If the raw project data file does not exist locally, the query and url variables, which are defined 
    globally in the acquire.py file, are used to access the SQL and the queried data is written to a 
    pandas df.
    
    This function returns a df of the raw queried data. 
    '''

    # if csv file with project data already exists locally, read it into a pandas df
    if os.path.isfile(file_name):
        return pd.read_csv(file_name)
    
    # if project data csv file does not exist locally, connect to SQL db and save query as df
    else:
        return pd.read_sql(query, url)
    
    
    
    ## PREPARE FUNCTION     #######################################################################

def clean_data():
    
    # function from acquire module, that reads sql query (or local .csv file) to DataFrame
    df = acquire_data()
    
    # change column names
    df.rename(columns = {'bathroomcnt': 'baths', 
                              'bedroomcnt': 'beds', 
                              'calculatedfinishedsquarefeet': 'sqft',
                              'taxvaluedollarcnt':'tax_value'}, inplace = True)
    
    # drop null rows
    df = df.dropna()
    
    # drop rows with zero count for 'beds' or 'baths'
    df = df.drop(df[(df.beds == 0) | (df.baths == 0)].index)
    
    #change dtype of fips from float to object
    df.fips = df['fips'].astype(int).astype(object)
    
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
        

def assign_county(row):
    '''
THIS FUNCTION TAKES IN A ROW FROM DF AND CREATES A NEW COLUMN
WITH THE TEXT OF THE CORRESPONDING COUNTY TO THE FIPS CODE.
    '''
    if row['fips'] == 6037:
        return 'Los Angeles'
    if row['fips'] == 6059:
        return 'Orange'
    if row['fips'] == 6111:
        return 'Ventura'
    
def encode_fips(df):
    '''
THIS FUNCTION TAKES IN THE DF AND ENCODES THE FIPS COLUMN FOR 
EACH OF THE THREE COUNTIES AND THEN DROPS THE OBJECT COUNTY COLUMN
    '''
    df['county'] = df.apply(lambda row: assign_county(row), axis = 1)
    
    dummy_df = pd.get_dummies(df[['county']], drop_first = False)
    
    df = pd.concat([df, dummy_df], axis = 1)
    
    
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
    # df of raw data acquired from acquire function
    raw_data = acquire_data()
    
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
    df = encode_data()
    
    # create test df
    train_validate, test = train_test_split(df, test_size = .2, random_state = 123)
    
    #split remaining data into train and validate
    train, validate = train_test_split(train_validate, test_size = .3, random_state = 123)
    
    return train, validate, test
       
    
def feature_select(train, validate, test):
    '''
    
    '''
    train, validate, test = prepare_data()
    
    #prepare data for modeling
    X_train = train[['baths', 'beds', 'sqft', 'county_Los Angeles', 'county_Orange', 'county_Ventura']]
    y_train = train[['tax_value']]

    X_validate = validate[['baths', 'beds', 'sqft', 'county_Los Angeles', 'county_Orange', 'county_Ventura']]
    y_validate = validate[['tax_value']]

    X_test = test[['baths', 'beds', 'sqft', 'county_Los Angeles', 'county_Orange', 'county_Ventura']]
    y_test = test[['tax_value']]
    
    return X_train, y_train, X_validate, y_validate, X_test, y_test
    
    
    