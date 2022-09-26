
import streamlit
import pandas

my_fruits_list= pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruits_list)
streamlit.multiselect ("pick some fruits:", list(my_fruit_list.index))
stramlit.dataframe(my_fruit_list)
