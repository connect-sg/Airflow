from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup


from datetime import datetime

def download_tasks():
    with TaskGroup("downloads", tooltip = "Download tasks") as group:

        downlaod_a  = BashOperator(
            task_id = 'download_a',
            bash_command = 'sleep 10'
        )
        downlaod_b  = BashOperator(
            task_id = 'download_b',
            bash_command = 'sleep 10'
        )
        downlaod_c  = BashOperator(
            task_id = 'download_c',
            bash_command = 'sleep 10'
        )

        return group