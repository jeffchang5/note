---
title: "Unit Testing"
tags:
  - testing
categories:
  - clean code
excerpt: "Best practices for writing unit tests"
last_modified_at: 2019-11-15T13:15:07.732526
---
## Unit Tests

### Test Driven Development 
**Before** : Adding ad hoc code to test code.
**After** : Make sure code tests every cranny. 

### Three Laws of TDD
1. Do not write production code unless you have set up an unit test.
2. Unit tests should not carry too much information.
3. May not write production code that passes the currently failing test.

Tests are written together with production code. Tests will cover all of production code eventually.

### Keeping Tests Clean
Tests should be the same quality as production code.

* Dirty tests may be worse than no worse tests
* Tests have to evolve as production code evolves.
* Tests will be harder to change if the tests are dirty.
* Without tests, the behavior begins to rot and making changes become much harder.
* It should be first class citizen
* With proper testing, code is more flexible.
* Poor testing means poor loss of flexibility

### Clean Tests
* Tests should be readable
* Avoid duplication of code.
* Tests should be free of tedious code that hide intent
* Create a language to test libraries and make readable of the details in your tests.
* Test details should be continuously refactored to hide implementation details.

### Dual standards
* efficiency is not as important compared to readability. Code is happening on local machine's JVM anyway. 

### Minimize number of asserts
* single reason for a test to fail

Write tests before designing code.

