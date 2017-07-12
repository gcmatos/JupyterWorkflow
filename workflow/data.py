import os

from urllib.request import urlretrieve

import pandas as pd

URL ='https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_fremont_data(filename='Fremont.csv', url=URL,
                     force_download=False):
    '''
    Download and load dataset.
    
    Parameters
    ----------
    filname: string(optional)
    url: string(optional)
    force_download: bool(optional), if True force download
    
    Returns
    -------
    data: pandas.DataFrame
    
    '''
    if force_download or not os.path.exists(filename):
        urlretrieve(URL, 'Fremont.csv')
    
    data = pd.read_csv('Fremont.csv', 
                       index_col='Date', parse_dates=True)
    data.columns = ['West', 'East']
    data['Total'] = data['West'] + data['East']
    
    return data