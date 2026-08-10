import requests
import dotenv
import psycopg2
import os 
import json
import asyncio
import aiohttp  


dotenv.load_dotenv(override=True)
url = os.getenv('url')
port=os.getenv('port')
hostname=os.getenv('hostname')
username= os.getenv('username')
password =os.getenv('password')
database=os.getenv('database')
alldata=[]
gitoken= os.getenv('gittoken')

headers = {
    "Authorization": f'Bearer {gitoken}',
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2026-03-10",
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
calls = ['ApeXLgross','imshinyu','Serine404','0xHadyy','raideno','MedBelk','abderrahmenebe','BoyHMN']
def httpcalls(session):
    task=[]
    for call in calls :
            for i in range(1, 31):
                params = {"per_page": 100, "page": i}
                response = session.get(f'https://api.github.com/users/{call}/repos',params=params,headers=headers)
                task.append(response)
                

                
    return task 



async def fetchingData():
    data= []
    async with aiohttp.ClientSession() as session:
        task= httpcalls(session) 
        responses = await asyncio.gather(*task)
        for response in responses : 
            
            value = await response.json()             
            if value :
                data.extend(value)
        
    return data 

column=[]

data =asyncio.run(fetchingData())
for info in data :
    
    values.append((info['id'],info['name'],info['full_name'],info['private'],info['html_url']))

    repoDict={
            'id':info['id'],
            'name':info['name'],
            'full_name':info['full_name'],
            'private':info['private'],
            'html_url': info['html_url']
        }
    alldata.extend(values)




for name, value in repoDict.items():
        datatype= pythotosql.get(type(value).__name__,'TEXT')
        if name == 'id':
             column.append(f'id {datatype} primary key not null')
             continue
        column.append(f'{name} {datatype}')


create_query=f"create table if  not exists gitrepo({','.join(column)})"
cursor= connection.cursor()
cursor.execute(create_query)
connection.commit()

#cursor.execute(create_script)
for item in alldata:
    insert_script = f"insert into gitrepo(id,name,full_name,private,html_url) values {item} on conflict (id)  do nothing  "
    cursor.execute(insert_script)
    
connection.commit()
connection.close()
