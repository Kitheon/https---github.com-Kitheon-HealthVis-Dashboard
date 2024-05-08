import streamlit as st
import AbuseRecovery
import Choro
import FitBit
import LevelOfAbuse

def main():
    page = st.sidebar.selectbox("Select Visualization", 
                                ["Substance Abuse Recovery",
                                 "Stage of Addiction Questionaire",
                                 "Overdose Choropleth",
                                 "FitBit Sample"])
    if page == "Substance Abuse Recovery":
        AbuseRecovery.main()
    elif page == "Stage of Addiction Questionaire":
        LevelOfAbuse.main()
    elif page == "Overdose Choropleth":
        Choro.main()
    elif page == "FitBit Sample":
        FitBit.main()

if __name__ == "__main__":
    main()