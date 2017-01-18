## Answers to Lecture 1: Introduction to Python

###Question 1
~~~python
one = 2
two = 3
three = 1

ans = one * (three - two)
~~~
What is the value of ans?

Answer: -4

###Question 2
After the following statements, what are the values of x and y?

~~~python
x = 15
y = x
x = 22
~~~
Answer: x is 22 and y is 15

###Question 3
What is printed by the following line of code?
~~~python
print(18 / 4)
~~~
Answer: 4.5

In Python 3, the / operator does exact division and returns a floating point result.

###Question 4
What is the value of the following expression:
~~~python
2 ** 3 * 3
~~~
Answer: 24

The exponentiation operator takes precedence over multiplication and hence it is evaluated first.

###Question 5
Which is the most accurate way to determine the type of a variable?

Answer: Use the type() function.

###Question 6
What is the data type of "this is what kind of data"?

Answer: string

###Question 7
Which of the following are legal Python names?

Answers:

* _HAPPY_DAY
* happyDay
* Happy_day
* haPpyDay

Happy_day is not a good style though. In this course, please follow the Python convention - use lower case letters and underscores.

###Question 8
Which of the following results in a `SyntaxError`?

Answer: 'python\\'

'python\\': Backslash in computer science is commonly used to escape the character behind it but will not be printed out. e.g print('\\'Great!\\', he said.') gives 'Great!', he said.

###Question 9
~~~python
s = 'cheesecake'
~~~
What does the slice `s[1:6]` produce?

Answer: heese

###Question 10
Which of the following evaluates to `True`?

Answers:

* 'here' == 'there'[1:] 
* '5' != 5
* 'two' > 'seven billion'

###Question 11
In Python, the start index, stop index and step size of slices can each take on negative values. `s[-1]` refers to the last element of `s`, `s[-2]` the second last and so on. Negative steps sizes indicate that 'steps' are taken in the direction of decreasing indices when selecting elements to be included in the slice. 

For example, `'banana'[-1]` will return `'a'` and `'through'[::-2]` takes every alternate character of the string `'through'` starting from the last character towards the first, resulting in `'hurt'`. [Open the Python shell in IDLE and experiment for yourself.]

`s = 'banananananananab'`

Which of the following returns 'banana'?

Answers:

* s[:-11]
* s[0:2] + (s[-2] + s[2])[::-1] * 2
* s[-6:][::-1]
* s[:10:-1]
* s[-1:10:-1]
* s[::3]
* s[:6]

s[0:2] + (s[-2] + s[2])[::-1] * 2 is correct. You can slice any expression (in this case, s[-2] + s[2]) that returns a string.
s[-6:][::-1] is correct. Python allows slicing a slice.
s[:10:-1] is correct. The default 'start' of the string depends on which direction you are 'stepping' in.

###Question 12
What is the output of the following piece of code?
~~~python
if not False and not True:
    if '123' == 123:
        print('1')
    elif 2 ** 3 == 3 ** 2:
        print('2')
else:
    if (not True or not False) and (False and True):
        print('3')
    elif False or True:
        print('4')
~~~
Answer: 4