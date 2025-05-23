import numpy as np



def medal_tally(df):
    medal_tally = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    medal_tally = medal_tally.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold',
                                                                                             ascending=False).reset_index()
    medal_tally['Total'] = medal_tally['Gold'] + medal_tally['Silver'] + medal_tally['Bronze']
    return medal_tally

def country_year_list(df):
    Years = df['Year'].unique().tolist()
    Years.sort()
    Years.insert(0, 'OverAll')

    country = df['region'].unique().tolist()
    country = np.unique(df['region'].dropna().values).tolist()
    country.sort()
    country.insert(0, 'OverAll')

    return Years, country

def fetch_medal_tally(df,year,country):
  medal_df = df.drop_duplicates(subset=['Team','NOC','Games','Year','City','Sport','Event','Medal'])
  flag = 0
  if year == 'OverAll' and country == 'OverAll':
    temp_df = medal_df
  if year == 'OverAll' and country != 'OverAll':
    flag = 1
    temp_df = medal_df[medal_df['region'] == country]
  if year != 'OverAll' and country == 'OverAll':
    temp_df = medal_df[medal_df['Year'] == int(year)]
  if year != 'OverAll' and country != 'OverAll':
    temp_df = medal_df[(medal_df['Year']==int(year)) & (medal_df['region']==country)]

  if flag == 1:
    x = temp_df.groupby('Year').sum()[['Gold','Silver','Bronze']].sort_values('Year').reset_index()
  else:
    x = temp_df.groupby('region').sum()[['Gold','Silver','Bronze']].sort_values('Gold',ascending=False).reset_index()
  x['Total'] = x['Gold'] + x['Silver'] + x['Bronze']

  return x

def data_over_time(df,col):
    nation_over_time = df.drop_duplicates(['Year', col])['Year'].value_counts().reset_index().sort_values('Year')
    nation_over_time.rename(columns={'Year': 'Edition', 'count': col}, inplace=True)
    return nation_over_time

def most_successful(df, sport):
  temp_df = df.dropna(subset=['Medal'])

  if sport != 'Overall':
    temp_df = temp_df[temp_df['Sport'] == sport]

  x = temp_df['Name'].value_counts().reset_index().head(12).merge(df,left_on='Name',right_on='Name',how='left')[['Name','count','Sport','region']].drop_duplicates('Name')
  x.rename(columns={'count':'Medals'},inplace=True)
  return x


def yearwise_medal_tally(df,country):
    temp_df = df.dropna(subset=['Medal'])
    temp_df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'], inplace=True)
    new_df = temp_df[temp_df['region'] == country]
    final_df = new_df.groupby(['Year']).count()['Medal'].reset_index()

    return final_df

def country_event_heatmap(df,country):
    temp_df = df.dropna(subset=['Medal'])
    temp_df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'], inplace=True)
    new_df = temp_df[temp_df['region'] == country]

    pt = new_df.pivot_table(index='Sport', columns='Year', values='Medal', aggfunc='count').fillna(0)
    return pt

def most_successful_countrywise(df,country):
  temp_df = df.dropna(subset=['Medal'])
  temp_df = temp_df[temp_df['region']==country]

  x = temp_df['Name'].value_counts().reset_index().head(10).merge(df,left_on='Name',right_on='Name',how='left')[['Name','count','Sport']].drop_duplicates('Name')
  x.rename(columns={'count':'Medals'},inplace=True)

  return x

def weight_v_height(df,sport):
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])
    athlete_df['Medal'].fillna('No Medal', inplace=True)
    if sport != 'Overall':
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        return temp_df
    else:
        return athlete_df

def men_vs_women(df):
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])

    men = athlete_df[athlete_df['Sex'] == 'M'].groupby('Year').count()['Name'].reset_index()
    women = athlete_df[athlete_df['Sex'] == 'F'].groupby('Year').count()['Name'].reset_index()

    final = men.merge(women, on='Year', how='left')
    final.rename(columns={'Name_x': 'Male', 'Name_y': 'Female'}, inplace=True)

    return final


