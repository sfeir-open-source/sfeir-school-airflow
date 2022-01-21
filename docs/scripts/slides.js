// One method per module
function schoolSlides() {
  return [
    '00-school/welcome_school.md',
    '00-school/speaker_jch.md',
    '00-school/planning.md',
  ];
}

function introSlides() {
  return ['01-introduction/airflow.md'];
}

function formation() {
  return [
    //
    ...schoolSlides(), //
    ...introSlides(), //
    '02-architecture/operators.md',
    '03-operators/operators.md',
  ].map(slidePath => {
    return { path: slidePath };
  });
}

export function usedSlides() {
  return formation();
}
