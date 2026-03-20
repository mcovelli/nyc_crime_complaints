import streamlit as st
import ollama
import os

st.title("NYC Crime Complaints 2006 - 2024")
st.subheader("Analysis by Michael Covelli")

base_path = os.path.dirname(__file__)
with open(os.path.join(base_path, 'narrative.md'), 'r') as f:
    narrative = f.read()
st.write(narrative)
st.image(os.path.join(base_path, 'charts','crimes_per_year_plot.jpg'))
st.image(os.path.join(base_path, 'charts','crimes_per_year_per_boro_plot.jpg'))
st.image(os.path.join(base_path, 'charts','crimes_per_boro_bar.jpg'))
st.image(os.path.join(base_path, 'charts','crime_time_of_day.jpg'))
st.image(os.path.join(base_path, 'charts','f_susp_m_vic_bar.jpg'))
st.image(os.path.join(base_path, 'charts','m_susp_f_vic.jpg'))
st.image(os.path.join(base_path, 'charts','murder_rates_plot.jpg'))
st.image(os.path.join(base_path, 'charts','offense_by_boro.jpg'))
st.image(os.path.join(base_path, 'charts','report_delay.jpg'))
st.image(os.path.join(base_path, 'charts','susp_age_group.jpg'))
st.image(os.path.join(base_path, 'charts','susp_vic_race.jpg'))
st.image(os.path.join(base_path, 'charts','susp_vic_sex.jpg'))
