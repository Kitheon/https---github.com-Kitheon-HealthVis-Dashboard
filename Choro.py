import streamlit as st
import pandas as pd
import json
import plotly.express as px
from urllib.request import urlopen

def main():
    # Load US counties information
    with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
        counties = json.load(response)

    # Load West Virginia FIPS codes
    fipsDF = pd.read_csv('WV FIPS.csv')
    fips = fipsDF.loc[:, 'FIPS'].tolist()

    # Load drug poisoning mortality data
    DF = pd.read_csv("NCHS_-_Drug_Poisoning_Mortality_by_County__United_States.csv")

    # Filter data for West Virginia in 2021
    filteredDF = DF.loc[(DF["State"] == 'West Virginia') & (DF["Year"] == 2021)]
    filteredDF["Model-based Death Rate"] = filteredDF["Model-based Death Rate"].round()

    # # Set Streamlit page to wide layout for full screen
    # st.set_page_config(layout="wide")

    # title
    st.title(f"West Virginia Overdose Deaths per 100,000 (2021)")

    # Display loading spinner while the figure is being generated
    with st.spinner("Generating map..."):
        # Create choropleth map
        fig = px.choropleth_mapbox(filteredDF, 
                                geojson=counties, 
                                locations='FIPS', 
                                color="Model-based Death Rate",
                                color_continuous_scale=px.colors.sequential.Reds,
                                center = {"lat": 38.7214, "lon": -80.6530}, 
                                zoom = 5,
                                opacity=0.75,
                                hover_name = filteredDF['County'].tolist(),
                                labels={"Model-based Death Rate": "Overdose Deaths"},
                                mapbox_style="carto-positron",
                                custom_data=['County', "Model-based Death Rate"])

        # Update hover template
        fig.update_traces(hovertemplate='County: %{customdata[0]}<br><br>' + 
                                        "Overdose Deaths" + ': %{customdata[1]:.2f}')
        
        # Set the size of the plotly chart to be larger for fullscreen
        fig.update_layout(width=900, height=600)

        # Display the choropleth map
        st.plotly_chart(fig, theme="streamlit")
