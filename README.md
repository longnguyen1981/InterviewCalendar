# InterviewCalendar

This repo is an API to map the available time slots of the interviewers and the candidates. The code is written in Python and a Postgresql database is used to store the data.

### Setup ###
The instructions below help you to start the service on your local machine using docker.

- Prerequisite [Docker installed](https://docs.docker.com/install/)

1. Start the service
   ```
   .bin/start_service
   ```
2. Stop the service
    ```
    .bin/drop_all
    ```
    
### Startup ###
After start the service you can try to reach the API on your local machine. This should response Ok:
```
localhost:7000/health
``` 
1. Add the time slots
    - Send a POST to
      ```
      localhost:7000/add
      ```
    - Form of Input: 
      ```
      {"data": [{"name": "A", "fromhour": 9, "tohour": 12, "day": "Wed"},
                {"name": "B", "fromhour": 8, "tohour": 16, "day": "Thu"}]}
      ``` 
2. Get the info
    - Send a GET to
      ```
      localhost:7000/get/<name of people>
      ```
3. Update the time slots
    - Send an UPDATE to
      ```
      localhost:7000/update/<id>
      ```
    - Form of Input: 
      ```
      {"data": {"name": "A", "fromhour": 9, "tohour": 12, "day": "Wed"}}
      ```  
4. Delete the time slots
    - Send a DELETE to
      ```
      localhost:7000/update/<id>
      ```
5. Get available time slots
    - Send a GET to
      ```
      localhost:7000/map
      ```
    - Form of Input:
      ```
      {"names": {"A", "B", "C"}}
      ```  

### Tests ###
To run unittest you have to install the dependencies under [virtulenv](https://virtualenv.pypa.io/en/latest/installation/) by
```
pip install -r requirements.txt
```

then run 
```
python -m unittest
```