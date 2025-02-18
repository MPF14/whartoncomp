import pandas as pd
import numpy as np

df = pd.read_csv('/Users/mf/eh/whartoncomp/data/data.csv', skipinitialspace=True, na_values='?')
df['win'] = (df['team_score'] > df['opponent_team_score']).astype(int)

#team averages raw 
tar = df.groupby(['team']).agg(lambda x: x.mean() if x.dtype in ['int64', 'float64'] else np.nan) 
#standard deviation wins 
sdw = df.groupby(['win']).agg(lambda x: x.std() if x.dtype in ['int64', 'float64'] else np.nan).drop([0])
#win avgerages 
wa = df.groupby(['win']).agg(lambda x: x.mean() if x.dtype in ['int64', 'float64'] else np.nan).drop([0])
#standard deviation percent 
sdp = (sdw/ wa * 2).replace([np.inf, -np.inf], np.nan)
#team averages weighted 
taw = tar.div(sdp.iloc[0]) 
taw['talent'] = taw.sum(axis=1)
taw = taw.sort_values(by='talent',ascending=False)
print(taw)

#tawpath = '/Users/mf/eh/whartoncomp/data/taw.csv'
#taw.to_csv(tawpath, index=True)
#sdv = df.groupby(['home_away_NS', 'win']).agg(lambda x: x.std() if x.dtype in ['int64', 'float64'] else np.nan)
#avg = df.groupby(['home_away_NS', 'win']).agg(lambda x: x.mean() if x.dtype in ['int64', 'float64'] else np.nan)
#tavg = df.groupby(['team','home_away_NS', 'win']).agg(lambda x: x.mean() if x.dtype in ['int64', 'float64'] else np.nan)
# sdvpath = 'data/sdv.csv'
# avgpath = 'data/avg.csv'
# tavgpath = 'data/tavg.csv'
# sdv.to_csv(sdvpath, index=False)
# avg.to_csv(avgpath, index=False) 
# tavg.to_csv(tavgpath, index=False)