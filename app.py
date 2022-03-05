#-- Peter's first streamlit attempt, with thanks to Jonah for example
import streamlit as st
import pandas as pd

gwtc1=pd.read_csv("data/GWTC-1.csv")
gwtc2=pd.read_csv("data/GWTC-2.csv")
gwtc21=pd.read_csv("data/GWTC-2.1.csv")
gwtc21m=pd.read_csv("data/GWTC-2.1-marginal.csv")
gwtc3=pd.read_csv("data/GWTC-3.csv")
gwtc3m=pd.read_csv("data/GWTC-3-marginal.csv")

#gwtc = pd.concat([gwtc1,gwtc2,gwtc21,gwtc21m,gwtc3,gwtc3m])
gwtc = pd.concat([gwtc1,gwtc2,gwtc21,gwtc3m])
gwtc = gwtc.drop(columns=['pastro_cWB','pastro_GstLAL','pastro_MBTA','pastro_PyCBC','pastro_PyCBCBBH'])
df2 = gwtc.sort_values('Name')

st.write('## GWTC correspondence table')
st.write("Total {} candidates".format(len(df2)))
st.write("Shape: {}".df2.shape)
#st.dataframe(df2)
