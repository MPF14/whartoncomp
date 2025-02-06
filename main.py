import pandas as pd
import numpy as np

df = pd.read_csv('/Users/mf/eh/whartoncomp/data.csv', skipinitialspace=True, na_values='?')

df['win'] = (df['team_score'] > df['opponent_team_score']).astype(int)

sdv = df.groupby(['home_away_NS', 'win']).agg(lambda x: x.std() if x.dtype in ['int64', 'float64'] else None)
avg = df.groupby(['home_away_NS', 'win']).agg(lambda x: x.mean() if x.dtype in ['int64', 'float64'] else None)

print(sdv)
print(avg)

# sdv = pd.DataFrame(sdv)
# avg = pd.DataFrame(avg)
# sdvpath = 'sdv.csv'
# avgpath = 'avg.csv'
# sdv.to_csv(sdvpath, index=False)
# avg.to_csv(avgpath, index=False)
