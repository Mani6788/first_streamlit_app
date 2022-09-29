
import streamlit
import pandas

my_fruit_list= pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)
fruits_selected=streamlit.multiselect ("pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)


#new section to display fruityvice response

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text (fruityvice_response)


#new section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice")
streamlit.text (fruityvice_response.json())
