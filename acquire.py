#  ACQUIRE              #######################################################################
#Use this module to acquire project data

## CONTENTS             #######################################################################
''' 
    I. IMPORTS
    
    II. GLOBAL VARIABLES
        - db
        - url
        - query
        - file_name
        
    III. acquire_data() function
    
    IV. VERIFY COUNT
'''


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
        regionidzip,
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

## VERIFY COUNT         #######################################################################

#row count of data acquired, will be used for notebook in a print statement to verify the number of observations
verify_count = f'After acquiring our data, we have {acquire_data().shape[0]} observations, ready to be prepapred.'



