import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype


def reduce_mem_usage(df):
    """ iterate through all the columns of a dataframe and modify the data type
        to reduce memory usage.
    """
    start_mem = df.memory_usage().sum() / 1024 ** 2
    print('Memory usage of dataframe is {:.2f} MB'.format(start_mem))

    for col in df.columns:
        col_type = df[col].dtype

        if col_type != object:
            
            if all(df[col] == df[col].astype(int)):
                df[col] = df[col].astype(int)
                col_type = df[col].dtype
                print(col, 'converted to int')
            
            c_min = df[col].min()
            c_max = df[col].max()   
            
            if str(col_type)[:3] == 'int':
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)
            else:
                if c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)
        else:
            df[col] = df[col].astype('category')

    end_mem = df.memory_usage().sum() / 1024 ** 2
    print('Memory usage after optimization is: {:.2f} MB'.format(end_mem))
    print('Decreased by {:.1f}%'.format(100 * (start_mem - end_mem) / start_mem))

    return df       
    
    
def add_features(data):
    data = data.copy()
    data['x1'] = data['gfs_temperature_sea_interpolated'] + data['cmc_0_0_0_2_interpolated'] 
    data['x2'] = (data['gfs_temperature_sea_interpolated'] + 0.5 +
                  data['cmc_0_0_0_2_interpolated'] - 272.15 +
                  data['wrf_t2'] - 272.15) / 3
    return data


def fill_nas(data):
    features = data.columns[6:]
    missing_columns = data[features].isna().sum()[data[features].isna().sum() > 0].index

    for feature in missing_columns:
        if is_numeric_dtype(data[feature]):
            fill_value = data[feature].min() - 1
        
            data[feature] = data[feature].fillna(fill_value)
        else:
            data[feature] = data[feature].fillna('None')
    return data

        
def process_data(data):
    data = add_features(data)
    data = fill_nas(data)
    return data
