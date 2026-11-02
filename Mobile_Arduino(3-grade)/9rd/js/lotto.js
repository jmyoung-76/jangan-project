// 로또 생성기 프로그램의 핵심 데이터를 저장하는 변수들
let drawCount = 0; // 사용자가 버튼을 누른 총 생성 횟수
let currentNumbers = []; // 마지막으로 생성된 로또 번호 배열

// HTML 요소를 가져오는 변수들
const drawBtn = document.getElementById('drawBtn');
const resetBtn = document.getElementById('resetBtn');
const resultBox = document.getElementById('result');
const countValue = document.getElementById('countValue');

// 번호를 공 모양으로 화면에 출력하는 함수
// 배열에 들어 있는 숫자를 순서대로 하나씩 읽어서 HTML 요소를 생성한다.
function renderNumbers(numbers) {
  // 기존에 표시된 결과를 비운다.
  resultBox.innerHTML = '';

  // 번호 배열이 비어 있으면 빈 상태 메시지를 보여준다.
  if (!numbers.length) {
    resultBox.innerHTML = '<span class="empty">아직 생성된 번호가 없습니다.</span>';
    return;
  }

  // 배열의 각 숫자를 하나씩 돌면서 공 요소를 만든다.
  numbers.forEach((number) => {
    const ball = document.createElement('div');
    ball.className = 'ball ' + getBallColor(number);
    ball.textContent = number;
    resultBox.appendChild(ball);
  });
}

// 번호 범위에 따라 공 색상을 정하는 함수
// 로또 공은 숫자 크기와 무관하게 보기 좋게 구간별 색상을 지정한다.
function getBallColor(number) {
  if (number <= 10) return 'red';
  if (number <= 20) return 'orange';
  if (number <= 30) return 'yellow';
  if (number <= 40) return 'green';
  return 'blue';
}

// 1부터 45까지의 숫자 중 중복 없이 6개를 뽑는 함수
// Math.random()을 사용하여 무작위 숫자를 뽑고, 중복을 체크해 최종 6개를 만든다.
function generateLottoNumbers() {
  const numbers = [];

  while (numbers.length < 6) {
    const randomNumber = Math.floor(Math.random() * 45) + 1;

    // 같은 숫자가 이미 추가되어 있으면 다시 뽑는다.
    if (!numbers.includes(randomNumber)) {
      numbers.push(randomNumber);
    }
  }

  return numbers.sort((a, b) => a - b);
}

// 번호 뽑기 버튼 클릭 시 실행되는 함수
// 생성 횟수를 증가시키고, 숫자를 만들고, 화면에 출력한다.
function drawLotto() {
  currentNumbers = generateLottoNumbers();
  drawCount += 1;
  countValue.textContent = drawCount;
  renderNumbers(currentNumbers);
}

// 초기화 버튼 클릭 시 실행되는 함수
// 화면의 번호와 생성 횟수를 모두 초기값으로 되돌린다.
function resetLotto() {
  drawCount = 0;
  currentNumbers = [];
  countValue.textContent = '0';
  renderNumbers(currentNumbers);
}

// 버튼 이벤트 연결
// 사용자가 클릭하면 각각의 함수가 실행된다.
drawBtn.addEventListener('click', drawLotto);
resetBtn.addEventListener('click', resetLotto);

// 초기 로딩 시 기본 화면을 설정한다.
renderNumbers(currentNumbers);
countValue.textContent = drawCount;
