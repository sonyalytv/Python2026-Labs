# Answers to Lab01

## Table of Contents
- [Task A](#task-a--binding-vs-rebinding)
- [Task B](#task-b--mutation-vs-rebinding)
- [Task C](#task-c--function-arguments-are-new-bindings)
- [Task D](#task-d--default-argument-trap)
- [Task E](#task-e--copy-semantics-shallow-vs-deep)
- [Task F](#task-f--reference-counting--gc-cpython)

## Task A $-$ Binding vs Rebinding
Why `b` **still refers to the old value after** `a = 4`?

In Python, names are bindings, they only refer to an object in memory. When we execute `b = a` we bind `b` to the same object `3`. Initial ids confirm that `a` and `b` refer to the same location in memory. When we perform rebinding `a = 4`, a new object `4` (with a new location) is created in memory and `a` now refers to it. However, it doesn't affect `b` and its corresponding object `3`. That's why after rebinding `a = 4` and still `b = 3`. We see that `id(a)` has changed and `id(b)` remains the same as before the operation.

## Task B $-$ Mutation vs Rebinding
Why both names see the change? What is the difference between **mutation** and **rebinding**?

* Both names refer to the same object (their ids are the same). When we change `b`, in fact, we change the **object** that it refers to. Here no rebinding happens, as no new object is created, but only the existing one is changed. As a result of mutation, ids do not change. Both `a` and `b` still refer to the same object, that's why both names see the change.
* Rebinding changes which object the name refers to, thus the id also changes. Mutation changes the object itself. All the names that refer to this object will see the change, and their ids will remain unchanged.

## Task C $-$ Function arguments are new bindings
Why mutation inside the function affects the caller? Why rebinding inside the function does **not** affect the caller?

* When an argument is passed to a function, we create a new local name as a parameter. The parameter binds to the same object that the argument refers to. That's why mutating the parameter affects the object itself and all the names that refer to it (including the caller). If we don't want the caller to be changed we need to make a copy of the object.
* When performing rebinding, a new object is created, and the parameter (which is a local name) starts referring to it, so it doesn't affect the initial object and, thus, the caller.

## Task D $-$ Default argument trap
Why does the list keep growing?

In Python default value is created only once when the function is defined and not before each call. That's why this value will refer to the same object in memory throughout the whole program. And when it is changed several times, we get the growing list.

## Task E $-$ Copy semantics (shallow vs deep)
What is the difference between shallow and deep copy?

The difference is noticeable when using nested objects. A nested list is an object in memory that stores references to its elements which are also objects in memory. When a shallow copy is created the list of references is copied to a new object in memory, but the references to the elements stay the same. So elements of `a` and `b` refer to the same objects, in fact. And when `b[0]` is changed, `a` also sees the change. In case of a deep copy, new copies are created for elements of all levels inside the nested object. So a deep copy will consist of other ids. That's why changing the deep copy doesn't affect the initial object.

## Task F $-$ Reference counting / GC (CPython)
Why do we get such an unexpected result for `42`?

It is caused by a CPython optimization. Some objects are very often referred to. That's why it is more effective (we avoid making update operations) to never change their reference counts, and never delete them. Their reference counts are immutable large numbers. However, the exact value may differ across different Python builds. Those objects are called immortal. They are often-used values: small integers, `None`, `True`, `False`, etc.