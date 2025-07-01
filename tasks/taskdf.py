import pandas as pd

data = {
    'Pclass': [1, 1, 1, 2, 2, 2, 3, 3, 3, 3],
    'Sex': ['male', 'female', 'male', 'female', 'male', 'male', 'female', 'female', 'male', 'male'],
    'Survived': [1, 1, 0, 1, 0, 0, 1, 0, 0, 0]
}

df = pd.DataFrame(data)

result = (
    df.groupby(['Pclass', 'Sex'])['Survived']
    .mean()
    .round(2)
    .reset_index()
    .rename(columns={'Survived': 'SurvivalRate'})
)

result = result.sort_values(by=['Pclass', 'SurvivalRate'], ascending=[True, False])
print(result)
