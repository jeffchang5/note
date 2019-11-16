---
title: "Error Handling"
tags:
  - errors
categories:
  - clean code
excerpt: "Best practices of where and how to handle errors."
last_modified_at: 2019-11-12T10:27:12.377727
---

## Error Handling

	Responsible for what code needs to do. 
	
* Many code bases are dominated by scattered error handling 
* Use exceptions, not return codes
* throw exception at callers and handle immediately.

### When developing code, write try - catch - finally first.
* Catch blocks must leave state consistent.
* change implementation to access an invalid file.

### Use TDD to build rest of the logic that's needed.
* change implementation to fit test. 
* write new tests to test different exceptions.
* Checked exceptions can violate open and closed principles. Try-catches can happen three layers above the current code so there may be need to handle all of these cases - knowing details about higher layers of abstraction.
* Creative exceptions have useful information to recreate the error.

### Define exception classes in caller needs
* biggest concern is how they are caught
* wrapping third party libraries can be useful. Reduces dependencies on this library.
* aren't tied to vendor's design choices.
* often times, one exception per class is fine. 

#### Define the normal flow.
* Special UseCase that returns a special circumstances.
* Class can return an object that handles the special case 

```java
public class PerDiemMealExpenses implements MealExpenses { 
	public int getTotal() {
		// return the per diem default }
	}
} 
```

### Don't return null
* avoid null when possible.
* type checking for null is not there in standard Java.

### Conclusion 
* Error handling can be out of the main flow of our logic and be reasoned independently.
