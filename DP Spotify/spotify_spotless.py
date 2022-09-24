import pandas as pd

df = pd.read_csv('Spotify Data Unclean.csv')

df['min_sec_played'] = df['ms_played'] / 60000

df['Year'] = pd.to_numeric(df['ts'].str.slice(0, 4))

df['sum_artist_mins_played'] = df.groupby('Artist Name')['min_sec_played'].transform('sum')
df['Overall Rank'] = df['sum_artist_mins_played'].rank(method='dense', ascending=False).astype('int64')

df = df.groupby(['Overall Rank', 'Artist Name', 'Year'])['min_sec_played'].sum().reset_index()
df['Year Rank'] = df.groupby('Year')['min_sec_played'].rank(method='dense', ascending=False)

df = df[df['Overall Rank'] < 101]

df = df.pivot(['Overall Rank', 'Artist Name'], 'Year', 'Year Rank')

df.to_csv('Output.csv')
