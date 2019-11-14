---
title: "LiveData with Coroutines and Flow"
categories:
  - android
tags:
  - architecture
  - android
excerpt: "Practice of introducing reactive structures into Kotlin co-routines"
last_modified_at: 2019-10-24T18:07:22+0000
---

ViewModels shouldn't have a reference to the view.

The problem is when do you choose your scope? When does the operation cancel?

	* Activity onStop
	* ViewModel onCleared()

In a real world application,  the problem becomes exponeniated because you have more scopes from more screens.

* Application scope
* Navigation component scope

## Coroutines

Structure for Concurrency

#### Problems that are solved

* get off main thread
* no boilerplate 
* ***structured concurrency***
  * viewModelScope
  * lifecycleScope
  * launchWhenResume()`

#### Application Scope

​	if the work needs to complete, use WorkManager

Scope for livedata. (work is disposed)

```kotlin
val result = liveData {
  emit(doComputation())
}
```

## Cancelling coroutines

```kotlin
suspend fun printPrimes() {
  suspend... 
} 
```

ends with scope, 



#### One shot vs multiple shot

For example, one shot

	* profile picture
	* tweets

multiple shot

* likes (observable source)
* flow. livedata is not a reactive source.

flow + livedata to handle functional paridigms.
