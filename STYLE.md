# Code Style
## General Format Checking

we run `pylint` to run our python file before commit to github. This allows us to check our code style on python. This allow us to do following features:
* Checking the length of each line
* Checking that variable names are well-formed according to the project's coding standard
* Checking that declared interfaces are truly implemented
* Checking the trail whitespace

## Python

There should be a two lines space between different functions.

Limiting the numbers of local variables per function to 21.

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
* Create the variable name as meaningful as possible

### Function Convention:
* Each function should have a good doctrine, which describes the functionality and input parameter and output type. 
* Each line of the doctrine should not be too long and follow the length requirement from pylint.

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
* Putting a `<-- Comment -->` a line above section start
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
