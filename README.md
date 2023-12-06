# Design Patterns: Abstract Factory

### 1. Quick idea about this pattern/Problem which this pattern solve?
Abstract Factory is a creation design pattern that lets you produce families of related objects without specifying their concrete classes.

This pattern solve problem such as: When you need a way to create individual objects so that they match other objects of the same family.
### 2. Where should we use this pattern (examples)?
When we have several variants of some product.
### 3. Pros and Cons
Pros:
- You can be sure that the products you’re getting from a factory are compatible with each other.
- You avoid tight coupling between concrete products and client code.
- You can extract the product creation code into one place, making the code easier to support.
- You can introduce new variants of products without breaking existing client code.

Cons:
- The code may become more complicated than it should be, since a lot of new interfaces and classes are introduced along with the pattern.
