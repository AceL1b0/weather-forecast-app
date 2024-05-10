import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for Next Days")
place = st.text_input("Place")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select the data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days for {place}")


if place:
    try:
        filtered_content = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict['main']['temp'] for dict in filtered_content]
            dates = [dict["dt_txt"] for dict in filtered_content]
            figure = px.line(x=dates, y=temperatures,
                             labels={"x": "Dates", "y": "Temperature in (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict['weather'][0]['main']
                                for dict in filtered_content]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=115)

    except Exception:
        st.subheader("You entered a non-existing place")