# Python - Async

## Async and Await Syntax

In Python, `async` and `await` are used to define and work with asynchronous functions. An asynchronous function is defined using the `async def` syntax, and within this function, you can use the `await` keyword to call other asynchronous functions.

```python
import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

# Running the async function
asyncio.run(say_hello())
```

## How to Execute an Async Program with asyncio

To execute an async program, you use the `asyncio.run()` function, which runs the passed coroutine and manages the event loop for you.

```python
async def main():
    print("Executing async program")
    await asyncio.sleep(1)
    print("Done")

# Running the async program
asyncio.run(main())
```

## How to Run Concurrent Coroutines

You can run multiple coroutines concurrently using `asyncio.gather()`. This function takes multiple coroutines and runs them concurrently.

```python
async def task1():
    await asyncio.sleep(1)
    print("Task 1 completed")

async def task2():
    await asyncio.sleep(2)
    print("Task 2 completed")

async def main():
    await asyncio.gather(task1(), task2())

# Running the concurrent coroutines
asyncio.run(main())
```

## How to Create asyncio Tasks

`asyncio.create_task()` is used to schedule the execution of a coroutine. This allows you to run multiple coroutines concurrently.

```python
async def task1():
    await asyncio.sleep(1)
    print("Task 1 completed")

async def task2():
    await asyncio.sleep(2)
    print("Task 2 completed")

async def main():
    task1_obj = asyncio.create_task(task1())
    task2_obj = asyncio.create_task(task2())
    await task1_obj
    await task2_obj

# Creating and running asyncio tasks
asyncio.run(main())
```

## How to Use the Random Module

The `random` module can be used within async functions to introduce randomness. For example, you can use `random.randint()` to generate random integers.

```python
import asyncio
import random

async def random_sleep():
    sleep_time = random.randint(1, 5)
    await asyncio.sleep(sleep_time)
    print(f"Slept for {sleep_time} seconds")

async def main():
    await random_sleep()

# Using the random module in async functions
asyncio.run(main())
```
