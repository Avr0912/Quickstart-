QUICKSTART+ DOCUMENTATION

SPECIFICATIONS
This quickstart+ program comes with options for three different data structures, those being stack, queue, and priority queue.






RUNNING THE APPLICATION:
In order to run the backend of the application, write the following command into the linux command line in the quickstart+ directory

docker compose up

Once this command is run, port 5000 will be exposed on the localhost to read in requests to the API


USEFUL API COMMANDS
ADD JOB
curl -X POST -H "Content-Type: application/json" -d '{"job_id": "<input id>", "priority": <input priority>, "job_name": "<input name"}' http://localhost:5000/<input datastructure>/jobs

GET JOB AT THE FRONT OF THE DS
curl http://localhost:5000/<INPUT DATASTRUCTURE>/jobs

GET JOB AT THE FRONT OF THE DS
curl http://localhost:5000/<INPUT DATASTRUCTURE>/jobs/job1

GET STATUS OF DATA STRUCTURE 
curl http://localhost:5000/<INPUT DATASTRUCTURE>/jobs/status

DELETE A JOB
curl -X DELETE http://localhost:5000/jobs/job1

