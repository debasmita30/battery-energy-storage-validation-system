import streamlit as st
import pandas as pd
import plotly.express as px
from battery.simulator import BatterySimulator
import time

st.set_page_config(layout="wide")

battery = BatterySimulator()
battery.start()

st.title("Intelligent Battery Management Platform")

placeholder = st.empty()

while True:
    t = battery.get_telemetry()

    df = pd.DataFrame([t])

    with placeholder.container():
        c1,c2,c3,c4,c5 = st.columns(5)

        c1.metric("Voltage", round(t["voltage"],2))
        c2.metric("Current", round(t["current"],2))
        c3.metric("Temperature", round(t["temperature"],2))
        c4.metric("SOC", round(t["soc"],2))
        c5.metric("SOH", round(t["soh"],2))

        fig = px.line(df.T)

        st.plotly_chart(fig, use_container_width=True)

    time.sleep(2)