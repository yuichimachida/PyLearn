`1-1`
\* : Operator
'hello' : Value
-88.8 : Value
- : Operator
/ : Operator
+ : Operator
5 : Value

`1-2`
spam = Variable
'spam' = Argument

`1-3`
3 data types
  * Integer
  * String
  * Float

`1-4`
>What is expression made up of? What do all expressions do?



`1-5`
>This chapter introduced assignment statements, like spam = 10.
What is the difference an expression and a statement?

`1-6`
\>bacon = 20
\>bacon + 1
21

`1-7`
>Why is *eggs* a valid variable name while *100* is invalid?

*100* is number which is banned as Variable.

`1-8`
>What three functions can be used to get the integer, floating-point number, or string version of a value?

int()
float()
str()

`1-9`
>Why does this expression cause an error? How can you fix it?
> 'I have  eaten ' + 99 + ' burritos'

99 is not string.
'I have eaten ' + str(99) + ' burritos' is work.

`Extra credit`
>Look up what the *round()* function does, and experiment with it in the interactive shell.

*round()* round floating-point number as you like.
If only a floating-point number as an argument, python round it to nearest integer.
If you use 2nd argument it must be integer, python round the 1st argument until you set as 2nd argument.
ちなみに偶数丸め（銀行丸め、ISO丸め、五捨五入）です。
>Return number rounded to ndigits precision after the decimal point. If ndigits is omitted or is None, it returns the nearest integer to its input.
