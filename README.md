# airflow_experiments

```
$ python3 dags/main.py -h
usage: main.py [-h] -n NAME -bd BIRTHDATE

Get user input.

options:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Enter name in string.
  -bd BIRTHDATE, --birthdate BIRTHDATE
                        Enter birthdate in yyyy-mm-dd format.
```

## How to run?

```
python3 dags/main.py -n Lily -bd 2020-01-03
```

## How to create DAG?
```
python3 dags/dag.py
```

## Repo structure

```
.
│
├── README.md
├── .gitignore
├── requirements.txt
├── webserver_config.py
├── airflow-webserver.pid
├── airflow.db
├── airflow.cfg
├── ...
│
├── dags                             
│   ├── main.py            
│   └── dag.py
│
└── ...
```