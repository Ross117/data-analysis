import pandas as pd

xlsx = pd.ExcelFile('2022W24 Inputs.xlsx')

flights = pd.read_excel(xlsx, 'Non-stop flights')
cities = pd.read_excel(xlsx, 'World Cities')

flights['From'].loc[flights['From'].str.contains('–')] = flights['From'].str.split('–').str[0]
flights['From'].loc[flights['From'].str.contains('-')] = flights['From'].str.split('-').str[0]
flights['From'].loc[flights['From'].str.contains('/')] = flights['From'].str.split('/').str[0]
flights['To'].loc[flights['To'].str.contains('–')] = flights['To'].str.split('–').str[0]
flights['To'].loc[flights['To'].str.contains('-')] = flights['To'].str.split('-').str[0]
flights['To'].loc[flights['To'].str.contains('/')] = flights['To'].str.split('/').str[0]

flights['Route'] = flights['From'] + " - " + flights['To']

flights['Distance - km'] = pd.to_numeric(flights['Distance'].str.split(' ').str[0].str.replace(',', ''))
flights['Distance - mi'] = flights['Distance'].str.slice(flights['Distance'].str.find('(')[0], flights['Distance'].str.find('i')[0])
flights['Distance - mi'] = pd.to_numeric(flights['Distance - mi'].str.slice(1, flights['Distance - mi'].str.find(' ')[0]).str.replace(',', ''))
flights = flights.drop(columns=['Distance'])

flights['rank'] = flights['Distance - km'].rank(method='dense', ascending=False).astype('int64')

flights['First flight'] = pd.to_datetime(flights['First flight'])

flights = pd.merge(flights, cities, left_on='From', right_on='City', how='left')
flights = flights.drop(columns=['City'])
flights = flights.rename(columns={'Lat': 'Lat_from', 'Lng': 'Lng_from'})

flights = pd.merge(flights, cities, left_on='To', right_on='City', how='left')
flights = flights.drop(columns=['City'])
flights = flights.rename(columns={'Lat': 'Lat_to', 'Lng': 'Lng_to'})

flights.to_csv('Output.csv')
