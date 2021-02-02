from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import streamlit as st
import pandas as pd


def run_eda(df):
    pr = ProfileReport(df, explorative=True)
    st_profile_report(pr)


st.set_page_config(  # Alternate names: setup_page, page, layout
    layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
    initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
    page_title='ML-Hub',  # String or None. Strings get appended with "• Streamlit".
    page_icon=None,  # String, anything supported by st.image, or None.
)
st.sidebar.title('ML-Hub')
option = st.sidebar.selectbox(
    'Select a task',
    ['Exploratory Data Analysis',
     'Sentiment Analysis',
     'Zero-Shot Topic Classification',
     'Language Detection',
     'Named Entity Recognition',
     'Keyphrase Extraction',
     'Gender Prediction'])
# show the selected task
st.title("{}".format(option))
# upload a dataset
uploaded_file = st.file_uploader("Upload a dataset")
# st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
# col2 = st.radio(label='',options=('Comedy', 'Drama', 'Documentary'))
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success('Successfully loaded the file {}'.format(uploaded_file.name))
    st.subheader("Sample Data")
    st.write(df.head())
    df_dtypes = pd.DataFrame(df.dtypes).reset_index()
    df_dtypes.columns = ['column', 'dtype']
    st.subheader("Data Types")
    st.write(df_dtypes)
    left_column, right_column = st.beta_columns(2)
    # dtypes = ['boolean', 'integer', 'float', 'datetime64', 'string', 'category']
    # # dtype_option = st.selectbox('Select a dtype', dtypes)
    # buffer = io.StringIO()
    # df.info(buf=buffer)
    # s = buffer.getvalue()
    # with open("df_info.txt", "w",encoding="utf-8") as f:
    #     f.write(s)
    # st.write(f)
    pressed = left_column.button('Run {}'.format(option))
    if pressed:
        with st.spinner('Running the {} '.format(option)):
            # run pandas profiler
            run_eda(df)
