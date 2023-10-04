import streamlit as st
import pickle
import numpy as np

# import the model
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))
st.write('<div style="display: flex; justify-content: center;">', unsafe_allow_html=True)
st.title("LapTrends")
st.write('</div>', unsafe_allow_html=True)
# Create a two-column layout
col1, col2 = st.columns(2)

# Brand and Type of Laptop
with col1:
    company = st.selectbox('Brand',df['Company'].unique())
with col2:
    type = st.selectbox('Type',df['TypeName'].unique())

# RAM and Weight
col3, col4 = st.columns(2)
with col3:
    ram = st.selectbox('RAM (in GB)',[2,4,6,8,12,16,24,32,64])
with col4:
    weight = st.number_input('Weight of the Laptop')

# Touchscreen and IPS
col5, col6 = st.columns(2)
with col5:
    touchscreen = st.selectbox('Touchscreen',['No','Yes'])
with col6:
    ips = st.selectbox('IPS',['No','Yes'])

# Screen Size and Resolution
col7, col8 = st.columns(2)
with col7:
    screen_size = st.number_input('Screen Size')
with col8:
    resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

# CPU and HDD/SSD
col9, col10 = st.columns(2)
with col9:
    cpu = st.selectbox('CPU',df['Cpu Brand'].unique())
with col10:
    hdd = st.selectbox('HDD (in GB)',[0,128,256,512,1024,2048])

# SSD and GPU
col11, col12 = st.columns(2)
with col11:
    ssd = st.selectbox('SSD (in GB)',[0,8,128,256,512,1024])
with col12:
    gpu = st.selectbox('GPU',df['Gpu brand'].unique())

# Operating System
os = st.selectbox('OS',df['os'].unique())
if st.button('Predict Price'):
    # Query
    ppi = None
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size
    query = np.array([company,type,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])

    query = query.reshape(1,12)
    st.title("The predicted price of this configuration is " + str(int(np.exp(pipe.predict(query)[0]))))