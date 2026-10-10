# Programming Practice

A collection of small projects and exercises I'm using to strengthen my programming fundamentals, problem-solving skills, and software development practices.

## Projects

### 📦 Package Shipping System

A Python practice project built using Test-Driven Development (TDD).

The project models different package types and their shipping behavior while practicing object-oriented programming concepts.

#### Concepts Practiced

- Test-Driven Development (Red → Green → Refactor)
- Python `unittest`
- Arrange-Act-Assert (AAA)
- Test fixtures with `setUp()`
- Test helper methods
- `subTest()`
- Input validation and exception testing
- Object-Oriented Programming (OOP)
- Encapsulation and properties
- Inheritance
- Method overriding
- Polymorphism

#### Current Package Types

- `Package` - Base class containing shared package data and validation
- `StandardPackage` - Calculates standard shipping costs
- `ExpressPackage` - Calculates express shipping costs

#### Running the Tests

From the repository root:

```bash
cd package_project
python test_package.py
```

Current test suite: **9 passing tests**.

## Learning Approach

For new behavior, I practice the TDD cycle:

1. **RED** - Write a test describing the expected behavior.
2. **GREEN** - Write the minimum code necessary to make the test pass.
3. **REFACTOR** - Improve the code while keeping the tests passing.