from turtle import color, width
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff

from scipy import stats
from scipy.stats import norm #used for plotting
import statsmodels.api as sm

from tkinter import *
from tkinter import ttk

st.title("Welcome to my awesome data science app!")
#st.text('In this project I look into the predictors for WNV presence')

df= px.data.gapminder()

st.write(df)

year_options = df['year'].unique().tolist()
#year = st.selectbox('Which uear would you like to see?', year_options, 0)
#df = df[df['year']==year]


fig = px.scatter(df, x='gdpPercap', y='lifeExp',
            size="pop", color='continent', hover_name='country',
            log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90],
            animation_frame='year', animation_group='country')
fig.update_xaxes(gridcolor='#333333')
fig.update_yaxes(gridcolor='#333333')

fig.update_layout(width=800)
st.subheader("Life expectancy vs GDP scatter plot")
st.write(fig)



covid = pd.read_csv('https://raw.githubusercontent.com/shinokada/covid-19-stats/master/data/daily-new-confirmed-cases-of-covid-19-tests-per-case.csv')
covid.columns = ['Country', 'Country_code', 'Date', 'Confirmed', 'Days_since_confirmed']


covid['Date'] = pd.to_datetime(covid['Date']).dt.strftime('%Y-%m-%d')
country_options = covid['Country'].unique().tolist()

st.write(covid)

date_options = covid['Date'].unique().tolist()

#date = st.selectbox('Which date would you like to see', date_options, 100)
country = st.multiselect('Which country would you like to see?', country_options, ['Afghanistan'])

covid = covid[covid['Country'].isin(country)]
covid = covid[covid['Date'] > '2020-03-01']


fig2 = px.bar(covid, x='Country', y='Confirmed', color='Country', range_y=[0,35000],
            animation_frame='Date', animation_group='Country')

fig2.update_layout(width=800)

st.write(fig2)
















