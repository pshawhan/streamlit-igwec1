#-- Peter's first streamlit attempt, with thanks to Jonah for example
import streamlit as st
import pandas as pd

evts1=pd.read_csv("data/GWTC-1.csv")
evts2=pd.read_csv("data/GWTC-2.csv")
evts21=pd.read_csv("data/GWTC-2.1.csv")
evts21m=pd.read_csv("data/GWTC-2.1-marginal.csv")
evts3=pd.read_csv("data/GWTC-3.csv")
evts3m=pd.read_csv("data/GWTC-3-marginal.csv")

#-- Work with lists of names
n1 = evts1['Name'].tolist()
n2 = evts2['Name'].tolist()
n21 = evts21['Name'].tolist()
n21m = evts21m['Name'].tolist()
n3 = evts3['Name'].tolist()
n3m = evts3m['Name'].tolist()

#-- Store runs for each
run = dict()
gwtc1 = dict()
gwtc2 = dict()
gwtc21 = dict()
gwtc3 = dict()

#-- O1+O2 events, reported in the GWTC-1 paper
for n in n1:
    run[n] = 'O2'
    gwtc1[n] = 'new'
    gwtc2[n] = 'y'
    gwtc21[n] = 'y'
    gwtc3[n] = 'y'
#-- Correct the run name for the first three events
run['GW150914'] = 'O1'
run['GW151012'] = 'O1'
run['GW151226'] = 'O1'

for n in n2:
    run[n] = 'O3a'
    gwtc1[n] = ''
    gwtc2[n] = 'new'
    gwtc21[n] = ''
    gwtc3[n] = ''
for n in n21:
    run[n] = 'O3a'
    gwtc1[n] = ''
    if n not in gwtc2:
        gwtc2[n] = ''
    gwtc21[n] = 'new'
    gwtc3[n] = 'y'
for n in n21m:
    run[n] = 'O3a'
    gwtc1[n] = ''
    if n not in gwtc2:
        gwtc2[n] = ''
    gwtc21[n] = 'marginal'
    gwtc3[n] = 'm'
for n in n3:
    run[n] = 'O3b'
    gwtc1[n] = ''
    gwtc2[n] = ''
    gwtc21[n] = ''
    gwtc3[n] = 'new'
for n in n3m:
    run[n] = 'O3b'
    gwtc1[n] = ''
    gwtc2[n] = ''
    gwtc21[n] = ''
    gwtc3[n] = 'marginal'

#-- Build a DataFrame from all of those
ns = sorted(run.keys())
df = pd.DataFrame( { 'Name':ns, 'Run':[run[n] for n in names],
    'GWTC-1':[gwtc1[n] for n in names], 'GWTC-2':[gwtc2[n] for n in names],
    'GWTC-2.1':[gwtc21[n] for n in names], 'GWTC-3':[gwtc3[n] for n in names] } )

#-- The "astype(str)" here is to work around a bug introduced in streamlit 0.85
#-- See https://stackoverflow.com/questions/69578431/how-to-fix-streamlitapiexception-expected-bytes-got-a-int-object-conver
df2 = df.astype(str)

st.write('## GWTC correspondence table')
st.write("Total {} candidates".format(len(df2)))
st.write("Shape: {}".format(df2.shape))
st.write("Data types: {}".format(df2.dtypes))
st.dataframe(df2)
