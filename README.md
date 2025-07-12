# Spell Checker

A simple spell checker library built following SOLID principles.

## Installation

To install the package, run the following command:

```bash
pip install -e .
```

## Usage

To run the example script, use the following command:

```bash
python3 spell_checker/app/main.py
```

## SOLID Principles

This project is designed to demonstrate the application of SOLID principles in a real-world scenario. Each principle is explained below, with a reference to how it's implemented in the codebase.

### Single Responsibility Principle (SRP)

The Single Responsibility Principle states that a class should have only one reason to change. In our spell checker, this is achieved by separating the core components into distinct classes:

*   **`Vocabulary`**: Responsible for managing the set of known words.
*   **`DistanceMetric`**: Responsible for calculating the distance between two words.
*   **`SpellChecker`**: Responsible for the main spell-checking logic, using a vocabulary and a distance metric.

Each class has a single, well-defined responsibility, making the code easier to understand, maintain, and test.

### Open/Closed Principle (OCP)

The Open/Closed Principle states that software entities (classes, modules, functions, etc.) should be open for extension but closed for modification. We achieve this by using abstract base classes (`Vocabulary` and `DistanceMetric`) as contracts.

*   If we want to add a new way of loading a vocabulary (e.g., from a file), we can create a new class that inherits from `Vocabulary` without modifying the existing `SimpleVocabulary` or the `SpellChecker` class.
*   Similarly, if we want to use a different distance metric (e.g., Jaro-Winkler), we can create a new class that inherits from `DistanceMetric` without changing the `SpellChecker` class.

This makes the system extensible without altering the existing, tested code.

### Liskov Substitution Principle (LSP)

The Liskov Substitution Principle states that objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program. Our design adheres to this principle by ensuring that any subclass of `Vocabulary` or `DistanceMetric` can be used by the `SpellChecker` class without issues.

For example, the `SpellChecker` class expects any `Vocabulary` object to have a `__contains__` method and a `get_words` method. As long as our subclasses implement these methods correctly, they can be substituted for one another.

### Interface Segregation Principle (ISP)

The Interface Segregation Principle states that no client should be forced to depend on methods it does not use. We follow this principle by keeping our interfaces small and focused.

*   The `Vocabulary` interface only has the methods necessary for a vocabulary.
*   The `DistanceMetric` interface only has the methods necessary for a distance metric.

This prevents classes from depending on methods they don't need, which reduces coupling and makes the system more robust.

### Dependency Inversion Principle (DIP)

The Dependency Inversion Principle states that high-level modules should not depend on low-level modules; both should depend on abstractions. Our `SpellChecker` class (the high-level module) does not depend on the concrete `SimpleVocabulary` or `EditDistance` classes (the low-level modules). Instead, it depends on the `Vocabulary` and `DistanceMetric` abstractions.

This inversion of dependencies, facilitated by dependency injection in the `SpellChecker`'s constructor, makes the system more flexible and easier to test. We can easily swap out the implementations of the vocabulary or distance metric without changing the `SpellChecker` class.
