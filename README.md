Hello everyone!

Here you'll find the code we worked with at Tinker Lab. There will be a folder for each week and inside that we'll have the lesson code along with any extras for those that might want to go further.

Extra challenges will be detailed within each folder and I will include a `challenge-x-solution.py` file for each one so you can see how I would have done it.

Remember a few things:

- Comments begin with a `#`, they are there to help explain the code.
- Indentation is important, and is a common gotcha. An example of good vs bad indentation is detailed below. You can indent code with tabs.
- Variable and function names must all be one word and can only include letters, numbers, and underscores.

## Indentation

Python is particularly fussy about how we indent our code. Here are some examples:

```python
#--------- GOOD -----------

# notice this has no indentation
MY_NAME = 'Matt'

# Note that the function definition here starts without any indentation
# but the code within it is indented one space
def my_function():
  some_method()
  some_method_again()

# This code has no indentation, so it is not part of the function above
some_method()

#--------- BAD -----------

# This variable is indented
  MY_NAME = 'Matt'

def my_function():
# This line should be indented, but it's not
some_method()
```
