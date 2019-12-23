---
title: "Emergence"
tags:
  - clean
categories:
  - clean code
excerpt: "Rules for writing clean code"
last_modified_at: 2019-12-23T10:13:25.687266
---
## Emergence
### Getting Clean via Emergent Design
Simple code is
* Can run all tests
* Contains no duplication
* Expresses intent of programmer
* Minimize number of classes and methods

### Run all the tests
Verifiable behaviors are important.
* Easier to test SRP classes. They are smaller.
* Tight coupling makes it difficult to write tests.
* DIP. DI, interfaces and abstraction minimize coupling

### Refactoring
Incrementally refactoring code.
Question is did anything degrade?
	* Necessary to clean up code and run tests to verify they haven't break anything. 
* Increase cohesion. (Relationship elements in a system belongs there)
* Modularize system concerns. 
* Shrink functions, ensure expressiveness.

### No duplication
Reduce small amount of duplication.

If code starts looking like it doesn't relate to the responsibility of the class, should be moved to another class.

* Template pattern can be used to remove duplication.

### Expressive
Cost of system is in long term maintenance. 
* Choosing good names
* Keep functions small
* Using standard nomenclature can describe patterns to other developers.
* Well written unit tests are expressive
	* Reading tests can help us understand what a class is about. 

### Minimal Classes and Methods 
* Keep method and classes to the minimal.
* Creating an interface for every class is bad. Creates useless code 
* Relatively low priority compared to the other methods.
