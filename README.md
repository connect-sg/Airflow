# Airflow

Setup - 
1. Install docker desktop from docker.com
2. Visual studio code

Why Airflow?
1. Helps set the order of tasks
2. Make sure each task starts only when the previous ones are done
3. Control the timing of your entire data process
4. Provides visibility, monitor progress of workflow
5. Flexibility and scalability

Core components - 
1. The web server
2. Scheduler
3. The meta database
4. Triggerer
5. Executor
6. Queue
7. Worker

Core Concepts - 
1. DAG(Directed acyclic graph) - define structure of entire workflow
2. Operator - Single, ideally idempotent task in your DAG (registry.astronomer.io/providers)
3. Task/ Task instance
4. Workflow

Airflow is not..
1. Not data processing framework
2. Not Real time streaming solution
3. Not Data storage system
4. Not for high frequency scheduling
5. Not for processing large datasets directly
6. Not for Real-time data streaming
7. Not for simple linear workflow with few dependencies

Architectures - 
1. Single node architecture - All components are running on one machine
   Scalable
   Reliable
   Performance
   Not for complext workflow

2. Multi node architecture
  Example - 
  
  node 1 -> webserver 1, webserver 2
                   -> Load balancer

  node 2 -> Scheduler 1, scheduler 2, Queues

  node 3, node 4, node 5 -> workers    

  node 6 -> meta database

How it works?
Add DAG -> FOlder DAG <---PARSER---> Scheduler -> metadata <-----DAG RUN, TASK INSTANCE-----> update-> Executor
