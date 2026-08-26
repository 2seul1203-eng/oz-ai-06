// 조건문 (if/else)
// falsy: false, 0, "", null, nudefined, NaN(Not a Number)
// truthy: 그 외

let age = 20;

if (user_input) {
    console.log("성인입니다");
} else if (age >= 8) {
    console.log("학생입니다");
} else {
    console.log("어린이입니다");
}
