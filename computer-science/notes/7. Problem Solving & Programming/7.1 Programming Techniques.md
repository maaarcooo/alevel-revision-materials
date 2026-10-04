# 7.1 Programming Techniques

## Data Types

A **data type** classifies data according to the kind of value it represents, determining how the computer stores and manipulates it.

| Data Type | Description | Examples |
|-----------|-------------|----------|
| **Integer** | Whole numbers, positive or negative | 10, -5, 0 |
| **Real** (float) | Numbers with a fractional part | 3.14, -2.5, 0.0 |
| **Char** | A single character (letter, digit, symbol) | 'a', 'B', '5', '$' |
| **String** | A sequence of characters | "Hello World", "1234" |
| **Boolean** | True or false values | True, False |

Choosing the correct data type ensures accuracy and efficiency in a program.

### Casting

**Casting** is converting one data type to another. User input is typically received as a string, so casting to a numerical type is often required before performing calculations or comparisons. For example, comparing whether `"12"` is less than `20` requires casting the string `"12"` to an integer first.

**Python:** `int("123")`, `float("3.14")`
**Java:** `Integer.parseInt("123")`, `Double.parseDouble("3.14")`

| Conversion | Example (Python) | Output |
|------------|-----------------|--------|
| Integer to Real | `float(5)` | 5.0 |
| Real to Integer | `int(5.7)` | 5 (truncated) |
| String to Integer | `int("10")` | 10 |
| Integer to String | `str(5)` | "5" |
| Boolean to String | `str(True)` | "True" |
| String to Boolean | `bool("True")` | True |

---

## Arithmetic, Logical and Boolean Operators

### Arithmetic Operators

| Operator | Symbol | Example | Result |
|----------|--------|---------|--------|
| Addition | `+` | `5 + 3` | 8 |
| Subtraction | `-` | `10 - 4` | 6 |
| Multiplication | `*` | `3 * 5` | 15 |
| Exponentiation | `^` | `3 ^ 3` | 27 |
| Division | `/` | `10 / 2` | 5 |
| Modulus | `MOD` | `10 MOD 3` | 1 |

The `+` operator also performs **string concatenation**: `'John' + ' ' + 'Doe'` produces `'John Doe'`.

**Operator precedence** follows BIDMAS/BODMAS. Parentheses override default precedence:

```
result = 2 + 3 * 4         // 14 (multiplication first)
adjustedResult = (2 + 3) * 4  // 20 (addition first)
```

### Comparison (Logical) Operators

Comparison operators compare two values and return a boolean result.

| Operator | Meaning | Example (`x=5, y=10`) | Result |
|----------|---------|----------------------|--------|
| `==` | Equal to | `x == y` | False |
| `!=` | Not equal to | `x != y` | True |
| `>` | Greater than | `x > y` | False |
| `<` | Less than | `x < y` | True |
| `>=` | Greater than or equal to | `x >= y` | False |
| `<=` | Less than or equal to | `x <= y` | True |

### Boolean Operators

Boolean operators combine and manipulate boolean values.

**AND** returns True only if both operands are True:
```
result = (5 < 10) AND (10 < 15)   // True
```

**OR** returns True if at least one operand is True:
```
result = (5 > 10) OR (10 < 15)    // True
```

**NOT** negates a boolean value:
```
result = NOT False                  // True
```

---

## Programming Constructs

Programming constructs determine the order in which lines of code are executed. In **structured programming** (a subsection of procedural programming), three constructs represent a program's control flow:

**Sequence** executes code line-by-line, from top to bottom, in the order written.

**Branching (selection)** runs a block of code only if a specific condition is met, using `IF` statements or `switch/case` statements. The program flow is interrupted, a condition is tested, and the outcome determines which block executes next.

**Iteration** repeats a block of code either a set number of times or while/until a condition is met, using `FOR`, `WHILE`, or `DO...UNTIL` loops.

### Identifying Constructs by Keywords

The keywords `if`, `elseif`, `else`, `endif`, `switch`, `case` indicate **selection**. The keywords `for`, `while`, `do` indicate **iteration**. Lines of code using none of these keywords are **sequence**.

---

## Selection

Selection tests conditions and determines which block of code runs next. There are two main forms: `if...elseif...else` statements (test conditions sequentially) and `switch...case` statements (test an expression against multiple constant values).

### Writing Conditions

Think of conditions as yes/no questions. When a range check requires two operators, use Boolean operators to combine them:

```
if number >= 1 AND number <= 6 then
    // number is between 1 and 6
endif
```

**Common AND/OR mistake:** `if number < 0 AND number > 100` is impossible (no number is simultaneously below 0 and above 100). Use `OR` to check if a number is outside a range: `if number < 0 OR number > 100`.

### If Statements

**`if`** executes a block only when the condition is true:
```
if condition then
    // code if true
endif
```

**`if...else`** adds an alternative block for when the condition is false:
```
if condition then
    // code if true
else
    // code if false
endif
```

**`if...elseif...else`** handles multiple scenarios:
```
if condition1 then
    // code if condition1 true
elseif condition2 then
    // code if condition2 true
else
    // code if all conditions false
endif
```

### Switch/Case Statements

`switch/case` is an alternative to chained `elseif` when comparing a single expression against multiple constant values:

```
switch expression
    case value1:
        // code for value1
    case value2:
        // code for value2
    default:
        // code if no case matches
endswitch
```

The `default` keyword is optional and executes when no case matches.

---

## Iteration

Iteration repeats a line or block of code using a loop.

### Count-Controlled Iteration (FOR Loops)

A `for` loop repeats a fixed number of times. The counter variable is initialised, iterates through a defined range, and increments (by 1 by default) after each iteration.

```
for i = 0 to 5
    print(i)
next i
```

**Python:** `for i in range(0, 6):` (the upper bound is exclusive, so `range(0, 6)` gives 0 to 5).

**Java:** `for (int i = 0; i < 6; i++) { ... }`

**Iterating over an array:**
```
fruits = ["apple", "banana", "orange"]
for i = 0 to fruits.length
    print(fruits[i])
next i
```

### Condition-Controlled Iteration (WHILE Loops)

A `while` loop repeats until a condition becomes false. The condition is evaluated **before** each iteration, so the loop body may never execute if the condition is initially false.

```
while condition
    // code
endwhile
```

Example (password check):
```
password = ""
while password != "secret"
    password = input("What is the password?")
endwhile
```

### Condition-Controlled Iteration (DO...UNTIL Loops)

A `do...until` loop executes the code block **at least once** before checking the condition. The condition is evaluated **after** each iteration.

```
do
    // code (executes at least once)
until condition
```

Example:
```
desiredNumber = 6
do
    roll = randomnum(1, 6)
    print("Rolled:", roll)
until roll == desiredNumber
```

*(Beyond source: Python does not have a native `do...while` or `do...until` construct. The equivalent is typically simulated using `while True:` with a `break` statement.)*

**Key difference:** A `while` loop checks the condition before executing the body (may run zero times). A `do...until` loop checks after executing the body (always runs at least once).

**Incrementing a variable** can be written as `i = i + 1`, `i += 1`, or `i++` depending on the language.

---

## Modularity, Functions and Procedures

### Modularity

**Modular programming** splits large, complex programs into smaller, self-contained modules (subroutines). Benefits of modularity include: making problems easier to understand and approach, enabling tasks to be divided between a team, simplifying testing and maintenance (each component can be dealt with individually), and improving reusability of components.

The **top-down approach** (also called **stepwise refinement**) continually breaks a problem down into sub-problems until each can be represented as an individual, self-contained module that performs a specific task. This implements the principle of **problem decomposition**.

### Functions vs Procedures

Both functions and procedures are named blocks of code that perform a specific task. They are collectively called **subroutines**.

| | Function | Procedure |
|---|----------|-----------|
| Returns a value? | Must always return a value | Does not return a value |
| Return statement | Has an explicit `return` | No `return` (or returns with no value) |
| Typical use | Calculations, producing a result | Performing actions (e.g. printing output) |

⚠ Check: PMT states "Procedures can return multiple values whereas a function must return one, single value." The intended meaning is that procedures can *modify* multiple values via parameters passed by reference, but they do not formally return values. The standard OCR definition is that procedures do not return a value.

**Function example:**
```
function addNumbers(a, b)
    return a + b
endfunction

c = addNumbers(5, 10)
print(c)                  // outputs 15
```

**Procedure example:**
```
procedure addNumbers(a, b)
    total = a + b
    print(total)           // prints rather than returns
endprocedure
```

**Parameters** are values passed into a function or procedure to allow it to complete its task.

### Best Practices

Choose descriptive, meaningful names for subroutines and parameters. Keep subroutines short and focused on a single task. Functions should have explicit return statements with meaningful return values.

---

## Parameter Passing

When parameters are passed into a subroutine, they can be passed **by value** or **by reference**.

### Passing by Value (byVal)

A **copy** of the value is passed to the subroutine. The subroutine works with this local copy, so the original value outside the subroutine is not affected. When the subroutine ends, the copy is destroyed.

```
function printValue(number : byVal)
    return("The random value is:", number)
endfunction
```

### Passing by Reference (byRef)

The **memory address** of the parameter is passed to the subroutine, so changes made within the subroutine directly affect the original value outside it. Both the subroutine and the calling code share the same memory location.

```
function printValue(number : byRef)
    return("The random value is:", number)
endfunction
```

### Comparison

| Aspect | By Value | By Reference |
|--------|----------|--------------|
| What is passed | A copy of the value | The memory address |
| Effect on original | Original unchanged | Original directly modified |
| Memory | Creates a copy (higher consumption) | No copy (more efficient) |
| Performance | Overhead for large data structures | Efficient for large data structures |
| Data protection | Protects original data | Risk of unintended side effects |
| Suitability | Primitive types, small structures | Large data structures (arrays, lists) |
| Reusability | Enhances reusability (no side effects) | May reduce reusability |

### Exam Notation

In OCR exam questions, assume parameters are passed by value unless stated otherwise. The notation used is:

```
function multiply(x:byVal, y:byRef)
```

**Why byVal matters in recursion:** In a recursive function, passing by value ensures each recursive call works with its own local copy of the parameter, preventing earlier calls from having their values overwritten. If passed by reference, the parameter would point to a single shared memory address, corrupting the recursion.

---

## Recursion

**Recursion** is a programming construct in which a subroutine calls itself during its execution. It continues until a **stopping condition** (also called the **base case**) is met, at which point the recursion stops.

### Three Features of a Recursive Algorithm

1. The function must **call itself**
2. A **base case** that returns a value without further recursive calls
3. The base case must be **reachable after a finite number of calls**

### How Recursion Works

Each time the function calls itself, a new **stack frame** is created within the **call stack**, storing parameters, local variables, and return addresses. This allows the subroutine to return to the correct point during execution. Stack frames accumulate until the base case is reached, at which point the subroutine **unwinds** (information is popped off the call stack in reverse order).

### Factorial Example

```
function factorial(number)
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)
    endif
endfunction
```

⚠ Check: PMT writes `if number == 0 or 1:` which is ambiguous pseudocode. In Python, `0 or 1` evaluates to `1` (truthy), so the condition would always be true. The correct form is `if number == 0 or number == 1:` as used in the Save My Exams source.

**Trace of `factorial(5)`:**

| Call | n | Returns |
|------|---|---------|
| factorial(5) | 5 | 5 * factorial(4) = 120 |
| factorial(4) | 4 | 4 * factorial(3) = 24 |
| factorial(3) | 3 | 3 * factorial(2) = 6 |
| factorial(2) | 2 | 2 * factorial(1) = 2 |
| factorial(1) | 1 | 1 (base case) |

### Importance of the Stopping Condition

Without a proper stopping condition, the function calls itself indefinitely, consuming excessive memory until the **call stack runs out of memory**, causing a **stack overflow** and crashing the program.

### Recursion vs Iteration

Any recursive algorithm can be rewritten iteratively, and vice versa.

| | Recursion | Iteration |
|---|-----------|-----------|
| Code length | Often fewer lines, more concise | Can be longer and more complex |
| Readability | Elegant for naturally recursive problems (trees, fractals) | Easier to understand and debug in general |
| Memory | Uses more memory (stack frames for each call) | More memory efficient |
| Performance | Repeated function calls are CPU-intensive | More efficient execution |
| Risk | Stack overflow if too many calls | No stack overflow risk |
| Tracing | Difficult to trace with many calls | Easier to trace |
| Application | Suited to divide-and-conquer problems | Suited to a wider range of problems |

**Tail recursion** is a form of recursion where the recursive call is the last operation in the function, allowing the compiler to optimise it to use less stack space.

### Translating Recursion to Iteration

**Recursive countdown:**
```
def countdown_rec(n):
    print(n)
    if n == 0:
        return
    countdown_rec(n - 1)

countdown_rec(10)
```

**Equivalent iterative version:**
```
def countdown_rec(n):
    while n > 0:
        print(n)
        n = n - 1
    return

countdown_rec(10)
```

The recursive call is replaced with a loop. The iterative version uses less memory and is easier to debug.

### Worked Example: Recursive to Iterative Conversion

Given the recursive function (a binary search):
```
function thisFunction(theArray, num1, num2, num3)
    result = num1 + ((num2 - num1) DIV 2)
    if num2 < num1 then
        return -1
    else
        if theArray[result] < num3 then
            return thisFunction(theArray, result + 1, num2, num3)
        elseif theArray[result] > num3 then
            return thisFunction(theArray, num1, result - 1, num3)
        else
            return result
        endif
    endif
endfunction
```

**Iterative equivalent:** Replace recursive calls by updating the parameters (`num1` and `num2`) within a `while(true)` loop. The recursive call `thisFunction(theArray, result + 1, num2, num3)` becomes `num1 = result + 1`. The call `thisFunction(theArray, num1, result - 1, num3)` becomes `num2 = result - 1`. The `return` statements exit the loop.

---

## Global and Local Variables

**Scope** refers to the section of code in which a variable is accessible.

### Local Variables

A **local variable** is declared within a specific block of code (e.g. a subroutine). It can only be accessed within that block, and its memory is released when the block finishes executing. Multiple local variables with the same name can exist in different subroutines without conflict.

Using local variables is considered good programming practice because it ensures subroutines are **self-contained**, with no danger of variables being affected by code outside the subroutine. This follows the principle of **encapsulation**.

### Global Variables

A **global variable** is declared at the outermost level of a program (outside any subroutine). It can be accessed and modified from any part of the program. All variables declared in the main body of a program are automatically global.

Global variables are useful for values that need to be used by multiple parts of the program (e.g. configuration settings, constants), and for sharing data between modules without parameter passing.

### Comparison

| Aspect | Local Variables | Global Variables |
|--------|----------------|-----------------|
| Scope | Only within the block where defined | Across the whole program |
| Lifetime | Deleted when the block ends | Persist until the program terminates |
| Memory | Efficient (released after use) | Always in memory while program runs |
| Name conflicts | Same name can exist in different subroutines | Can be unintentionally overwritten |
| Testing | Subroutine can be tested independently | Must run entire program to set up globals |
| Best practice | Preferred | Avoid where possible |

### Precedence Rule

If a local variable within a subroutine has the same name as a global variable, the **local variable takes precedence** within that subroutine.

### Converting Global to Local

To convert a program from using global variables to local variables: pass the variable into functions as a parameter, perform operations on the parameter, and return the modified value. The calling code then assigns the returned value back to its own local variable.

---

## Integrated Development Environment (IDE)

An **Integrated Development Environment (IDE)** is a program that provides a comprehensive set of tools to make it easier for programmers to write, develop, and debug code. Examples include PyCharm, Eclipse, IDLE, Microsoft Visual Studio, and Replit (web-based).

### Features for Writing Code

**Source code editor** provides features that make coding easier: **autocompletion** of variable/function/method names and closing brackets, automatic **indentation** within code blocks, and **syntax highlighting** (also called pretty printing) which uses distinct colours for keywords, strings, comments, variables, and functions to improve readability and reduce syntax errors.

**Code comments** are non-executing lines of text that document the code's purpose, algorithmic steps, and relevant information for maintenance.

### Features for Debugging Code

**Stepping** (step mode) executes a single line at a time, allowing the programmer to monitor the effect of each individual line. Options include step into, step over, and step out for examining function calls and control flow.

**Variable watch** (watch window) allows the programmer to observe how the contents of specific variables change in real-time during program execution, useful for pinpointing errors.

**Breakpoints** are markers set at specific lines where the program will pause execution. They can be condition-based or line-based, allowing inspection of the program's state and variable values at that point.

**Syntax error highlighting** automatically highlights errors in the code editor as developers type, allowing instant identification before execution.

**Error message list** displays errors, warnings, and messages generated during compilation and execution, with detailed descriptions and line numbers indicating where errors occurred.

**Crash dump / post-mortem report** captures the program's state and memory contents at the time of a crash, helping diagnose the root cause after unexpected termination.

**Stack contents** tool shows the contents of the program's call stack during debugging, displaying the order of function calls and the parameters and local variables of each function.

---

## Object-Oriented Programming Techniques

Object-oriented programming (OOP) is built around the concept of **classes** and **objects**.

### Classes

A **class** is a template (blueprint) for an object. It defines the **state** and **behaviour** of objects created from it. State is given by **attributes** (the object's properties/data). Behaviour is defined by **methods** (the actions an object can perform).

**Pseudocode example (Car class):**
```
class Cars
    private Manufacturer
    private Model
    private Price
    private Mileage
    private PreOwned

    public procedure new(givenManufacturer, givenModel,
                         givenPrice, givenMileage, givenPreOwned)
        Manufacturer = givenManufacturer
        Model = givenModel
        Price = givenPrice
        Mileage = givenMileage
        PreOwned = givenPreOwned
    endprocedure

    public function Accelerate()
        // Go faster
    endfunction

    public function honkHorn()
        // Honk horn
    endfunction
endclass
```

The `new` procedure is the **constructor**, called when creating new objects to initialise their attributes.

**Python:**
```python
class Cars:
    def __init__(self, manufacturer, model, price, mileage, preOwned):
        self.Manufacturer = manufacturer
        self.Model = model
        self.Price = price
        self.Mileage = mileage
        self.PreOwned = preOwned

    def Accelerate(self):
        # code to accelerate

    def honkHorn(self):
        # code to honk horn
```

**Java:**
```java
public class Cars {
    private String Manufacturer;
    private String Model;
    private int Price;
    private int Mileage;
    private boolean PreOwned;

    public Cars(String manufacturer, String model, int price,
                int mileage, boolean preOwned) {
        this.Manufacturer = manufacturer;
        this.Model = model;
        this.Price = price;
        this.Mileage = mileage;
        this.PreOwned = preOwned;
    }

    public void Accelerate() { /* ... */ }
    public void honkHorn() { /* ... */ }
}
```

### Objects and Instantiation

An **object** is a particular instance of a class. Creating an object from a class is called **instantiation**. A class can be used to create multiple objects, each with the same set of attributes and methods but different attribute values.

```
person1 = new Person("Bob", "Jones", "06/10/1981", "E Sports")
person2 = new Person("Jess", "Jones", "05/04/1980", "Astronomy")
```

### Methods

**Methods** define the behaviour (actions) that an object can perform. They are declared inside the class definition.

**Public methods** can be accessed by other classes and objects. **Private methods** can only be accessed within the class itself.

```
// Pseudocode
public procedure bank_left()
    // Code to make the aircraft bank left
endprocedure

private procedure bank_right()
    // Code to make the aircraft bank right
endprocedure
```

*(Beyond source: In Python, there is no enforced private access modifier. By convention, a method prefixed with a single underscore `_` is treated as private, and a double underscore `__` triggers name mangling. However, both can still be accessed from outside the class.)*

### Attributes

**Attributes** store the state (data/properties) of an object. They are typically declared as **private** to enforce encapsulation.

```
class Person
    private name
    private age
    private gender
    private occupation
    private isMarried
endclass
```

In Python, attributes are defined within `__init__` using the `self` keyword: `self.name = name`.

In Java, attributes are declared at the class level with access modifiers: `private String name;`.

---

## Inheritance

**Inheritance** allows a new class (the **subclass** or **derived class**) to inherit the attributes and methods of an existing class (the **superclass** or **base class**). The subclass can then add its own additional attributes and methods, or override inherited ones.

**Pseudocode example:**
```
CLASS Vehicles
    private manufacturer
    private make
    private cost

    public procedure new(givenmanufacturer, givenmake, givencost)
        manufacturer = givenmanufacturer
        make = givenmake
        cost = givencost
    endprocedure

    public procedure TurnEngineOn()
        // Code to turn engine on
    endprocedure
ENDCLASS

CLASS Cars INHERITS Vehicles
    private isInsured
    private engineCapacity

    procedure Cars(givenmanufacturer, givenmake, givencost,
                   givenInsured, givenengineCapacity)
        SUPER.Vehicles(givenmanufacturer, givenmake, givencost)
        isInsured = givenInsured
        engineCapacity = givenengineCapacity
    endprocedure

    procedure GearChange()
        // Code to change gear
    endprocedure
ENDCLASS
```

The **`super`** keyword calls the constructor of the parent class to inherit its attributes. The `Cars` subclass inherits `manufacturer`, `make`, `cost`, and `TurnEngineOn()` from `Vehicles`, while adding `isInsured`, `engineCapacity`, and `GearChange()`.

**Python:** Inheritance is specified by placing the parent class name in parentheses: `class Car(Vehicle):`. The parent constructor is called with `super().__init__(manufacturer, make, cost)`.

**Java:** The `extends` keyword is used: `public class Car extends Vehicle`. The parent constructor is called with `super(manufacturer, make, cost)`.

---

## Encapsulation

**Encapsulation** is the technique of declaring attributes as **private** so they can only be accessed or modified through **public methods**. This implements the principle of **information hiding**, making programs less complex by protecting data from being accidentally edited by other parts of the program.

Top-down design implements the same principle: each module is designed to be self-contained.

### Getter (Accessor) Methods

A **get method** provides controlled read access to a private attribute without allowing direct modification.

```
class NumberUpdater
    private number = 10

    public function getNumber()
        return number
    endfunction
endclass
```

### Setter (Mutator) Methods

A **set method** provides controlled write access, typically including validation logic before updating an attribute.

```
class NumberUpdater
    private oldnumber = 10

    public procedure setNumber(newnumber)
        if newnumber < 0 then
            oldnumber = oldnumber    // reject negative values
        else
            oldnumber = newnumber
        endif
    endprocedure
endclass
```

In this example, calling `Object1.setNumber(45)` updates the value to 45, but `Object1.setNumber(-34)` keeps the original value because the validation rejects negative numbers.

---

## Polymorphism

**Polymorphism** allows objects of different classes to respond to the same method call in different ways. In **run-time polymorphism**, a subclass overrides a method defined in a superclass, and the correct version of the method is selected at run-time based on the actual type of the object, not at compile-time.

**Pseudocode example:**
```
CLASS Animal
    METHOD speak()
        // Empty placeholder method
ENDCLASS

CLASS Dog EXTENDS Animal
    METHOD speak()
        OUTPUT "Woof"
ENDCLASS

CLASS Cat EXTENDS Animal
    METHOD speak()
        OUTPUT "Meow"
ENDCLASS

PROCEDURE make_sound(animal : Animal)
    CALL animal.speak()

myDog = NEW Dog()
myCat = NEW Cat()
CALL make_sound(myDog)    // Outputs: Woof
CALL make_sound(myCat)    // Outputs: Meow
```

The `make_sound()` procedure accepts any `Animal` object but calls the correct overridden version of `speak()` depending on whether the object is a `Dog` or `Cat`. This demonstrates **method overriding** and **dynamic method binding**.

**Python:**
```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

def make_sound(animal):
    animal.speak()

make_sound(Dog())    # Woof
make_sound(Cat())    # Meow
```

**Java:** Uses `@Override` annotation and the `extends` keyword. A superclass reference (`Animal animal`) can point to a subclass object, and `animal.speak()` dynamically calls the correct overridden method.

---

## Key Terms Summary

| Term | Definition |
|------|-----------|
| **Data type** | Classification of data by the kind of value it represents |
| **Casting** | Converting one data type to another |
| **Sequence** | Code executed line-by-line, top to bottom |
| **Selection (branching)** | A condition is tested and the outcome determines which block runs |
| **Iteration** | A block of code is repeated (count-controlled or condition-controlled) |
| **Count-controlled loop** | Repeats a fixed number of times (FOR loop) |
| **Condition-controlled loop** | Repeats until a condition is met (WHILE, DO...UNTIL) |
| **Recursion** | A subroutine that calls itself until a base case is reached |
| **Base case** | The stopping condition in recursion |
| **Stack overflow** | When the call stack runs out of memory due to excessive recursive calls |
| **Call stack** | LIFO data structure storing details of subroutine calls |
| **Stack frame** | An entry on the call stack holding parameters, local variables, and return address |
| **Scope** | The section of code in which a variable is accessible |
| **Local variable** | Accessible only within the block where it is defined |
| **Global variable** | Accessible across the whole program |
| **Modularity** | Splitting a program into smaller, self-contained modules |
| **Top-down approach** | Continually breaking a problem into sub-problems (stepwise refinement) |
| **Subroutine** | A named block of code that performs a specific task (function or procedure) |
| **Function** | A subroutine that returns a value |
| **Procedure** | A subroutine that does not return a value |
| **Parameter** | A value passed into a subroutine |
| **Pass by value (byVal)** | A copy of the value is passed; original unchanged |
| **Pass by reference (byRef)** | The memory address is passed; original can be modified |
| **IDE** | Software providing tools to write, develop, and debug code |
| **Class** | A template defining the attributes and methods of an object |
| **Object** | A particular instance of a class |
| **Instantiation** | The process of creating an object from a class |
| **Attribute** | A property/data value of an object (defines state) |
| **Method** | An action an object can perform (defines behaviour) |
| **Constructor** | A special method called when an object is instantiated |
| **Encapsulation** | Declaring attributes as private, accessed only via public methods |
| **Information hiding** | Protecting data from accidental modification by other parts of the program |
| **Inheritance** | A subclass inheriting attributes and methods from a superclass |
| **Polymorphism** | Objects of different classes responding differently to the same method call |
| **Method overriding** | A subclass redefining a method inherited from a superclass |
