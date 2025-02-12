# `python-perks` (Python Notes)

**_`python-perks` is a repository for Python course notes, examples, and lab exercises targeted to students, professionals, and enthusiasts._**

This repository is intended to provide you a quick guide to starting your
journey as a python programmer.

> You are advised to **fork** this repository and solve problems as you proceed
> to different levels while still being able to sync with the new changes in the
> repository.

## Course Contents

###  Algorithms
**NOTE**:
_If you are an absolute beginner in python, please check_
_[**Notes section**](#notes) first to get started with python._

- [Algorithms](algorithms/README.md)
  - Searching Algorithms
    - [Linear Search](algorithms/searching/linear_search.py)
    - [Binary Search](algorithms/searching/binary_search.py)
  - Sorting Algorithms
    - [Bubble Sort](algorithms/sorting/bubble_sort.py)
    - [Insertion Sort](algorithms/sorting/insertion_sort.py)
    - [Quick Sort](algorithms/sorting/quick_sort.py)
    - [Selection Sort](algorithms/sorting/selection_sort.py)
- [Data Structures](data_structures/README.md)
  - [Linked List](data_structures/linked_list.py)
  - [Doubly Linked List](data_structures/doubly_linked_list.py)
  - [Binary Tree](data_structures/binary_tree.py)
  - [Queue](data_structures/queue.py)
  - [Stack](data_structures/stack.py)
- [Design Patterns](design_patterns/README.md)
  - [Adapter Pattern](design_patterns/adapter.py)
  - [Builder Pattern](design_patterns/builder.py)
  - [Command Pattern](design_patterns/command.py)
  - [Decorator Pattern](design_patterns/decorator.py)
  - [Factory Pattern](design_patterns/factory.py)
  - Observer Pattern
  - [Singleton Pattern](design_patterns/singleton.py)
  - Strategy Pattern

### [Problem Solving](problem_solving/README.md)

1. [Basic Problem Solving](problem_solving/basic/)
   1. [Practical Number Solution](problem_solving/basic/practical_number.py)
   2. Iteration with Comprehension
   3. [Greatest Common Divisor](problem_solving/basic/gcd.py)
   4. Matrix Multiplication
   5. Median Calculation
   6. [Reverse digits of an integer](problem_solving/basic/reverse_digits.py)

2. [Dynamic Programming](problem_solving/dp/)
   1. Coin Change Problem
   2. Fibonacci Series Problem
   3. Palindrome Partition Problem
   4. Minimizing the sum of list of integers
   5. Longest Common Subsequence Problem

### Notes
_(Links will be updated accordingly)_

1. **[Fundamentals of Python](notes/c01_basics)**
    - [Introduction to Python](notes/c01_basics/Chapter-1.1-Basics.md)
    - [Python Environment Setup, IDE Setup](notes/c01_basics/Chapter-1.1-Basics.md#installing-python)
    - [Hello World in Python](notes/c01_basics/Chapter-1.1-Basics.md#hello-world-with-idle)
    - [Running Python Programs](notes/c01_basics/Chapter-1.1-Basics.md#creating-editing-and-running-python-files)
    - comments and documentation
        - Single Line Comments
        - inline Comments
        - Multiline Comments
        - Docstrings
    - indentation
    - [Chapter 1 Quiz](notes/c01_basics/quiz)

2. **[Variables, basic data type and operations](notes/c02_basic_data_types)**
    - [Variables, constants, and keywords](notes/c02_basic_data_types/Chapter%202.1%20Variables.md)
    - [Numeric Data Types](notes/c02_basic_data_types/Chapter%202.2%20Numeric%20Data%20Types.md)
    - [Strings](notes/c02_basic_data_types/Chapter%202.3%20Strings.md)
    - [String Formatting](notes/c02_basic_data_types/Chapter%202.4%20string%20formatting.md)
    - [Basic Operations](notes/c02_basic_data_types/Chapter%202.5%20Operations.md)
    - Type Hinting in Python (only for python 3.6 and later)
    - [Type Conversion / Typecasting](notes/c02_basic_data_types/Chapter%202.6%20Typecasting.md)
    - [Chapter 2 Quiz](notes/c02_basic_data_types/quiz)

3. **[Advanced Data Types](notes/c03_advanced_data_types)**
    - [List](notes/c03_advanced_data_types/chapter%203.1%20list.md)
    - [Tuple](notes/c03_advanced_data_types/chapter%203.2%20tuple.md)
    - [Dictionary](notes/c03_advanced_data_types/chapter%203.3%20dictionary.md)
    - [Set](notes/c03_advanced_data_types/chapter%203.4%20set.md)
    - [Chapter 3 Quiz](notes/c03_advanced_data_types/quiz)

4. **[Decision Making](notes/c04_decision_making)**
    - [`if` condition](notes/c04_decision_making/README.md#the-if-condition)
    - [`if`-`else` condition](notes/c04_decision_making/README.md#the-if-else-condition)
    - [`if`-`elif`-`else` conditions](notes/c04_decision_making/README.md#the-if-elif-else-condition)
    - [the `match` condition](notes/c04_decision_making/README.md#the-match-condtion)
    - [ternary operators](notes/c04_decision_making/README.md#ternary-operators)
    - [Nested conditions](notes/c04_decision_making/README.md#nested-conditions)
    - [Chapter 4 Quiz](notes/c04_decision_making/quiz)

5. **[Loops, Pattern Generation, and Comprehension](notes/c05_loops)**
    - [While Loop](notes/c05_loops/Chapter%205.1%20while%20loop.md)
        - [The `break` and the `continue` statement](notes/c05_loops/Chapter%205.1%20while%20loop.md#the-break-and-the-continue-statement)
        - [`while`-`else`](notes/c05_loops/Chapter%205.1%20while%20loop.md#while-else)
        - [Nested `while` loop](notes/c05_loops/Chapter%205.1%20while%20loop.md#nested-while-loop)
    - [For Loop](notes/c05_loops/Chapter%205.2%20for%20loop.md)
        - [the `enumerate()` function](notes/c05_loops/Chapter%205.2%20for%20loop.md#the-enumerate-function)
        - [the `zip()` function](notes/c05_loops/Chapter%205.2%20for%20loop.md#the-zip-function)
    - [Pattern Generation](notes/c05_loops/Chapter%205.3%20Pattern%20Generation.md)
    - [Comprehensions](notes/c05_loops/Chapter%205.4%20Comprehensions.md)
    - [Chapter 5 Quiz](notes/c05_loops/quiz)

6. **[Functions](notes/c06_functions)**
    - [Introduction to Functions](notes/c06_functions/Chapter%206.1%20function.md)
        - Defining a function
        - Calling a function
        - the `return` statement
        - the `pass` statement
        - Local Variables and Global variables
    - [default arguments](notes/c06_functions/Chapter%206.2%20default%20arguments.md)
    - [arguments and keyword arguments](notes/c06_functions/Chapter%206.3%20args%20kwargs.md)
    - [Recursive Functions](notes/c06_functions/Chapter%206.4%20recursive%20functions.md)
    - [Lambda functions](notes/c06_functions/Chapter%206.5%20lambda.md)
    - [Chapter 6 Quiz](notes/c06_functions/quiz)

7. **[Classes](notes/c07_oop)**
    - [Introduction to Object-Oriented Programming](notes/c07_oop/Chapter-7.1-oop.md#introduction-to-oop)
        - Class
        - Class attributes, methods, and the `self` parameter
        - the Constructor method
        - built-in class attributes
        - object
    - [Class methods and Static methods](notes/c07_oop/Chapter-7.2-Class-Methods-and-Static-Methods.md)
    - [Operator Overloading](notes/c07_oop/Chapter-7.3-Operator-Overloading.md)
      -[Encapsulation in python](notes/c07_oop/Chapter-7.4-Encapsulation.md)
        - [getters and setters](notes/c07_oop/Chapter-7.4-Encapsulation.md#getter-and-setter-methods)
        - [The `@property` Decorator](notes/c07_oop/Chapter-7.4-Encapsulation.md#the-property-decorator)
    - [Inheritance and Polymorphism](notes/c07_oop/Chapter-7.5-Inheritance-and-Polymorphism.md)
        - Parent Class
        - Child Class
        - `super()` function
        - Mixins
    - [Chapter 7 Quiz](notes/c07_oop/quiz)

8. **[Python Modules and packages](note/c08_modules_packages)**
    - [Modules](notes/c08_modules_packages/chapter-8.1-modules.md)
    - [Packages](notes/c08_modules_packages/chapter-8.2-packages.md)
    - [The `datetime` module](notes/c08_modules_packages/chapter-8.3-datetime.md)
    - [The `random` module](notes/c08_modules_packages/chapter-8.4-random.md)
    - [The `json` module](notes/c08_modules_packages/chapter-8.5-json.md)
    - [The `math` module](notes/c08_modules_packages/chapter-8.6-math.md)
    - [The `complex` and `cmath` module](notes/c08_modules_packages/chapter-8.7-complex-and-cmath.md)

9. **[File I/O](notes/c09_file)**
    - `open()` function
    - `close()` method
    - `write()` method
    - `read()` method
    - `with` keyword

10. **[Exceptions and Exception Handling](notes/c10_exceptions/README.md)**
    - [Introduction to Exceptions](notes/c10_exceptions/chapter-10.1-exceptions.md)
    - [Exception Handling in Python](notes/c10_exceptions/chapter-10.2-exception-handling.md)
      - Standard Errors
      - `try`, `except` keyword
      - `try` `except` `else`
      - `finally` keyword
      - `raise` keyword
    - [Custom Exceptions](notes/c10_exceptions/chapter-10.3-custom-exceptions.md)
    - Total

11. **[Python Package Management with PIP](notes/c11_pip)**
    - [Introduction to Semantic Versioning](notes/c11_pip/chapter-11.1-semver.md)
    - [PIP and its usage](notes/c11_pip/chapter-11.2-pip.md)

12. **[Virtual Environments](notes/c12_virtual_environment)**
    - [Introduction to virtual environments](notes/c12_virtual_environment/chapter-12.1-virtual-environment-intro.md)
    - [VENV and its usage](notes/c12_virtual_environment/chapter-12.2-venv.md)
    - [PIPENV and its usage](notes/c12_virtual_environment/chapter-12.3-pipenv.md)
    - [Poetry Package manager](notes/c12_virtual_environment/chapter-12.4-poetry.md)

13. **[Python Advanced Functions](notes/c13_advanced_functions)**
    - [`groupby()` function](notes/c13_advanced_functions/chapter-13.1-groupby.md)
    - [`sorted()` function](notes/c13_advanced_functions/chapter-13.2-sorted.md)
    - [`filter()` function](notes/c13_advanced_functions/chapter-13.3-filter.md)
    - [`map()` function](notes/c13_advanced_functions/chapter-13.4-map.md)
    - [`reduce()` function](notes/c13_advanced_functions/chapter-13.5-reduce.md)

14. **[Regular Expressions (REGEX)](notes/c14_regex)**
    - [Introduction to regular expressions](notes/c14_regex/chapter-14.1-regular-expressions.md)
    - [REGEX special characters](notes/c14_regex/chapter-14.2-regex-special-characters.md)
    - [The `re` module](notes/c14_regex/chapter-14.3-the-re-module.md)

15. [**Advanced Data Structures**](notes/c15_data_structures)
16. [**Decorators**](notes/c16_decorators)
17. [**Mixins**](notes/c17_mixins)
18. [**`http` module**](notes/c18_python_http)
19. [**`requests` library**](notes/c19_requests)
20. [**Advanced Type hinting**](notes/c20_advanced_type_hinting)
21. **[Software Testing](notes/c21_testing/)**
    - [21.1: Introduction to Software Testing](./notes/c21_testing/chapter-21.1-intro.md)
    - [21.2: Testing using `unittest` module](./notes/c21_testing/chapter-21.2-unittest.md)
    - [21.3: The `pytest` Package](./notes/c21_testing/chapter-21.3-pytest.md)


## Folder Structure

The repository has its folder structure as shown in example below:

```
notes
├── README.md
├── c01_basics
│   ├── Chapter 1 Basics.md
│   ├── README.md
│   ├── code
│   │   ├── c0101_hello_world.py
│   │   └── c0102_comments.py
│   └── quiz
│       ├── README.md
│       └── solution
│           ├── q0101.py
│           └── q0102.py
├── c02_...
├── c03_...
│
```

> If you're directly **cloning** the repository, I suggest you to solve in the
> different branch than the `main` branch to avoid conflicts if the course
> content changes.
>
> If you're **forking**, I suggest you not to make any changes in the `main`
> branch in your repository too so that you can pull and rebase future changes
> to your `fork`.

## Pulling future changes for your forks

for pulling the future changes you can add new `remote` as upstream in your
local repository with the commands below:

```shell
# step 1: add the upstream remote as git@github.com:ghimiresdp/python-perks.git
# step 2: pull from the upstream
# step 3: push to the origin

git remote add upstream git@github.com:ghimiresdp/python-perks.git
git pull upstream main
git push origin main
```
