// One method per module
function schoolSlides() {
  return [
    '00-school/00-TITLE.md',
    '00-school/speaker-francois.md',
    '00-school/speaker-jonathan.md'
  ];
}

function introSlides() {
  return [
    '01-airflow-intro/00-TITLE.md',
    '01-airflow-intro/01-intro-airflow.md',
    '01-airflow-intro/02-airflow-ui.md',
    '01-airflow-intro/03-history.md',
    '01-airflow-intro/04-intro-orchestrator.md',
    '01-airflow-intro/05-installation.md',
  ];
}

function formation() {
  return [
    //
    ...schoolSlides(), //
    ...introSlides() //
  ].map(slidePath => {
    return { path: slidePath };
  });
}

export function usedSlides() {
  return formation();
}
