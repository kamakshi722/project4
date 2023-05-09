#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


df=pd.read_csv("C:/Users/kamak/Downloads\deliveries.csv")
df


# In[12]:


filt=df['batsman']=='DA Warner'
df_warner=df[filt]
df_warner


# In[13]:


df_warner['dismissal_kind'].value_counts()


# In[14]:


df_warner['dismissal_kind'].value_counts().plot.pie()


# In[15]:


def count(df,runs):
    return len(df_warner[df_warner['batsman_runs']==runs])*runs


# In[16]:


count(df_warner,1)


# In[21]:


count(df_warner,2)


# In[22]:


count(df_warner,3)


# In[23]:


count(df_warner,4)


# In[24]:


count(df_warner,6)


# In[26]:


slices=[997,414,39,1604,960]
labels=[1,2,3,4,6]
explode=[0,0,0,0.1,0]
plt.pie(slices,labels=labels,explode=explode,autopct='%1.1f%%')


# In[27]:


# DISTRIBUTION OF TEAMS BY INNINGS


# In[28]:


df['bowling_team'].unique()


# In[29]:


Teams ={'Royal Challengers Bangalore': 'RCB', 'Sunrisers Hyderabad':'SH',
       'Rising Pune Supergiant':'RPS', 'Mumbai Indians':'MI',
       'Kolkata Knight Riders':'KKR', 'Gujarat Lions':'GL', 'Kings XI Punjab':'KXP',
       'Delhi Daredevils':'DD', 'Chennai Super Kings':'CSK', 'Rajasthan Royals':'RR',
       'Deccan Chargers':'DC', 'Kochi Tuskers Kerala':'KTK', 'Pune Warriors':'PW',
       'Rising Pune Supergiants':'RPS'}


# In[30]:


df['batting_team']=df['batting_team'].map(Teams)
df['bowling_team']=df['bowling_team'].map(Teams)


# In[31]:


df.head()


# In[33]:


df.columns


# In[34]:


runs=df.groupby(['match_id','inning','batting_team'])['total_runs'].sum().reset_index()


# In[36]:


runs.drop('match_id',axis=1,inplace=True)


# In[37]:


inning1=runs[runs['inning']==1]


# In[38]:


inning2=runs[runs['inning']==2]


# In[31]:


import plotly.express as px


# In[44]:


fig=px.bar(data_frame=inning1,x='batting_team',y='total_runs')


# In[45]:


fig.show()


# In[48]:


sns.boxplot(data=inning1,x='batting_team',y='total_runs')


# In[46]:


fig=px.bar(data_frame=inning2,x='batting_team',y='total_runs')


# In[47]:


fig.show()


# In[49]:


sns.boxplot(data=inning2,x='batting_team',y='total_runs')


# In[51]:


high_score=df.groupby(['match_id','inning','batting_team'])['total_runs'].sum().reset_index()


# In[52]:


high_score


# In[53]:


score_200=high_score[high_score['total_runs']>=200]


# In[54]:


score_200


# In[55]:


sns.countplot(score_200['batting_team'])


# In[5]:


balls_played=df.groupby('batsman')['ball'].count().reset_index()
runs=df.groupby('batsman')['batsman_runs'].sum().reset_index()
four=df[df['batsman_runs']==4]
runs_4=four.groupby('batsman')['batsman_runs'].count().reset_index()
six=df[df['batsman_runs']==6]
runs_6=six.groupby('batsman')['batsman_runs'].count().reset_index()


# In[6]:


runs_4.columns=['batsman','4s']
runs_4


# In[7]:


runs_6.columns=['batsman','6s']
runs_6


# In[8]:


player=pd.concat([runs,balls_played.iloc[:,1],runs_4.iloc[:,1],runs_6.iloc[:,1]],axis=1)


# In[9]:


player


# In[10]:


player.fillna(0,inplace=True)


# In[11]:


player


# In[12]:


player['strike_rate']=(player['batsman_runs']/player['ball'])*100


# In[13]:


player


# In[19]:


max_strike_rate=player[['batsman','strike_rate']]
max_strike_rate


# In[26]:


max_strike_rate.sort_values(by=['strike_rate'], ascending=False)[:10]


# In[30]:


top_players=max_strike_rate.sort_values(by=['strike_rate'], ascending=False)[:10]


# In[34]:


fig=px.bar(data_frame=top_players,x='batsman',y='strike_rate')


# In[35]:


fig.show()


# In[36]:


df.columns


# In[38]:


df2=pd.read_csv("C:/Users/kamak/Downloads/matches.csv")
df2


# In[40]:


df2.isnull().sum()


# In[41]:


df2.shape


# In[43]:


df2.drop(['umpire3'],axis=1,inplace=True)


# In[44]:


df2.shape


# In[45]:


df2.columns


# In[46]:


Teams ={'Royal Challengers Bangalore': 'RCB', 'Sunrisers Hyderabad':'SH',
       'Rising Pune Supergiant':'RPS', 'Mumbai Indians':'MI',
       'Kolkata Knight Riders':'KKR', 'Gujarat Lions':'GL', 'Kings XI Punjab':'KXP',
       'Delhi Daredevils':'DD', 'Chennai Super Kings':'CSK', 'Rajasthan Royals':'RR',
       'Deccan Chargers':'DC', 'Kochi Tuskers Kerala':'KTK', 'Pune Warriors':'PW',
       'Rising Pune Supergiants':'RPS'}


# In[47]:


df2['team1']=df2['team1'].map(Teams)
df2['team2']=df2['team2'].map(Teams)


# In[48]:


df2.head()


# In[50]:


df2.shape[0]


# In[51]:


len(df2['city'].unique())


# In[52]:


sns.countplot(x='season',hue='toss_decision',data=df2)


# In[54]:


toss=df2['toss_winner'].value_counts()
toss


# In[58]:


fig=px.bar(data_frame=toss)


# In[56]:


fig.show()


# In[59]:


teams=(df2['team1'].value_counts()+df2['team2'].value_counts()).reset_index()


# In[60]:


teams.columns=['team_name','matches_played']
teams


# In[61]:


df2['winner']=df2['winner'].map(Teams)


# In[64]:


wins=df2['winner'].value_counts().reset_index()
wins


# In[65]:


wins.columns=['team_name','total_win']


# In[66]:


wins


# In[72]:


team_record=teams.merge(wins,left_on='team_name',right_on='team_name',how='inner')


# In[73]:


team_record


# In[74]:


team_record['winning_rate']=(team_record['total_win']/team_record['matches_played'])*100


# In[75]:


team_record


# In[76]:


team_record.sort_values(by=['winning_rate'],ascending=False)


# In[77]:


get_ipython().system('pip install plotly')


# In[78]:


import plotly.offline as py
import plotly.graph_objs as go


# In[86]:


trace1=go.Bar(x=team_record['team_name'],y=team_record['matches_played'],name='matches_played')


# In[87]:


trace2=go.Bar(x=team_record['team_name'],y=team_record['total_win'],name='total_wins')


# In[88]:


data=[trace1,trace2]


# In[89]:


py.iplot(data)


# In[ ]:




