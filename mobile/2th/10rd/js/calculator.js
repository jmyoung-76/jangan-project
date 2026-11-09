const STORAGE_KEY = 'todos'; // 계산기 상태를 저장할 키를 'todos'로 고정한다.
const display = document.getElementById('display'); // 계산 결과를 보여줄 화면 요소를 찾는다.

const clickSound = new Audio('https://cdn.pixabay.com/download/audio/2022/03/15/audio_c67ee9a55d.mp3?filename=soft-pop-1-185290.mp3'); // 숫자 클릭 시 재생할 작은 효과음을 준비한다.

let firstValue = '0'; // 첫 숫자를 저장하는 변수다.
let secondValue = ''; // 두 번째 숫자를 저장하는 변수다.
let operator = ''; // 선택된 연산자를 저장하는 변수다.
let isWaitingForSecondValue = false; // 두 번째 숫자 입력을 기다리는지 확인한다.
let isCalculated = false; // 마지막 계산이 끝났는지 확인한다.

function playClickSound() { // 숫자 버튼 클릭 소리를 재생하는 함수를 만든다.
  if (!clickSound) { // 효과음 객체가 없으면
    return; // 재생을 건너뛴다.
  } // 조건 분기를 닫는다.

  clickSound.currentTime = 0; // 재생 위치를 처음으로 되돌린다.
  clickSound.play().catch(() => { /* 자동 재생 차단 시 무시한다. */ }); // 브라우저 정책 때문에 재생이 막히면 예외를 무시한다.
} // 소리 재생 함수 끝.

function saveCalculatorState() { // 현재 계산 상태를 브라우저에 저장한다.
  const state = { // 저장할 상태 객체를 만든다.
    firstValue: firstValue, // 첫 값을 저장한다.
    secondValue: secondValue, // 두 번째 값을 저장한다.
    operator: operator, // 연산자를 저장한다.
    isWaitingForSecondValue: isWaitingForSecondValue, // 기다리는 상태를 저장한다.
    isCalculated: isCalculated // 계산 완료 상태를 저장한다.
  }; // 상태 객체를 완성한다.

  localStorage.setItem(STORAGE_KEY, JSON.stringify(state)); // 'todos' 키 하나를 사용해 저장한다.
} // 저장 함수의 끝이다.

function restoreCalculatorState() { // 저장된 계산 상태를 복원한다.
  try { // 저장 데이터가 잘못되어도 오류가 나지 않게 처리한다.
    const savedState = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}'); // 저장된 값을 객체로 바꾼다.

    if (!savedState || typeof savedState !== 'object') { // 저장 값이 없거나 잘못된 형식이면
      return; // 복원하지 않고 끝낸다.
    } // 조건 분기를 닫는다.

    firstValue = savedState.firstValue || '0'; // 저장된 첫 값을 복원한다.
    secondValue = savedState.secondValue || ''; // 저장된 두 번째 값을 복원한다.
    operator = savedState.operator || ''; // 저장된 연산자를 복원한다.
    isWaitingForSecondValue = Boolean(savedState.isWaitingForSecondValue); // 대기 상태를 복원한다.
    isCalculated = Boolean(savedState.isCalculated); // 계산 완료 상태를 복원한다.
    display.textContent = secondValue || firstValue || '0'; // 화면에 복원된 값을 표시한다.
  } catch (error) { // 잘못된 저장값이면 예외를 처리한다.
    localStorage.removeItem(STORAGE_KEY); // 깨진 저장값을 삭제한다.
    firstValue = '0'; // 첫 값을 초기값으로 만든다.
    secondValue = ''; // 두 번째 값을 비운다.
    operator = ''; // 연산자를 비운다.
    isWaitingForSecondValue = false; // 대기 상태를 해제한다.
    isCalculated = false; // 계산 완료 상태를 해제한다.
    display.textContent = '0'; // 화면을 0으로 초기화한다.
  } // 예외 처리를 마친다.
} // 복원 함수의 끝이다.

function renderDisplay(value) { // 화면에 값을 표시하고 상태를 저장한다.
  display.textContent = value; // 표시값을 화면에 넣는다.
  saveCalculatorState(); // 변경된 상태를 저장한다.
} // 화면 표시 함수의 끝이다.

function inputNumber(numberText) { // 숫자 버튼을 눌렀을 때 실행한다.
  playClickSound(); // 숫자 입력 시 클릭 소리를 재생한다.

  if (isCalculated) { // 최근 계산이 끝났다면
    firstValue = '0'; // 첫 값을 초기값으로 바꾼다.
    secondValue = ''; // 두 번째 값을 비운다.
    operator = ''; // 연산자를 비운다.
    isCalculated = false; // 계산 완료 상태를 해제한다.
  } // 계산 완료 상태를 정리한다.

  if (isWaitingForSecondValue) { // 두 번째 숫자를 입력할 차례라면
    secondValue += numberText; // 숫자를 이어 붙인다.
    renderDisplay(secondValue); // 두 번째 값을 화면에 표시한다.
    return; // 입력 처리 끝이다.
  } // 두 번째 입력 분기를 닫는다.

  if (firstValue === '0' && numberText === '0') { // 0이 이미 보이는 상태인데 0을 다시 누르면
    return; // 중복 입력을 막는다.
  } // 조건문을 닫는다.

  if (firstValue === '0') { // 현재 첫 값이 0이면
    firstValue = numberText; // 0을 새 숫자로 교체한다.
  } else { // 그 외에는
    firstValue += numberText; // 숫자를 이어 붙인다.
  } // 숫자 이어 붙이기를 끝낸다.

  renderDisplay(firstValue); // 첫 값을 화면에 표시한다.
} // 숫자 입력 함수의 끝이다.

function calculateResult(leftValue, rightValue, selectedOperator) { // 두 숫자와 연산자로 최종 계산을 한다.
  switch (selectedOperator) { // 선택된 연산자별로 분기한다.
    case '+': // 더하기 연산이다.
      return leftValue + rightValue; // 두 수를 더한다.
    case '-': // 빼기 연산이다.
      return leftValue - rightValue; // 왼쪽 수에서 오른쪽 수를 뺀다.
    case '*': // 곱하기 연산이다.
      return leftValue * rightValue; // 두 수를 곱한다.
    case '/': // 나누기 연산이다.
      if (rightValue === 0) { // 0으로 나누는 경우를 확인한다.
        return '오류'; // 오류 값을 반환한다.
      } // 0 나누기 예외를 처리한다.
      return leftValue / rightValue; // 정상 나누기를 실행한다.
    default: // 알 수 없는 연산자는 기본값으로 처리한다.
      return leftValue; // 왼쪽 값을 그대로 반환한다.
  } // switch문을 닫는다.
} // 계산 함수의 끝이다.

function inputOperator(nextOperator) { // 연산자 버튼을 눌렀을 때 실행한다.
  if (operator && secondValue && !isWaitingForSecondValue) { // 이미 연산자가 있고 두 번째 값이 준비돼 있으면
    const result = calculateResult(Number(firstValue), Number(secondValue), operator); // 앞의 계산을 먼저 수행한다.
    firstValue = String(result); // 계산 결과를 첫 값으로 저장한다.
    secondValue = ''; // 두 번째 값을 비운다.
    operator = nextOperator; // 새 연산자를 설정한다.
    isWaitingForSecondValue = true; // 다음 숫자를 두 번째 값으로 받는다.
    renderDisplay(firstValue); // 계산 결과를 화면에 표시한다.
    return; // 연산자 입력을 마친다.
  } // 연속 연산 처리 분기를 닫는다.

  operator = nextOperator; // 사용자가 선택한 연산자를 저장한다.
  isWaitingForSecondValue = true; // 다음 입력을 두 번째 숫자로 받는다.
  isCalculated = false; // 계산 완료 상태를 해제한다.
  saveCalculatorState(); // 상태를 저장한다.
} // 연산자 입력 함수의 끝이다.

function inputEqual() { // 등호 버튼을 눌렀을 때 실행한다.
  if (!operator) { // 연산자가 없으면
    return; // 계산을 하지 않는다.
  } // 조건문을 닫는다.

  const leftNumber = Number(firstValue); // 첫 숫자를 숫자로 바꾼다.
  const rightNumber = Number(secondValue || firstValue); // 두 번째 값이 없으면 첫 값을 사용한다.
  const result = calculateResult(leftNumber, rightNumber, operator); // 계산 결과를 구한다.

  if (result === '오류') { // 나누기 0 또는 오류 상태인지 확인한다.
    firstValue = '0'; // 첫 값을 초기값으로 되돌린다.
    secondValue = ''; // 두 번째 값을 비운다.
    operator = ''; // 연산자를 비운다.
    isWaitingForSecondValue = false; // 대기 상태를 해제한다.
    isCalculated = false; // 계산 완료 상태를 해제한다.
    renderDisplay('오류'); // 오류 메시지를 화면에 보여준다.
    return; // 함수 종료한다.
  } // 오류 처리 분기를 닫는다.

  firstValue = String(result); // 계산 결과를 첫 값으로 저장한다.
  secondValue = ''; // 두 번째 입력값을 비운다.
  operator = ''; // 연산자를 비운다.
  isWaitingForSecondValue = false; // 대기 상태를 끝낸다.
  isCalculated = true; // 계산 완료 상태를 표시한다.
  renderDisplay(firstValue); // 최종 결과를 화면에 표시한다.
} // 등호 입력 함수의 끝이다.

function clearCalculator() { // clear 버튼을 누르면 계산 상태를 초기화한다.
  firstValue = '0'; // 첫 값을 0으로 되돌린다.
  secondValue = ''; // 두 번째 값을 비운다.
  operator = ''; // 연산자를 비운다.
  isWaitingForSecondValue = false; // 대기 상태를 해제한다.
  isCalculated = false; // 계산 완료 상태를 해제한다.
  renderDisplay('0'); // 화면을 0으로 초기화한다.
} // clear 함수의 끝이다.

const buttons = document.querySelectorAll('button'); // 모든 버튼 요소를 한 번에 찾는다.
buttons.forEach((button) => { // 각 버튼마다 이벤트를 연결한다.
  button.addEventListener('click', () => { // 버튼 클릭 이벤트를 등록한다.
    const action = button.dataset.action; // 버튼의 동작 유형을 읽는다.
    const value = button.dataset.value; // 버튼의 값 또는 기호를 읽는다.

    if (action === 'number') { // 숫자 버튼이면
      inputNumber(value); // 숫자 입력 함수를 실행한다.
    } else if (action === 'operator') { // 연산자 버튼이면
      inputOperator(value); // 연산자 입력 함수를 실행한다.
    } else if (action === 'equal') { // 등호 버튼이면
      inputEqual(); // 계산 결과 함수를 실행한다.
    } else if (action === 'clear') { // clear 버튼이면
      clearCalculator(); // 초기화 함수를 실행한다.
    } // 조건 분기를 닫는다.
  }); // 클릭 이벤트 함수 끝이다.
}); // 버튼 반복문 끝이다.

restoreCalculatorState(); // 저장된 상태를 복원한다.
renderDisplay(display.textContent || '0'); // 화면이 비어 있으면 0을 보여준다.
