
import argparse
import dotenv
import psycopg2
import os 
import asyncio
import aiohttp  
import json


pythotosql={
    'int':'INT',
    'float':'DECIMAL',
    'str':'TEXT',
    'bool':'BOOLEAN',
    'dict':'JSON',
    'list':'JSON',
    'NonType':'TEXT'

 

}


def httpcalls(session,calls,gitoken):
    print(gitoken)
    headers = {
         
    "Authorization": f'Bearer {gitoken}',
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2026-03-10",
}
    task=[]
    for call in calls :
            for i in range(1, 31):
                params = {"per_page": 100, "page": i}
                response = session.get(f'https://api.github.com/users/{call}/repos',params=params,headers=headers)
                task.append(response)
                

                
    return task 

async def  Fetching(usernames,token):
    
    data = []
    async with aiohttp.ClientSession() as session : 
         task = httpcalls(session,usernames,token)
         responses = await   asyncio.gather(*task)

         for response in responses:
            value = await response.json()
            if value : 
                 data.extend(value)

    return data 


def storingDatatoPush(data ):
     alldata=[]
     for info in data :
        values = []
    
        values.append((info['id'],info['name'],info['full_name'],info['private'],info['html_url']))
        alldata.extend(values)
     return alldata

def connectiontodb(hostname,db,username,password,port):
    connection= psycopg2.connect(
    host=hostname,
    dbname=db,
    user=username,
    password=password,
    port=port

 )
    return connection


    
     
parser = argparse.ArgumentParser()
subpars = parser.add_subparsers(dest='command')
fetch_command = subpars.add_parser('fetch')
fetch_command.add_argument('-u', nargs='+' ,required=True)
fetch_command.add_argument('-gittoken',required=True)
store_command  = subpars.add_parser('store')
store_command.add_argument('-u', nargs='+',required=True)
store_command.add_argument('-dbusername',required=True)

store_command.add_argument('-hostname',type=str, required=True)
store_command.add_argument('-password',type=str,required=True)
store_command.add_argument('-port',required=True)
store_command.add_argument('-db',type=str,required=True)
store_command.add_argument('-gittoken',type=str,required=True)

args = parser.parse_args()

if args.command == 'fetch' :
    calls= None
    print(args.u)
    
    data = asyncio.run(Fetching(args.u,args.gittoken))
    print(json.dumps(data,indent=4))
         

if args.command =='store':
    data = asyncio.run(Fetching(args.u,args.gittoken))
    alldata = storingDatatoPush(data)
    connection=connectiontodb(args.hostname,args.db,args.dbusername,args.password,args.port)
    cursor = connection.cursor()
    for item in alldata:
        insert_script = f"insert into gitrepo(id,name,full_name,private,html_url) values {item} on conflict (id)  do nothing  "
        cursor.execute(insert_script)
    connection.commit()
    connection.close()
    print('Sucess check your DB ')        


     


     