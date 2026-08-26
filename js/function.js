// 함수(Function)
function add(n1, n2) {
    return n1 + n2
}

let result = add(4, 2)
console.log(result)


// result에 add 함수의 반환값 할당
let result = add(4, 2);

// 1. 함수를 변수에 할당할 수 있다
let  f = add;
let result = f(10, 6)
console.log(result);

// 2. 함수를 다른 함수의 인자로 전달할 수 있다
function 계산기(연산함수) {
    // let f = add
    return f(4, 2)
}

let result = 계산기(add);
console.log(result);