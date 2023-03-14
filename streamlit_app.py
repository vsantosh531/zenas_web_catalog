import streamlit
import snowflake.connector
streamlit.title('My test title')
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
