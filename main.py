import pandas as pd

df = pd.read_csv('data1.csv')
country_name = input('Enter the country name: ')
rowi = df[df['Country'] == country_name].index[0]

print('The Job Satisfaction for '+ country_name+' is ' +str(df.loc[rowi, 'JobSatisfaction']))