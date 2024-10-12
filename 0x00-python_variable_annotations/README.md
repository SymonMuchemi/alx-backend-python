# Python Variable Annotations

## Type Annotations in Python 3

Type annotations in Python 3 allow you to explicitly declare the data types of variables, function parameters, and return values. This helps improve code readability and maintainability.

## Using Type Annotations to Specify Function Signatures and Variable Types

You can use type annotations to specify the expected data types for function parameters and return types. For example:

```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

You can also annotate variables:

```python
age: int = 25
```

## Duck Typing

Duck typing is a concept where the type or the class of an object is less important than the methods it defines. If an object implements the required methods, it can be used in place of another object with the same method signatures.

## Validating Your Code with mypy

`mypy` is a static type checker for Python. It checks your code for type consistency and helps catch type-related errors. You can run `mypy` on your codebase to ensure that your type annotations are being followed correctly.

```sh
mypy your_script.py
```
