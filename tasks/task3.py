import pandas as pd
import numpy as np


data = {
    'Embarked': ['C', 'S', 'Q', 'S', 'C', 'Q', 'S', 'C', 'Q', 'S'],
    'Fare':     [80, 30, 20, np.nan, 70, 15, 35, 90, 25, 50],
    'Age':      [22, 35, 30, 40, np.nan, 28, 32, 26, 18, np.nan]
}

df = pd.DataFrame(data)


filtered_df = df.dropna(subset=['Fare', 'Age'])


result = (
    filtered_df.groupby('Embarked')
    .agg(AvgFare=('Fare', lambda x: round(x.mean(), 2)),
         AvgAge=('Age', lambda x: round(x.mean(), 2)))
    .reset_index()
)


result = result.sort_values(by='AvgFare', ascending=False)

print(result)
