// Fatch API(HTTP 요청/응답)

// // GET/ posts(게시물 조회 요청)
// fetch("https://jsonplaceholder.typicode.com/posts")
//     .then(response => response.json()) // 응답에서 응답 본문(JSON) 꺼내기
//     .then(data => console.log(data)) // JSON 데이터를 화면에 출력

// POST/ posts(새로운 게시물 생성)
fatch("https://jsonplaceholder.typicode.com/posts", {
    mathod: "POST",
    // 요청 본문 데이터가 JSON 형식
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({title: "Python", "body": "Hello, Python"})
})

    // 요청의 결과(서버 응답)을 콘솔에 출력
    .then(response => response.json())
    .then(data => console.log(data))