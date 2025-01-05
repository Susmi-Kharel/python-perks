# Chapter 15: Advanced Type Hinting using `Typing` module

**Table of contents**:
- [Chapter 15: Advanced Type Hinting using `Typing` module](#chapter-15-advanced-type-hinting-using-typing-module)
  - [Introduction to type hinting](#introduction-to-type-hinting)
  - [Type hinting variables for multiple data types.](#type-hinting-variables-for-multiple-data-types)
  - [Type hinting functions](#type-hinting-functions)


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


## Type hinting functions

Function can also be hinted using `:` notation for parameters and `->` for the
return type. An example of function with type hinting is as follows:

```python
def add(a: int, b:int)->int:
  return a + b
```
