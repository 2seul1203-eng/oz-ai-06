// Timer API(시간 관리 API)

// [1] setTimeout: 특정 시간이 지나면, 함수를 실행해주는 API
// 예: 30분 뒤 자동 로그아웃
// setTimeout(
//     () => console.log("시간이 종료되었습니다."),
//     3000 // 3000ms = 3s
// )

// setInterval: 특정 시간마다 함수를 실행해주는 API
// setTimeout/setInterval은 자신의 Timer 정보를 반환
setInterval(
    () => console.log("1초 경과"),
    1000 // 1000ms = 1s
)

// 타이머를 멈출 때는 어떤 타이머를 멈출지 지정
clearInterval(timerId)