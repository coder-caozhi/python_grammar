function add(a, b){
    return a + b
}

let result = add("10")
console.log(result)

let obj = {
    "name":"吴亦凡",
    "age":35
}

// 对象解构
let {name,age} = obj
console.log(name)
console.log(age)

let array = [1,2,3,4]

// 数组解构
let [a,b,c,d] = array
console.log(a)
console.log(b)
console.log(c)
console.log(d)