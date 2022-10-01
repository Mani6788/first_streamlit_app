
import streamlit
import pandas
import  snowflake.connector
import requests
from urllib.error import URLError

my_fruit_list= pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)
fruits_selected=streamlit.multiselect ("pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)


#new section to display fruityvice response


fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text (fruityvice_response)


#new section to display fruityvice api response

#streamlit.text (fruityvice_response.json())

def get_fruityvice_data(this_fruit_choice):
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
   fruityvice_normalized= pandas.json_normalize(fruityvice_response.json())
   return fruityvice_normalized 
  
streamlit.header("Fruityvice Fruit Advice")

try:
  fruit_choice=streamlit.text_input('what fruit would you like inforamtion about?')
  if not fruit_choice:
    streamlit.error("please select  a fruit to get information")
  else:
    back_from_function=get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
    
    
streamlit.stop()    
except URLError as e:
  streamlit.write("error occured")
  streamlit.error()

  

my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur=my_cnx.cursor()
my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
my_data_rows=my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)



add_my_fruit=streamlit.text_input('what fruit would you like to add?' ,'jackfruit')

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + add_my_fruit)
streamlit.write("thanks for adding", add_my_fruit )
my_cur.execute("insert into fruit_load_list values  ('from streamlit')")

