## Lecture 1: Introduction to Python

###Question 1
~~~python
one = 2
two = 3
three = 1

ans = one * (three - two)
~~~
What is the value of ans?

* 2
* -4
* 6
* 1

###Question 2
After the following statements, what are the values of x and y?

~~~python
x = 15
y = x
x = 22
~~~
* x is 22 and y is 15
* x is 15 and y is 22
* x is 22 and y is 22
* x is 15 and y is 15

###Question 3
What is printed by the following line of code?
~~~python
print(18 / 4)
~~~
* 5
* 4.5
* 4.0
* 4

###Question 4
What is the value of the following expression:
~~~python
2 ** 3 * 3
~~~
* 512
* 256
* 24
* 18


###Question 5
Which is the most accurate way to determine the type of a variable?

* Guess from the name of the variable.
* Use it in a known equation and print the result.
* Use the type() function.
* Print out the value and determine the data type based on the value printed.

###Question 6
What is the data type of "this is what kind of data"?

* float
* string
* integer
* character

###Question 7
Which of the following are legal Python names?
(More than 1 answer)

* _HAPPY_DAY
* happyDay
* 18happyday
* happyday!
* Happy_day
* haPpyDay

###Question 8
Which of the following results in a `SyntaxError`?

* None of above
* '''I'm an answer'''
* 'python\\'
* '"Once upon a time...", he said.'
* "I've heard of that!"

###Question 9
~~~python
s = 'cheesecake'
~~~
What does the slice `s[1:6]` produce?

* heese
* chees
* heesec
* cheese

###Question 10
Which of the following evaluates to `True`?
(More than 1 answer)

* 'here' not in 'everywhere'
* 'here' == 'there'[1:]
* '5' != 5 (answer)
* 'eight' >= 'eighteen'
* 'two' > 'seven billion'

###Question 11
In Python, the start index, stop index and step size of slices can each take on negative values. `s[-1]` refers to the last element of `s`, `s[-2]` the second last and so on. Negative steps sizes indicate that 'steps' are taken in the direction of decreasing indices when selecting elements to be included in the slice. 

For example, `'banana'[-1]` will return `'a'` and `'through'[::-2]` takes every alternate character of the string `'through'` starting from the last character towards the first, resulting in `'hurt'`. [Open the Python shell in IDLE and experiment for yourself.]

`s = 'banananananananab'`

Which of the following returns 'banana'?
(More than 1 answer)

* s[:-11]
* s[0:2] + (s[-2] + s[2])[::-1] * 2
* s[-6:][::-1]
* s[-1:-7]
* s[:-6:-1]
* s[0:10:-1]
* s[:10:-1]
* s[-1:10:-1]
* s[::3]
* s[:6]

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
* None of the above
* 4
* 3
* 2
* 1