function square(x) {
  return x * x
}

var f = square

console.log(square)
console.log(f(5)) // first class function

function my_map(func, arg_list) {
  result = []
  for (var i = 1; i <= args_list.length; i++) {
    result.push(func(i))
  }
  return result
}

var squares = my_map(cube, [1, 2, 3, 4, 5])

console.log(squares)

function cube(x) {
  return x * x * x
}
