# Notion de Worflow

un Workflow = ensemble de tâches orchestrées les unes à la suite des autres


##==##
<!-- .slide: -->
# Qu'est ce qu'un DAG ?

- un **DAG** = un **Workflow** dans Airflow

- DAG = **D**irected **A**cyclic **G**raph
</br></br>
c'est à dire
</br></br>
- un **graphe** contenant des tâches
- **non cyclique** = qui ne boucle pas sur lui-même
- **dirigé** = qui a un sens, un ordre chronologique 


##==##
<!-- .slide: -->
# Qu'est ce qu'un DAG ?

- dans un DAG, on définit des **tâches** (task) que l'on chaîne
- une tâche dans Airflow = un **appel** à un **opérateur** (operator)
- on **ordonne** les tâches **chronologiquement**


##==##
<!-- .slide: -->
# Un exemple de DAG
![dag example](./assets/images/dag_example.png)


##==##
<!-- .slide: -->

PLUSIEURS EXEMPLES


##==##
<!-- .slide: -->
# Comment créer un DAG ?

bout de code pour init
