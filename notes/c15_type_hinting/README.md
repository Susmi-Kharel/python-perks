# Chapter 15: Advanced Type Hinting using `Typing` module

**Table of contents**:
- [Chapter 15: Advanced Type Hinting using `Typing` module](#chapter-15-advanced-type-hinting-using-typing-module)
  - [Introduction to type hinting](#introduction-to-type-hinting)
  - [Type hinting variables for multiple data types.](#type-hinting-variables-for-multiple-data-types)
  - [Type hinting in functions and methods](#type-hinting-in-functions-and-methods)
  - [Advanced Type hinting](#advanced-type-hinting)


## Introduction to type hinting

Type hinting was introduced in Python `3.5` with the aim of supporting type
checking while developing. Even though we hint types, it is not enforced by the
python runtime.

We can hint types on variables, functions, etc with different annotations. The
type hinting annotation of python is almost close to that of python. to hint
types of different objects, we need to know the class name for those variables
which are as follows:

- integer: `int`
- floating point numbers: `float`
- string: `str`
- list: `list`
- set: `set`
- dictionary: `dict`
- object: `object` or `<CUSTOM ClASSNAME>`

Consider a code snippet below:

```python
id = 1
name = 'John Doe'
subjects = ['Physics', 'Chemistry', 'Biology']
data = {
  'roll': 1,
  'age': 10,
  'grade': 5
}
```

 The code snippet above can be hinted using type hinging as follows:


```python
id: int = 1
name: str = 'John Doe'
subjects: list[str] = ['Physics', 'Chemistry', 'Biology']
data: dict[str, int] = {
  'roll': 1,
  'age': 10,
  'grade': 5
}
```

In the above example, writing `id: str = 1` would also compile without errors,
but modern IDEs and linters would leverage the type hint so that they could
perform static type checking ahead of hte compilation.


## Type hinting variables for multiple data types.

If we want to hint multiple data types or different data types on different
condition, we could leverage the use of the operational OR `|` operator to hint
the conditional data type.

for example:

```python

roll: int | str = 5
role = 'five'
```

in the above code snippet, the type of the identifier `roll` is defined as
`int | str` which shows that the identifier `roll` can be either `int` or
`string`


## Type hinting in functions and methods

Function type hinting includes hinting the data type of a parameter as well as
return type. parameter type hinting is same as identifier type hinting which
uses colon `:` annotation, whereas return type is hinted using
hyphen `-` followed by greater than sign `>` when combined looks like right
arrow `->`.

The example of function type hinting is as follows:

```python
def distance(a: int, b:int)->int:
  return a + b
```

## Advanced Type hinting

[REF: <https://docs.python.org/3/library/typing.html>]

We can also hint types for advanced data types such as lists, sets, etc. which
may contain multiple data types inside of them. For example a list might contain
`str`, `int`, `float`, or even `List` itself. We can hint those types using
`Union` from `Typing` library or `|` opetator on newer version of python.

In older versions of python (`3.5` - `3.9`), we had to import types for complex
types such as `List`, `Dict`, etc. when we had to provide data type of such
compound data types. example `List[str]`.

Example:

```python
from typing import List, Literal, TypedDict, Union
my_list: List[Union[int, str]] = ["John", "Jane", 2]

class User(TypedDict):
    id: int
    name: str
    type: Literal["admin", "staff"]

```

In newer versions of python (`Python >= 3.10`) more type hints and operators are
available in the standard library. Because of which our code is even more
readable.

For example, instead of importing `List`, we have `list` type than can be used
to hint advanced list type. Another example is the use of Pipe `|` Operator
instead of `Union` type. So, the type `Union[str, int]` can be replaced by
`str | int`.

However completely avoiding the `typing` module is still not possible for some
data types such as `Literal` or `TypedDict`.

Example:
```python
from typing import Literal, TypedDict

# my_list: List[Union[int, str]] = ["John", "Jane", 2]
my_list: list[int | str] = ["John", "Jane", 2]

```
