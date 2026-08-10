
import argparse
import dotenv
import psycopg2
import os 
import asyncio
import aiohttp  

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
def httpcalls(session):
    task=[]
    for call in calls :
            for i in range(1, 31):
                params = {"per_page": 100, "page": i}
                response = session.get(f'https://api.github.com/users/{call}/repos',params=params,headers=headers)
                task.append(response)
                

                
    return task 



parser = argparse.ArgumentParser()
subpars = parser.add_subparsers()
fetch_command = subpars.add_parser('fetch')
fetch_command.add_argument('-u', required=True,)

store_command  = subpars.add_parser('store')
store_command.add_argument('-u', type=str)
store_command.add_argument('=h',type=str)
store_command.add_argument('-p',type=str)
store_command.add_argument('-db',type=str)
store_command.add_argument('-gittoken',type=str)

args = parser.parse_args()

