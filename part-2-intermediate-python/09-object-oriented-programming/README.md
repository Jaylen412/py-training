# Module 09: Object-Oriented Programming

Bundle data and behaviour into classes. You will define classes with attributes and methods, make them work with Python's built-in operations, build families of classes with inheritance and combine objects with composition, write data classes and properties, and finish by building models with the `fit`/`predict` interface that scikit-learn uses.

**Prerequisites:** Part 1 and Module 08.

## Lessons

1. [09-01 Classes and instances](09-01-classes-and-instances/lesson.md)
2. [09-02 Special methods](09-02-special-methods/lesson.md)
3. [09-03 Inheritance and composition](09-03-inheritance-and-composition/lesson.md)
4. [09-04 Dataclasses and properties](09-04-dataclasses-and-properties/lesson.md)
5. [09-05 The estimator pattern](09-05-the-estimator-pattern/lesson.md)

## Checkpoint quiz

1. What is `self`, and why does every method list it first?
2. Which special method does `print(obj)` use, and which does `[obj]` use when printed?
3. Should a `Car` class inherit from `Engine`? Why or why not?
4. Why is `area` better as a `@property` than as an attribute set in `__init__`?
5. In the estimator pattern, what goes in `__init__`, what goes in `fit`, and what does a trailing underscore on an attribute mean?

<details>
<summary>Answers</summary>

1. The instance the method is working on. Python passes it automatically when you call `obj.method()`, so the method needs a parameter to receive it.
2. `print(obj)` uses `__str__` (falling back to `__repr__`); a list shows its items with `__repr__`.
3. No. A car is not a kind of engine; it has an engine. Use composition: store an `Engine` as an attribute of `Car`.
4. A property is recalculated whenever it is read, so it stays correct when `width` or `height` change; a stored attribute would go out of date.
5. `__init__` stores hyperparameters only; `fit` learns from data and stores the results. A trailing underscore marks an attribute learned during `fit`.

</details>
