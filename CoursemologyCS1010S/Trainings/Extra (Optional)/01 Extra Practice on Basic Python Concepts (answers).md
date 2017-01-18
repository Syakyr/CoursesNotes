## Extra Practice on Basic Python Concepts

### Question 1: Variable assignment
You can store numbers into variables and reuse it later. For example, `x = 3` and `y = 4` and `x + y` will output 7.

As an exercise, assign the value 1 and 2 to `num1` and `num2` respectively.

~~~python
num1 = 1
num2 = 2
~~~

### Question 2: Type checking
Python comes with a inbuilt function that can help us to check the type of a variable. For example, `type('this is a string')` will output string type.

As an exercise, assign the types of `x`, `y` and `z` respectively to `x_type`, `y_type`, `z_type`. The first example has been completed for you.

Hint: Similar to numbers, you can also store types as values into variables.

~~~python
x = 2
y = 2.0
z = '2'
x_type = type(x)
y_type = type(y)
z_type = type(z)
~~~

### Question 3: String concatenation
To concatenate strings in python, you can use the plus(+) sign.

For example, "There are 240 students in this class" + " and it is great!" will become
"There are 240 students in this class and it is great!"

As an exercise, assign a string using `gunshot_single` and `car_exploded` to `guns_fired` such that `guns_fired` will have the value `'Bang!Boom!'`.

~~~python
gunshot_single = 'Bang!'
car_exploded = 'Boom!'
guns_fired = gunshot_single + car_exploded
~~~

###Question 4: Multiplying strings
You can multiply strings in python using the multiplication operator: `*`

For example, `"woof!" * 3` will give `"woof!woof!woof!"`

As an exercise, fill in the answer for `fire_3_times` such that it repeats `gunshot_single` for 3 times to get `'Bang!Bang!Bang!'`

Then, fill in the answer `fire_21_times` such that it repeats `gunshot_single` for 21 times to get
`Bang!Bang!Bang!.......Bang!Bang!` where `Bang!` occurs in the string 21 times.

~~~python
gunshot_single = 'Bang!'
fire_3_times = gunshot_single * 3
fire_21_times = fire_3_times * 7
# You can also use the following:
# fire_21_times = gunshot_single * 21
~~~

###Question 5: length of string
You can use the inbuilt `len` function in python to calculate the length of a string. For example, `len('I am a short string')` will output 19.

As an exercise, assign the length of `super_long_string` to `my_length`.

~~~python
super_long_string = "I am so long that it is so taxing on the eyes to count the actual length of my string. You should rely on python to help you do this"
my_length = len(super_long_string)
~~~

###Question 6: String slicing
You can perform string slicing to remove portions of string that we may not be interested in. 

For example, given `my_recent_purchase = 'I bought a new toy but it costed me 100 dollars'` and we can do `my_recent_purchase[:18]` to only retain the characters from the **start to index 17** of the string. `my_recent_purchase[9:]` will output all the characters from **index 9 to the end** of the string. You can use also `my_recent_purchase[2:5]` to get the characters from **index 2 to 4** of the string. Try them!

As an exercise, assign the string consisting of the index 5 to index 15 (inclusive) from `long_string` to `character_from_5_to_15` using string slicing. 

~~~python
long_string = 'I am only interested in the characters from 5 to 15 in this string'
character_from_5_to_15 = long_string[5:16]
~~~

### Question 7: More on strings
You can perform `find`, `replace` operations on strings to find and replace certain strings within another string. For example, given `my_string = 'This is my dog'`, you can use `my_string.find('dog')` to obtain the start position of the string `'dog'` in `my_string`. `my_string.find('dog')` will output 11.

You can use `my_string.replace('dog','cat')` to replace all occurrence of `'dog'` in my_string to `'cat'`.

As an exercise, assign the value of the position of `'dog'` in the given `long_string` to the variable `position_of_word`. Secondly, replace it with a `'cat'` and assign it to variable `replaced_long_string`.

~~~python
long_string = 'Whenever i get home, i will always go and find my dog first'
position_of_word = long_string.find('dog') #replace with your answer
replaced_long_string = long_string.replace('dog','cat')
~~~

### Question 8: Comparing strings
You can compare strings in python using the comparison operator `======`. For example, ``'This is one string' == 'This is one string'`` will return `True`.

As an exercise, compare the string in `string_a` with `string_b` and assign the value to `comparison_result`.

Note: Do not mix it up with the assignment operator `=`.

~~~python
string_a = 'I love strings!'
string_b = 'I love strings!'
comparison_result = string_a == string_b
~~~

### Question 9: Using the math module
Python comes with a module called math that can help you perform many different kinds of math function. You can type
`import math`
`help(math)`
in IDLE to find out what other functions are provided. 

The cosine function is provided in the module. To use the cosine function, you will need to precede the function with the module name. For example, `math.cos(45)`

As an exercise, assign a value to `area_of_circle` such that it computes the area of a circle using radius

~~~python
import math

radius = 3
area_of_circle = 3 ** 2 * math.pi
~~~
