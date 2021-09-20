import numpy as np
import pandas as pd
from janitor import clean_names

df = pd.read_csv('world-happiness-report-2019.csv')
df = df.clean_names()
df['first_five_Letter'] = df['country_region_'].str.extract(r'(^w{5})')
print(df.head())
#df['first_five_Letter']=df['Country (region)'].str.extract(r'(^w{5})')
