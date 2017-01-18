## Lecture 2: Functional Abstraction

### Question 1: Write a function
The variable `bar` is assigned the value of `10` when the following code is run:
~~~python
def foo():
    return 5

bar = foo() + foo()
~~~
Update the definition of `foo` so that the value of `bar` is 20 when the above code is run. Do not change the definition of `bar`

Answer guide:
~~~python
def foo():
    return 5
~~~
###Question 2
Which of the following are valid function definition(s)? Select all that apply.

~~~python
# A
def foo(a, b):
    return a + a

# B
def foo():
    return

# C
def foo:
    return b

# D
define foo(a):
    return a 

# E
def foo(a, b, c):
    a + b + c

# F
def foo(a)
return a
~~~
(More than 1 answer)

* F
* E
* D
* C
* B
* A

###Question 3: Function error
The `triple` function should return 3 * the argument of the function. However, the code below contains some error(s), so it does not behave as expected. Fix it.

Answer guide:
~~~python
def triple(amt):
    return 3 ** a
~~~

###Question 4
Which of the following is the correct output for the code snippet below?

~~~python
def square(x):
    return x * x

def double(x):
    return x + x

print(double(square(2)) - square(double(2)))
~~~

* 8
* 0
* -8
* 2
* Error

### Question 5: Squared Difference
We discussed the `square` function in the lecture. Using the `square` and `mean` functions provided, define a new function called variance that calculates the variance of **two** input parameters. Reuse the `square` and `mean` functions in your answer!

Refer to the formula for variance here: http://en.wikipedia.org/wiki/Variance.

**Note: This function is only applicable when computing the variance of two numbers, and you can assume that the inputs will be numbers.**

For example `variance(1, 5)` and `variance(5, 1)` should both return 4.0

Answer guide:
~~~python
def square(x):
    return x * x

def mean(x, y):
    return (x + y) / 2

def variance(x, y):
    # fill in your code here
    pass
~~~

### Question 6
Which of the following is the correct output for the code snippet below?

~~~python
x = 2
def square(x):
    x = 3
    return x * x

print(square(x), x, square(5))
~~~

* 9 2 9
* 4 9 25
* 9 3 9
* 2 2 2

### Question 7: Greetings
Given the cosmopolitan society we live in, many of us speak several different languages.

Here we will write a function named `greet`, that takes in a person's name and language, and **returns** a different greeting string depending on which language is given and include the person's name behind it.

**Note: Do not use the command `print` to print the greeting, `greet` should be return a string.**

You are free to include additional languages but for grading purposes, but minimally, please support the following 3 languages: English, Klingon and Elvish.

For example, 
`greet('Ben', 'English')` => `'Nice to meet you Ben'`
`greet('Okrand', 'Klingon')` => `'nuqneH Okrand'`
`greet('Elrond', 'Elvish')` => `'Gi suilon Elrond'`

Answer guide:
~~~python
def greet(name, language):
    # fill in your code here
    # return the string at the end, do not print it!
    pass # remove this line
~~~

### Question 8: Abstraction
The function `area_rect(x, y)` returns the area of a rectangle of length x and breadth y. 

Define a function `area_square(x)` that:

1. Returns the area of a square of length x. The `area_square` function should make use of the `area_rect` function. Thus, you do not need to know how the area of a rectangular is calculated.
2. Returns `0` if the input parameter is <= 0.

**Note: You do not have to define the `area_rect` function yourself. You simply have to call the function.**

Answer guide:
~~~python
def area_square(a):
    # Fill in code
    pass # remove this line
~~~

### Question 9: Code Reuse
**Note: In this question, 0 is considered to be neither a positive number nor negative number.**

You are to implement the following three functions with the following specifications:

1. `is_odd(x)` returns `True` if the input parameter `x` is odd, `False` otherwise.
2. `is_negative(x)` returns `True` if the input parameter `x` is negative, `False` otherwise. 
3. `is_even_and_positive(x)` returns `True` if the input parameter `x` is even AND positive, `False` otherwise.

Bear in mind that you should try to reuse functions whenever possible!

Answer guide:
~~~python
def is_odd(x):
    # Fill in code here
    pass # remove this line
    
def is_negative(x):
    # Fill in code here
    pass # remove this line
    
def is_even_and_positive(x):
    # Fill in code here
    pass # remove this line
~~~