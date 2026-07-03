# 2.5 Object Oriented Languages

## Classes

A **class** is a blueprint or template used to create **objects** in Object Oriented Programming (OOP). It defines the **attributes** (data) and **methods** (behaviours) that all objects of that type will share, enabling reusable, modular, and organised code.

**Class variables** are the attributes defined within a class template (e.g. Name, Age, Gender in a People class). When an object is created from the class, those attributes become **instance variables** holding that specific object's values (e.g. Name: "Bob", Age: 34, Gender: "Male").

**Instantiation** is the process of creating an object from a class. The name used to refer to an object is its **identifier** (e.g. `P1`, `P2`).

**Prebuilt classes** are provided by the programming language and offer common functionality without the programmer writing them from scratch. Java examples include `Date` and `Calendar` (date handling), `String` (text handling), `Random` (random number generation), and `Scanner` (reading input from a user or file). **Custom classes** are created by the programmer to define new data types not provided by the language (e.g. an Animal class).

Classes also contain **methods** (functions or procedures) that define actions or behaviours objects can perform. A **function** is a method that must return a value. A **procedure** is a method that does not need to return a value.

**Exam technique:** When asked "What is a class?", a full-mark answer requires two points: (1) it is a blueprint/template for creating objects with specific attributes, and (2) it provides a way to organise code in a modular fashion.

## Objects

An **object** is a specific instance of a class, representing a real-world entity (e.g. teacher, aeroplane, mobile phone). While a class describes the properties and behaviours in general, an object is created from that blueprint with its own unique values for each property.

A **constructor** is a special method within a class that is automatically called when an object is instantiated. Constructors define the initial values of instance variables and perform any necessary setup to prepare the object for use.

**Creating an object (instantiation syntax):**

```
mushypeas = new ItemForSale("mushy peas", 0.89)
```

or equivalently in typed syntax:

```
ItemForSale mushypeas = ItemForSale("mushy peas", 0.89)
```

Three marks are typically available: (1) the identifier on the left-hand side, (2) the class type on the right-hand side, and (3) the correct parameters passed in.

## Methods

**Methods** are functions associated with objects or classes that define the behaviour and actions objects can perform. They come in two types:

| Type | Description |
|---|---|
| **Function** | Performs a task and returns a value |
| **Procedure** | Performs a task but does not return a value |

Once objects have been created, they call methods using **dot notation**: `objectName.methodName()`. For example, given `jumboJet = new aircraft("Boeing", "747", 416, 547)`, calling `jumboJet.Takeoff()` invokes the Takeoff method on that specific object.

Methods called through objects are **instance methods** because they operate on the specific data of that individual instance. **Static methods** are associated with the class itself and can be called without creating an instance of the class.

### Public and Private Methods

| | Public Methods | Private Methods |
|---|---|---|
| **Access** | Accessible from within the same class or from any external class | Only accessible within the same class; cannot be invoked by external code |
| **Impact of changes** | May affect other parts of the codebase, so should be carefully designed and backward-compatible | Localised impact only; can be modified or refactored without affecting other parts of the program |
| **Use case** | Providing access to certain functionalities or behaviours to other parts of the program | Internal implementation details that should not be accessed externally; used for organising and managing code internally |

If a method does not specify the keyword `public` or `private`, its default access level is **public**.

**Exam technique:** A one-mark definition of a method: a function/procedure that belongs to a class and operates on its instance data, allowing objects to perform actions and behaviours.

## Attributes

An **attribute** is a data member or property associated with an object or class. Attributes define the **state** of an object and can have different values for different instances of the same class. They can be of various data types: integers, strings, Booleans, or even other objects.

Attributes have **access rights** (public or private) that determine how they can be accessed. A private attribute (e.g. `private manufacturer` of type String in a Car class) can only be accessed by instances of that class, not by external code.

A class typically has many attributes. For example, a Person class might have: Name (String), Age (Integer), Gender (String), Occupation (String), and IsMarried (Boolean).

**Key distinction:** Attributes declared within methods are **local variables**. Local variables cannot have access modifiers (public/private) because they are local to the method and have limited scope. They are only accessible within the block or method in which they are declared and are not part of the class's state.

## Inheritance

**Inheritance** allows a class to inherit the properties and behaviours (methods and attributes) of another class. It involves two entities:

| Term | Also known as | Role |
|---|---|---|
| **Base class** | Parent class, superclass | Serves as the blueprint from which the derived class inherits; defines common properties and behaviours shared among multiple derived classes |
| **Derived class** | Child class, subclass | Inherits the attributes and methods of the base class; can add its own additional attributes and methods |

Inheritance establishes an **"IS-A" relationship** between base and derived classes. For example, if Vehicle is the base class and Car is the derived class, then "a Car IS-A Vehicle."

**Benefits:** Inheritance promotes code reuse by allowing derived classes to use existing code from the base class, avoiding duplication and improving organisation and maintainability.

**Example:** A Vehicle base class with attributes (Manufacturer, Make, Cost) and methods (TurnEngineOn(), TurnEngineOff(), SteerLeft(), SteerRight()) can have derived classes Car and Truck. The Car class inherits all Vehicle attributes and methods but adds its own attributes (IsInsured, EngineCapacity) and methods (GearChange(), UnlockDoors()). The Truck class similarly adds its own (IsRefrigerated, TotalCargoArea, ReleaseTrailer(), UnlockTrailerDoors()).

The **`super` keyword** is used within a subclass to refer to the superclass and access its members (methods, attributes, or constructors).

**Exam technique:** For a "describe inheritance" question, two marks are typically awarded: (1) the child/derived/subclass takes on attributes and methods, (2) from the parent/base/superclass.

## Encapsulation

**Encapsulation** is the practice of grouping data (attributes) and methods (functions) within a class. It serves several purposes:

**Data security:** By controlling access using access modifiers (public, private), encapsulation ensures data is not accidentally modified or misused. Private variables are only accessible within the class itself, and external code cannot access them directly.

**Information hiding:** Encapsulation hides how things work inside a class from the outside. External code interacts with the class using public methods without needing to understand its internal details. This uses a concept called **abstraction**, which reduces complexity by hiding implementation details.

**Code organisation and reusability:** Related data and methods are kept together within an object. The same object or class can be reused in different parts of a program without rewriting the code. Programmers can use methods and classes from other parts of the program without understanding how they have been constructed internally.

### Encapsulation in Classes

Private variables and private methods are not accessible outside the class. Public variables and public methods can be accessed from outside the class. This separation provides encapsulation at the class level.

### Encapsulation in Methods

Variables declared within a method are not accessible outside of that method. This provides encapsulation at the method level.

**Exam technique:** To describe encapsulation in code, identify a private attribute (e.g. `private distance`) and explain that a public method (e.g. `updateDistance()`) serves as the interface to modify it. This prevents direct access to the internal data from outside the class.

## Polymorphism

**Polymorphism** allows objects to take on different forms or behaviours. Different objects can share the same method name but execute different code when that method is called. It makes code more flexible, reusable, and easier to maintain by allowing objects of different classes to be treated as belonging to a common group.

### Method Overriding

The **`override` keyword** provides a new implementation for a method already defined in the parent class.

**Example:** A base class Animal has a method `move()` that prints a generic message. Derived classes Fish and Bear each override `move()` to print class-specific messages ("I am a fish swimming" and "I am a bear lumbering around" respectively). All three classes have a method named `move()`, but each executes different code.

⚠ Check: the source labels this Animal/Fish/Bear example as "method overloading"; standard treatment classifies this as **method overriding**, since the subclass replaces the inherited method with its own implementation using the same signature. Method overloading refers to multiple methods with the same name but different parameter lists within the same class.

**Example 2:** A base class Vehicle has methods `startEngine()` and `displayInfo()`. Derived classes Motorcycle and Car each override `displayInfo()` but inherit `startEngine()` unchanged. A Motorcycle object calling `displayInfo()` outputs "I am a Motorcycle!", while a Car object outputs "I am a Car!". Both can still call `startEngine()` and get "Engine Started!" from the base class.

### Treating Objects as Common Groups

Polymorphism allows objects of different derived classes to be stored in variables or arrays typed as the common base class:

```
Vehicle vehicle1 = new Car()
Vehicle vehicle2 = new Motorcycle()
```

This allows an array of type Vehicle to store both Motorcycle and Car objects rather than requiring separate data structures. Despite being stored as Vehicle references, calling `vehicle1.displayInfo()` still outputs "I am a Car!" and `vehicle2.displayInfo()` still outputs "I am a Motorcycle!" because the overridden method in the actual object's class is executed. This flexibility is essential for creating maintainable and modular code.

## Key Terminology Summary

| Term | Definition |
|---|---|
| **Class** | A blueprint/template for creating objects, defining their attributes and methods |
| **Object** | A specific instance of a class with its own state and behaviours |
| **Instantiation** | The process of creating an object from a class |
| **Identifier** | The name used to refer to an object |
| **Constructor** | A special method automatically called when an object is created, setting initial values |
| **Method** | A function or procedure belonging to a class that defines object behaviours |
| **Attribute** | A data member/property of a class or object that defines its state |
| **Class variable** | An attribute defined in the class template |
| **Instance variable** | An attribute belonging to a specific object with its own value |
| **Inheritance** | A mechanism allowing a derived class to take on attributes and methods of a base class |
| **Base class** | The parent/superclass from which another class inherits |
| **Derived class** | The child/subclass that inherits from a base class |
| **Encapsulation** | Grouping data and methods within a class and controlling access via public/private modifiers |
| **Abstraction** | Hiding implementation details to reduce complexity |
| **Polymorphism** | Allowing objects to take on different forms; methods with the same name execute different code depending on the object's class |
| **Method overriding** | A derived class provides a new implementation for a method inherited from the base class |
| **Dot notation** | Syntax for calling methods on objects: `objectName.methodName()` |
| **Public** | Accessible from within the class and from external classes |
| **Private** | Accessible only within the class itself |
| **`super` keyword** | Used in a subclass to refer to the superclass and access its members |
