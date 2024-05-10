import requests
import streamlit as st

API_KEY = st.secrets["API_KEY"]

def get_data(place, forecast_days):
    url = (f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid="
           f"{API_KEY}&units=metric")
    response = requests.get(url)
    content = response.json()
    filtered_content = content['list']
    nr_values = 8 * forecast_days
    filtered_content = filtered_content[:nr_values]
    return filtered_content


if __name__=="__main__":
    print(get_data)
