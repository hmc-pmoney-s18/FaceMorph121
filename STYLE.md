# Code Style
## General Format Checking

we run `pylint` to run our python file before every commit to github. Therefore most of python code conforms to the pylint python style rules. Those rules can be read at https://www.python.org/dev/peps/pep-0008/#tabs-or-spaces. For example, pylint allowed us to implement the following style rules:
* Checking the length of each line making sure it is less than 72 characters.
* Checking that variable names are well-formed according to the project's to the snake_case naming convention.
* Checking that declared interfaces are truly implemented
* Checking the trail whitespace
* Checking the number of declared variables making sure they are less than 21

## Python
These are specific rules we applied to our code base:
There should be a two lines space between different functions.

We limit the numbers of local variables per function to 21.

We use 4 spaces as a way of spacing instead of tabs.

When a line gets too long, we break it into two lines after an operation sign.

### Comments
* Start the sentence with a capital letter
* Not end-of-line comment. The comment should be written on the line immediately above the code which it refers to. If explaining a long block of code, the comment can be converted into multiple lines.
For example:
```
# Convert Mat to float data type
    image_1 = np.float32(img_1)
    image_2 = np.float32(img_2)
```

### Naming Convention:
* `snake_case` for Python & `SCREAMING_SNAKE_CASE` for global constants
* Create the variable name as meaningful as possible to reflect the purpose it serves within a function 
and within the scope of the project

### Function Convention:
* Each function should have a good docstrings, which describe the functionality, input, and output parameters. 
* Each line of the doctstring should not be too long and follow the length requirement from pylint.

For example:
```
def foo(x,y):
  """ Describing the input parameter first. 
      Then talking about the functionality.
      Then describing the return.
  """
  code begins
```

## Html
* Two line spaces between `section`.
* One line spaces between  block of `div`
* Putting a `<-- Comment -->` a line above the start of each section
* Input css file first, content second, and javascript at the end

For example:
```
<!DOCTYPE html>
<html lang="en">

<head>

  <title>FaceMorph</title>
  
  ...
<\head>


<-- Section Name -->
  <section ...>
    <div>
      ...
    <\div>
    
    <div>
      ...
    <\div>
  <\section>

...

```
