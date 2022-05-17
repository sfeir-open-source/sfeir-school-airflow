# Les opérateurs

- un opérateur (operator) = **modèle** (ou template) de tâche pour effectuer une action spécifique
- l’action peut s’exécuter sur un système/application/service tier(ce) à Airflow
- utilisation de "Hooks" pour communiquer avec l'extérieur


##==##
<!-- .slide: -->
# Les tâches

- une tâche = 

##==##
<!-- .slide: -->
# Exemples d'opérateurs

- **BashOperator** permet d'exécuter une commande bash depuis Airflow
```python
print_user = BashOperator(
    task_id='print_airflow_user',
    bash_command='echo $USER',
)
```


##==##
<!-- .slide: -->
# Exemples d'opérateurs
- **PythonOperator** permet d'exécuter une fonction python depuis Airflow
```python
def hello(my_word: str):
    print(f'hello {my_word}')

print_hello_world = PythonOperator(
    task_id='print_hello_world',
    python_callable=hello,
    op_args=['world'],
)
```

##==##
<!-- .slide: -->
# Exemples d'opérateurs
- PostgresOperator


##==##
<!-- .slide: -->
# Exemples d'opérateurs
- BigQueryToGCSOperator


##==##
<!-- .slide: -->
# 

- multitude d'opérateurs existants
- dédié à tout type de services
- possibilité d'écrire ses propres opérateurs
