# FUNCTION TO ACQUIRE RAW DATA 
'''
Use this module to acquire project data
    - Global variables:
        - sql_connect_str
        - url
        - query
        - db
    - Acquire function:
        - acquire_data(filename)
'''


## IMPORTS              #######################################################################
import pandas as pd
import numpy as np

from env import user, password, host

import os

## GLOBAL VARIABLES     #######################################################################

#database to use to pull the data
db = zillow

#string with sql db connection credentials
sql_connect_str = f'mysql+pymysql://{user}:{password}@{host}/db'

#url string to access Zillow database from SQL server
url = f'mysql+pymysql://{user}:{password}@{host}/zillow'

#sql query to pull data
query = '''
SELECT bathroomcnt,
        bedroomcnt,
        calculatedfinishedsquarefeet,
        fips,
        regionidzip,
        yearbuilt,
        taxvaluedollarcnt
FROM properties_2017
WHERE propertylandusetypeid = 261
'''

## ACQUIRE FUNCTION     #######################################################################

def acquire_data(filename):
    '''
    This function takes in as an argument the .csv file with the raw project data and, if the file exists
    locally, writes its contents to a pandas df.
    
    If the raw project data file does not exist locally, the query and url variables, which are defined 
    globally in the acquire.py file, are used to access the SQL db with the db credentials and SQL query 
    of the desired data.
    
    This function returns a df of the raw queried data. 
    '''

    # if csv file with project data already exists locally, read it into a pandas df
    if os.path.isfile(file_name):
        return pd.read_csv(file_name)
    
    # if project data csv file does not exist locally, connect to SQL db and save query as df
    else:
        return pd.read_sql(query, url)
