import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

if st.button("Test Code"):
  time_series = np.random.randn(100)
  st.pyplot(time_series)
  plt.title("Random 100-Unit Time Series")
  plt.xlabel("Time")
  plt.ylabel("Value")
  
