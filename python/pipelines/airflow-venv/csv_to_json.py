import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

import pandas as pd

def CSVtoJSON():
    df = pd.read_csv('../../csv/data.csv')
    for i,r in df.iterrows():
        print(r['name'])
    df.to_json('fromAirflow.json',orient='records')

default_args = {
    'owner': 'loken',
    'start_date': dt.datetime(2024,2,18),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5)
}

with DAG('MyCSVDAG',
         default_args = default_args,
         schedule_interval=timedelta(minutes=5),
         # '0 * * * *',
         ) as dag:
    print_starting = BashOperator(task_id='starting',
                                  bash_command = 'echo "I am reading the csv now ..."')
    CSVJson = PythonOperator(task_id='convertCSVtoJSON',
                             python_callable=CSVtoJSON)
    
print_starting .set_downstream(CSVJson)

# alternative to set upstream and downstream would be
#  CSVJson .set_upstream(print_starting)

# or alternatively bit shift operator
# print_starting >> CSVJson
# CSVJson << print_starting


