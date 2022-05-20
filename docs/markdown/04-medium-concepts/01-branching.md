# Branching

Comment organiser les opérateurs ?

TODO : insérer une image d'un dag complexe en terme de branching

# Un par un 

``` python
task1 >> task2 >> task3
``` 

TODO: image d'un graph correspondant

# En parrallèle

``` python
task1 >> [task2, task3]
``` 

TODO: image d'un graph correspondant

# Regroupement

``` python
task1 >> task3
task2 >> task3
``` 

TODO: image d'un graph correspondant

# En parrallèle puis regroupé

``` python
task1 >> [task2, task3] >> task4
``` 

TODO: image d'un graph correspondant

# LAB : Avec des opérateurs

``` python
BranchPythonOperator(
    task_id="branching",
    callable=myfunction
)
``` 

TODO: image d'un graph correspondant
