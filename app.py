import pandas as pd
import streamlit as st
#import plotly.express as px

from positions import generating_Positions

st.set_page_config(page_title='Shamili Website')
st.header('Shamili Trade Analysis')
st.subheader('Current Positions')



df=generating_Positions()
st.write(df)

st.button("click me")
