import streamlit as st
import ollama

st.title("NYC Crime Complaints 2006 - 2024")
st.subheader("Analysis by Michael Covelli")

with open('/Users/mike/nyc-crime-ai/narrative.md', 'r') as f:
    narrative = f.read()
st.write(narrative)
st.image("/Users/mike/nyc-crime-ai/crimes_per_year_plot.jpg")
st.image("/Users/mike/nyc-crime-ai/crimes_per_year_per_boro_plot.jpg")
st.image("/Users/mike/nyc-crime-ai/crimes_per_boro_bar.jpg")
st.image("/Users/mike/nyc-crime-ai/crime_time_of_day.jpg")
st.image("/Users/mike/nyc-crime-ai/f_susp_m_vic_bar.jpg")
st.image("/Users/mike/nyc-crime-ai/m_susp_f_vic.jpg")
st.image("/Users/mike/nyc-crime-ai/murder_rates_plot.jpg")
st.image("/Users/mike/nyc-crime-ai/offense_by_boro.jpg")
st.image("/Users/mike/nyc-crime-ai/report_delay.jpg")
st.image("/Users/mike/nyc-crime-ai/susp_age_group.jpg")
st.image("/Users/mike/nyc-crime-ai/susp_vic_race.jpg")
st.image("/Users/mike/nyc-crime-ai/susp_vic_sex.jpg")