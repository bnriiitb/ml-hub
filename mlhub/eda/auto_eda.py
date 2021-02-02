from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import streamlit as st
import pandas as pd

# upload a dataset
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    # st.success('Successfully loaded the file {}'.format(uploaded_file.file_name))
    st.write(df.head())
    # run pandas profiler
    pr = ProfileReport(df, explorative=True)
    st.title("EDA Report")
    # st.write(df)
    st_profile_report(pr)
