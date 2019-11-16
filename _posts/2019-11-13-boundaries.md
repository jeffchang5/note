---
title: "Boundaries"
tags:
  - software
categories:
  - clean code
excerpt: "Where to separate your code and different unknowns."
last_modified_at: 2019-11-13T10:44:03.734146
---

## Boundaries
Tension between interface and users of interface.

Users want an interface that is focused on their particular needs.
* interfaces may do too much or too little
* don't pass maps around too much. Keep it inside a class with closed implementation details.

### Third Party Code 
* Write tests to learn the API.
* Focus on understanding the API through what we want from it.
* Tests can determine behavioral differences.

	New code comes new risk - tests help mitigate this risk
	
### Using code that does not exist yet.
Working with teams that don't define the interface. 
* Can create and define your own interface.
* Can create abstractions that depends on adapters that define the interaction with an API.

Avoid code that knows too much about the third party.

	
	


