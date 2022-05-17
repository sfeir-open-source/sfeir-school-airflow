// One method per module
function school() {
  return [
    '00-school/00-TITLE.md',
    '00-school/speaker-francois.md',
    '00-school/speaker-jonathan.md',
  ];
}

function airflowIntro() {
  return [
    '01-airflow-intro/00-TITLE.md',
    '01-airflow-intro/01-intro-airflow.md',
    '01-airflow-intro/02-airflow-ui.md',
    '01-airflow-intro/03-history.md',
    '01-airflow-intro/04-intro-orchestrator.md',
  ];
}

function installation() {
  return [
    '02-installation/00-TITLE.md',
    '02-installation/01-installation.md',
    '02-installation/02-prerequisites.md',
  ];
}

function basicConcepts() {
  return [
    '03-basic-concepts/00-TITLE.md',
    '03-basic-concepts/01-dag.md',
    '03-basic-concepts/02-operators.md',
    '03-basic-concepts/04-scheduler.md',
  ];
}

function formation() {
  return [
    ...school(),
    ...airflowIntro(),
    ...installation(),
    ...basicConcepts(),
  ].map(slidePath => {
    return { path: slidePath };
  });
}

export function usedSlides() {
  return formation();
}
