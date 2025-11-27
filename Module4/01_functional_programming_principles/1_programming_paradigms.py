"""
Programming paradigms are different styles or approaches to writing programs.

1️⃣ Imperative Paradigm
the imperative paradigm tells the computer exactly what to do and how to do it.

a. Procedural Language
Example: Pascal
Breaks programs into procedures/functions
lot of repitition of code, no loops

b. Structured Language 
Example: C
Enforces structured control flow:
→ goto, loops & conditionals
structures, functions and loops
Makes code easier to read, debug, and maintain

c. Object-Oriented Language (OOP)

Example: Java, Python, C++

Organizes code around objects and classes 
brings it closer to make real world apps

2️⃣ Declarative Paradigm

Declarative programming expresses logic without describing the steps.

a. Database Query Languages
Example: SQL
You write what data you want, not how to retrieve it

b)Functional Paradigm
Programs are built using pure mathematical functions.
Examples: Haskell
-----------------------
A pure function is a function that always meets two rules:

1️⃣ Same input → Same output
A pure function always returns the exact same result when called with the same arguments.
2️⃣ No Side Effects
A pure function does NOT change anything outside itself.

----------------
let x = 10;
function increment() {
  x = x + 1;     // modifies global state → impure
  return x;
}
----------
Example (pure —  no side effects):

function increment(x) {
  return x + 1;
}

with python we can use procedural form, functional form, oop and functional form too.
"""