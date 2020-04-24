import pandas as pd
import numpy as np

def clean_data(df):
    '''
    cleans in the input dataframe and returns dataframe with extra columns
    
    Parameters
    ----------
    df: pandas dataframe with the following columns:
    
    - `city`: city this user signed up in phone: primary device for this user
    - `signup_date`: date of account registration; 
        in the form `YYYYMMDD`
    - `last_trip_date`: the last time this user completed a trip; 
        in the form `YYYYMMDD`
    - `avg_dist`: the average distance (in miles) per trip taken 
        in the first 30 days after signup
    - `avg_rating_by_driver`: the rider’s average 
        rating over all of their trips 
    - `avg_rating_of_driver`: the rider’s average rating 
        of their drivers over all of their trips 
    - `surge_pct`: the percent of trips taken with surge multiplier > 1 
    - `avg_surge`: The average surge multiplier over all of this user’s trips 
    - `trips_in_first_30_days`: the number of trips this user took 
        in the first 30 days after signing up 
    - `luxury_car_user`: TRUE if the user took a luxury car in 
        their first 30 days; FALSE otherwise 
    - `weekday_pct`: the percent of the user’s trips occurring during a weekday
    
    Returns
    ---------
    df: pandas dataframe 
    with additional columns:
    - 'active': target. If 0, the user is considered 'churned', 1 if active
    - `avg_rating_by_driver_nan`: if the rider has been given 
        no ratings by their drivers. 1 if true
    - 'avg_rating_of_driver_nan': if the rider has given no 
        ratings to their drivers. 1 if true
        
    drops the following columns:
    - 'city': Cities were not of this world (Game of Thrones)
    '''

    # Load in data
    df = pd.read_csv('data/churn_train.csv')

    # Convert times (current in strings) to datetimes
    df['last_trip_date'] = pd.to_datetime(df['last_trip_date'])
    df['signup_date'] = pd.to_datetime(df['signup_date'])

    # A user is 'active' if they have taken a trip since June 1, 2014
    cutoff_date = '2014-06-01'
    cutoff_date = pd.to_datetime(cutoff_date)
    df['active'] = (df['last_trip_date'] >= cutoff_date).astype(int)

    # Make a column, avg_rating_of_driver_nan, where if the rider hasn't 
    # given out a rating, then its value is 1
    df['avg_rating_of_driver_nan'] = df['avg_rating_of_driver'].isnull().astype(int)

    # Make a column, avg_rating_by_driver_nan, where if the 
    # rider hasn't been given a rating, then its value is 1
    df['avg_rating_by_driver_nan'] = df['avg_rating_by_driver'].isnull().astype(int)

    return df