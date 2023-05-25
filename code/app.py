import streamlit as st
from portrait import Portrait, categories


st.header('Data Portraits PyconDE & PyData Berlin 2023')
st.subheader('')
st.text('Answer que questions on the sidebar to generate your own individual data portrait.')

area = st.sidebar.selectbox('Which better describes your area of Python?', categories['areas'])
data_type = st.sidebar.selectbox('Which Python data type do you like the most?', categories['objects'])
pyladies = st.sidebar.selectbox('Are you a member of Pyladies', categories['pyladies'])
working = st.sidebar.selectbox('Do you prefer working', categories['workings'])
water = st.sidebar.selectbox('How do you like your water?', categories['waters'])
distance = st.sidebar.selectbox('How far are  you traveling to come to Berlin?', categories['distances'])
superpower = st.sidebar.selectbox('If you could choose one superpower:', categories['powers'])
game = st.sidebar.selectbox('If you had to play something, would you rather play:', categories['games'])


p = Portrait(image_path = 'Data_Portraits/images')
fig, ax = p.fig, p.ax
p.add_python_area(area)
p.add_favourite_object(data_type)
p.add_travel_distance(distance)
p.add_water_preference(water)
p.add_working_preference(working)
p.add_games(game)
p.add_pyladies(pyladies)
p.add_superpower(superpower)

st.pyplot(fig, use_container_width = True)

