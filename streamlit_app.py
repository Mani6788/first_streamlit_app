
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
streamlit.header("Fruityvice Fruit Advice")
#streamlit.text (fruityvice_response.json())

#fruityvice_normalized= pandas.json_normalize(fruityvice_response.json())
#streamlit.dataframe(fruityvice_normalized)


fruit_choice=streamlit.text_input('what fruit would you like inforamtion about?' ,'kiwi')
streamlit.write('The user entered', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

streamlit.stop()


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

