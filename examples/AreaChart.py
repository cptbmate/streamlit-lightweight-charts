import streamlit as st
from streamlit_lightweight_charts import renderLightweightCharts

chartOptions = {
    "layout": {
        "textColor": 'black',
        "background": {
            "type": 'solid',
            "color": 'white'
        }
    }
}

seriesAreaChart = [{
    "type": 'Area',
    "data": [
        { "time": '2018-12-22', "value": 32.51 },
        { "time": '2018-12-23', "value": 31.11 },
        { "time": '2018-12-24', "value": 27.02 },
        { "time": '2018-12-25', "value": 27.32 },
    ],
    "options": {}
}]

st.subheader("Area Chart sample")

renderLightweightCharts( [
    {
        "chart": chartOptions,
        "series": seriesAreaChart,
    }
], 'area')