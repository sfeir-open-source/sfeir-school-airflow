# Conditions

Nous l'avons vu avec le branching, nous pouvons orchestrer notre DAG selon certaine conditions.

Seulement, ces conditions sont limitées et ne permettent pas de communiquer avec l'extérieur.

Plusieurs solutions s'offrent à nous :
- SensorOperator
- CheckOperator

# SensorOperator

```python
FileSensor(
    task_id="checking",
    path="path/to/check/file.ext"
)
```

# CheckOperator

```python
BigQueryCheckOperator(
    task_id="checking",
    value_to_check=1000,
    sql="SELECT count(*) FROM orders"
)
```

# Detecter la présence d'un fichier CSV

