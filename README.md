# calculator
![](https://img.shields.io/badge/python-v3.7-informational?style=flat&logo=<LOGO_NAME>&logoColor=white&color=blue)

The following has been made for educational purposes as part of the final project of 2.1.5, "Software Engineering and Reproducible Research" on Turing College. It is meant to serve as a toy-example of making a package that can be later installed using `pip`. Standard package structure has been adapted and initialized.  

1. [Introduction](#Introduction)
2. [Installation](#Installation)
3. [Methods](#Methods)
   * [Addition](#Addition)
   * [Subtraction](#Subtraction)
   * [Multiplication](#Multiplication)
   * [Division](#Division)
   * [Square root](#Square-root)
   * [Memory reset](#Memory-reset)
4. [License](#License)
5. [Contact](#Contact)

<sub><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></sub>


## Introduction
> A **mechanical calculator**, or calculating machine, is a mechanical device used to perform the basic operations of arithmetic automatically [...] 
> The first mechanical calculator (also known as *Pascaline*) appeared in 1642, the creation of French intellectual Blaise Pascal as "a device that will eventually perform all four arithmetic operations without relying on human intelligence."
 
350 years later (the number has been arrived at while relying on human intelligence), the idea of calculator is still inconceivable without the original four operations - addition, subtraction, multiplication, and division. This is exemplified by the code that you will find here - an object `calculator`, which, in addition, is also able to take the square root of a number.

## Installation
In order to use the package, go through the two-step process:
1. To install the package directly from GitHub using `pip`, use the following:
```python
pip install git+https://github.com/virbickt/calculator.git
```
2. Once the package has been successfully installed, make sure to include the import statement:
```python
from calculator import Calculator
```
## Methods
### Addition
Addition is performed by using `calculator.add()`. It takes inputs of type float and returns the result of adding the input value to the value stored in the memory state:
```python
calculator = Calculator()
calculator.add(2.0)
# output: 2.0
```

### Subtraction
Subtraction is performed by using `calculator.subtract()`. It takes inputs of type float and returns the result of subtracting the input value from the value stored in the memory state:
```python
# assuming that the memory state equals 7

calculator.subtract(5.0)
# output: 2.0
```

### Multiplication
Multiplication is performed by using `calculator.multiply()`. It takes inputs of type float and returns the result of multiplying the input value to the value stored in the memory state:
```python
# Assuming that the memory state equals 2

calculator.multiply(3.0)
# output: 6.0
```

### Division
Division is performed by using `calculator.divide()`. It takes inputs of type float and returns the result of multiplying the input value to the value stored in the memory state:
```python
# assuming that the memory state equals 6

calculator.divide(3.0)
# output: 2.0
```

### Square root
The operation of taking square root is performed by using `calculator.sqrt()`. It takes no inputs and returns the result of taking the square root of the value stored in the memory state:
```python
# assuming that the memory state equals 4

calculator.sqrt()
# output: 2.0
```
`calculator.sqrt()` uses `math.sqrt` as it has been found to be quicker than the alternative such as `pow()` or `**0.5`
### Memory reset
Memory can be reset by using `calculator.reset()`. It takes no inputs and sets the value stored in the memory state to `0`:
```python
calculator.reset()
```
## License
The project is licenced under [GNU General Public License v3.0](https://github.com/virbickt/calculator/blob/main/LICENSE.md)

## Contact
Feedback is very welcome! Drop me an email: [tvirbickas@gmail.com](mailto:tvirbickas@gmail.com?subject=Calculator%20on%20Github)
