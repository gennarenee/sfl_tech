SFL Scientific - Genna Hilbing Technical Assessment
##################################################
NOTE: Sections 2 and 3 require docker to run.

Directory Structure
├── section_1
├── section_2
│   ├── jar
│   └── __pycache__
├── section_3
│   └── fashion_model
│       └── 1659311357
│           ├── assets
│           └── variables
└── sfl_venv

section_1: Includes PDF of answers to questions.

section_2: Please execute file by running "docker build ." from the section_2 directory.
    -jar: includes mysql jar file
    -app.py: python application for running transformations.
    -DATA.csv: data for transformation.
    -Dockerfile: file for running docker commands.
    -outcome.PNG: screenshot of data in MySQL Workbench to verify that data has been loaded in case
        AWS RDS MySQL database cannot be accessed.
    -requirements.txt: text file of python requirements.
    -util.py: functions to support app.py.
    -Information needed to access AWS DB:
        user = "admin"
        password = "adminpass"
        host = "techdb.cmhgbb7baamz.us-east-1.rds.amazonaws.com"
        port = 3306

section_3: Please run ml-app.sh in section_3 directory to run code; dockerfile not used to avoid docker-in-docker.
    -fashion_model: includes model created using fashion_mnist dataset.
    -ml-app.py: python code use to create resultant model.
    -ml-test.py: python code that can be run to test api connection.
    -API hosted on localhost:8501

