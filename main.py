import streamlit as st
import pandas as pd
from streamlit_folium import folium_static
import folium
import streamlit_folium as sf
import altair as alt
from vega_datasets import data
import plotly.graph_objects as go
import geopandas as gpd
import numpy as np
from PIL import Image

# Set page configuration
st.set_page_config(
    page_title="Fiber Competitive Intensity",
    page_icon=":smiley:",
    layout="wide",
    initial_sidebar_state="auto",
)

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Fiber Competitive Intensity")

# Create sidebar menu
menu = ["Home", "About", "Contact Us"]
selection = st.sidebar.radio("Go to", menu)

# Add submenu to Home menu
if selection == "Home":
    Home_menu = ["Map", "Uptake Rate"]
    sub_selection = st.sidebar.radio("Select an option", Home_menu)

    # Add content to Map
    if sub_selection == "Map":
        st.title("Map")
        gdf = gpd.read_file('C:\\Users\\NODROTE VENTURES\\Desktop\\S3 Bucket\\final_data.geojson')

        # Filter the data based on a condition
        dun = st.sidebar.selectbox("Select a Dun", gdf['dun'].unique())
        filtered_gdf = gdf[gdf['dun'] == dun]
        
        # Select the desired columns
        columns_to_display = ['population', 'fiber_tests', 'uptake_rate', 'poverty_incidence']

        # Display the filtered results
        st.write("Result for the selected region")
        st.write(filtered_gdf[columns_to_display])
        
        # Create a Folium map object centered around the region
        m = folium.Map(location=[filtered_gdf.geometry.centroid.y.mean(), filtered_gdf.geometry.centroid.x.mean()], zoom_start=10)

        # Add the polygons to the map
        folium.GeoJson(filtered_gdf).add_to(m)

        # Render the map in Streamlit
        folium_static(m)



    # Add content to Uptake Rate
    elif sub_selection == "Uptake Rate":
        st.title("Uptake Rate")
        gdf = gpd.read_file('C:\\Users\\NODROTE VENTURES\\Desktop\\S3 Bucket\\final_data.geojson')

        # filter the data based on a condition
        fiber_tests = st.sidebar.selectbox("Select a Fiber Tests", gdf['fiber_tests'].unique())
        filtered_gdf = gdf[gdf['fiber_tests'] == fiber_tests]

        # filter the data based on a condition
        dun = st.sidebar.selectbox("Select a Dun", gdf['dun'].unique())
        if dun:
            filtered_gdf = filtered_gdf[filtered_gdf['dun'] == dun]

        # Drop the 'geometry' column
        filtered_gdf = filtered_gdf.drop('geometry', axis=1)

        # Display the filtered results
        chart = alt.Chart(filtered_gdf).mark_bar().encode(
            x=alt.X('dun', axis=alt.Axis(labelAngle=-45)),
            y='count()',
            color='poverty_incidence',
            column=alt.Column('uptake_rate', spacing=10),
        ).properties(
            width=200,
            height=300
        )
        st.altair_chart(chart, use_container_width=True)


        

# Add content to About menu
elif selection == "About":
    st.title("About")
    st.write("MEET THE TEAM")


    
    
    # Define the image paths and captions
    image_paths = [
        "C:\\Users\\NODROTE VENTURES\\Desktop\\S3 Bucket\\The_new_me-removebg-preview.png",
        "C:\\Users\\NODROTE VENTURES\\Desktop\\S3 Bucket\\Tebogo.jpeg"
    ]
    captions = [
        "John Chukwuebuka | Data Scientist",
        "Tebogo Mngoma | Data Scientist"
    ]

    # Resize the images
    resized_images = []
    for image_path in image_paths:
        image = Image.open(image_path)
        resized_image = image.resize((300, 300))
        resized_images.append(resized_image)

    # Display the images side by side
    col1, col2 = st.columns(2)
    with col1:
        st.image(resized_images[0], caption=captions[0])

    with col2:
        st.image(resized_images[1], caption=captions[1])


        # Define the image paths and captions
    image_paths = [
        "C:\\Users\\NODROTE VENTURES\\Desktop\\S3 Bucket\\Gracious.jpeg",
        "C:\\Users\\NODROTE VENTURES\\Desktop\\S3 Bucket\\Kabelo.jpg"
    ]
    captions = [
        "Gracious Ngetich | Data Enginneer",
        "Kabelo | Data Scientist"
    ]

    # Resize the images
    resized_images = []
    for image_path in image_paths:
        image = Image.open(image_path)
        resized_image = image.resize((300, 300))
        resized_images.append(resized_image)

    # Display the images side by side
    col3, col4 = st.columns(2)
    with col3:
        st.image(resized_images[0], caption=captions[0])

    with col4:
        st.image(resized_images[1], caption=captions[1])




# Add content to Contact Us menu
elif selection == "Contact Us":
    st.title("Contact Us")
    st.write("Please email us at contact@example.com.")
