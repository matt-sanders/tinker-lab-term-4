This week we covered three main topics:

- Passing arguments to functions. This allows us to create variables that are only accessible by a single function and makes functions more dynamic and re-usable. E.g. `move_forward( seconds )` and `turn( direction )`.
  - Function arguments are generally lowercase.
  - When a function accepts an argument, we have to send that argument along when we call it. E.g. `turn( 'l' )` or `move_forward( 1 )`.
- Conditional statements. We were introduced to `if` and `elif` which allows us to write code that responds differently to different situations. E.g. `turn( 'l' )` will turn left and `turn( 'r' )` will turn right.
  - `elif` is shorthand for "else if".
  - We use `==` to check if two things are equal to each other, ( e.g.  `direction == 'l'` ).
- Loops. We covered the `while` loop, and more specifically `while True:` to make a loop that runs forever! With this we can run the same function over and over again. We saw this with our `square_dance` function which made Rocky do the same square "dance" on repeat until we pressed the "b" button.
  - `while True:` means that the code will run forever!
  - `while` loops can accept any condition, e.g. `while ButtonIsPressed == True:`
