const todoInput = document.querySelector("#todo-input")
const button = document.querySelector("#add-btn")
const todolist = document.querySelector("#todo-list")


let todos = []

// saveTodos() = 데이터 저장 (쓰기)
// savedTodos = 변수명. 저장된 데이터 읽기
// localStorage.getItem() -> localStorage에서 JSON 문자열을 배열로 변환해서 로드
const savedTodos = JSON.parse(localStorage.getItem("todos"))

// const saveTodos = localStorage.getItem("todos")
if(savedTodos) {
    todos = savedTodos
    renderTodos()

}
function addTodo() {
    if(todoInput.value) {
      todos.push(todoInput.value)
      todoInput.value = ""

      saveTodos()
      renderTodos()
    }
}

// Todo 추가
button.addEventListener("click", addTodo)
todoInput.addEventListener("keydown", e => {
    if (e.key == "Enter" && !e.isComposing) addTodo() //엔터가 눌리면 addTodo 호출
        
})

// 전체 todo 목록을 함수에 그리는 함수
function renderTodos() {
    //기존 목록 지우기
    todolist.innerHTML =""

    // 모든 todo list 배열에는 인덱스 번호가 존재함
    for (const [index, todo] of todos.entries()) {
        //const todo of todos) {
         const li = document.createElement("li")
         li.textContent = todo
         li.className = "list-group-item d-flex justify-content-between align-items-center"


        const deleteButton = document.createElement("button")
        deleteButton.textContent = "삭제"
        deleteButton.className = "btn btn-sm btn-danger"
        deleteButton.addEventListener("click", () => {
            todos.splice(index, 1)
            saveTodos()
            renderTodos() // 빼고 싶은 내용만 빠진 상태로 다시 그려줌
        })

          li.appendChild(deleteButton)
          todolist.appendChild(li)
    }
}

function saveTodos() {
    localStorage.setItem("todos", JSON.stringify(todos))
}