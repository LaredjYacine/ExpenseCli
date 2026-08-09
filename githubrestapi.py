import requests
import dotenv
import psycopg2
import os 
import json 
dotenv.load_dotenv(override=True)
url = os.getenv('url')
port=os.getenv('port')
hostname=os.getenv('hostname')
username= os.getenv('username')
password =os.getenv('password')
database=os.getenv('database')

response = requests.get('https://api.github.com/users/LaredjYacine')
data = response.json()
first_name,last_name = data['name'].split()
connection= psycopg2.connect(
    host=hostname,
    dbname=database,
    user=username,
    password=password,
    port=port

)
connection.close()
print(first_name)

