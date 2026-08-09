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
session = requests.session()
alldata=[]
params= {
    'per_page':100,
    'page':1
}
pythotosql={
    'int':'INT',
    'float':'DECIMAL',
    'str':'TEXT',
    'bool':'BOOLEAN',
    'dict':'JSON',
    'list':'JSON',
    'NonType':'TEXT'

 

}


connection= psycopg2.connect(
    host=hostname,
    dbname=database,
    user=username,
    password=password,
    port=port

)

  
values = []
repoDict=None
while True:
    response = session.get('https://api.github.com/users/LaredjYacine/repos',params=params)
    data = response.json()
    for info in data :
        
        values.append((info['id'],info['name'],info['full_name'],info['private'],info['html_url']))
    if not data:
        break
    repoDict={
            'id':info['id'],
            'name':info['name'],
            'full_name':info['full_name'],
            'private':info['private'],
            'html_url': info['html_url']
        }
    alldata.extend(values)
    params['page']+=1


column=[]


for name, value in repoDict.items():
        datatype= pythotosql.get(type(value).__name__,'TEXT')
        if name == 'id':
             column.append(f'id {datatype} primary key not null')
             continue
        column.append(f'{name} {datatype}')

print(','.join(column))

create_query=f"create table if  not exists gitrepo({','.join(column)})"
cursor= connection.cursor()
cursor.execute(create_query)
connection.commit()

#cursor.execute(create_script)
for item in alldata:
    insert_script = f"insert into gitrepo(id,name,full_name,private,html_url) values {item} "
    cursor.execute(insert_script)
    
connection.commit()
connection.close()
