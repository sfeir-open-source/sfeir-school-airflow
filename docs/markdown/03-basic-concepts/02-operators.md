# Les opérateurs

- un **opérateur** (operator) = **modèle** (ou template) de tâche pour effectuer une action spécifique
- l’action peut s’exécuter sur un système/application/service tier(ce) à Airflow
- utilisation d'interface (hooks) pour communiquer avec l'extérieur


##==##
<!-- .slide: -->
# Les tâches

- une tâche = un appel à un opérateur **avec des paramètres**
- une tâche = opération **atomique** à l'échelle d'Airflow
- toujours dans un des états suivants:
  ![task states](./assets/images/task_states.png)
- **par défaut**, les tâches s'exécutent si la/les précédente(s) sont en succès


##==##
<!-- .slide: -->
# Les tâches

![DAG example](./assets/images/state_example.png)


##==##
<!-- .slide: -->__
# Exemples d'opérateurs

- opérateur:
  - **BashOperator** permet d'exécuter une commande bash depuis Airflow

- tâche '**print_airflow_user**':
  ```python
  print_user = BashOperator(
      task_id='print_airflow_user',
      bash_command='echo $USER',
  )
  ```
  
Notes: le code présenté ici est la définition d'une tâche, on a appelé un opérateur existant avec des paramètres.

##==##
<!-- .slide: -->
# Exemples d'opérateurs
- opérateur:
  - **PythonOperator** permet d'exécuter une fonction python depuis Airflow
- tâche '**print_hello_world**':
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
