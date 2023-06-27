import zipfile

import folium
import folium.plugins as plugins
import pandas as pd
import ujson as json
from streamlit_folium import folium_static

import streamlit as st

# read data
zf = zipfile.ZipFile('gh_td.zip') 
gh_td = pd.read_csv(zf.open("gh_td.csv"))


# Loading Json data
@st.cache_data()
def load_json():
    # Open the zip file in read mode
    with zipfile.ZipFile("td_data.zip", "r") as zip_file:

        # Read the JSON file as bytes
        json_data = zip_file.read("td_data.json")

        # Decode the bytes to string
        json_str = json_data.decode("utf-8")

        # Parse the JSON string
        return json.loads(json_str)


data=load_json()

#Title
st.title('Daily Traffic Density in Istanbul')

# Create a Folium map object
map = folium.Map(location=[gh_td['LATITUDE'].mean(), gh_td['LONGITUDE'].mean()], zoom_start=10)

# Add the HeatMapWithTime layer to the map
hm = plugins.HeatMapWithTime(data, 
                            auto_play=True,
                            index=list(gh_td['DATE_TIME'].unique()),
                            max_opacity=1.5, 
                            min_speed=9.5)
hm.add_to(map)

# Display the map using folium_static
folium_static(map, width=800, height=500)
