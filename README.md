Python Design Pattern Practice
====
Helpful Guide [https://refactoring.guru/design-patterns/]

# Dependancies
unittest
pytest
pymongo

Use this command to install all dependancies
```bash
pip install -r requirements.txt
```

## MongoImage
To Start
```bash
docker run --name mongodb -d -p 27017:27017 mongo
```

## Singleton
Singleton objects ensure that a class has only one instance that is globally available to other services. Whenever the object is called, the same object is returned.

This pattern is used when
* 

Implementation:
* Create a singleton object that stores JSON(ish) objects
* Make default constructor private, to prevent objects from using the new operator with the singleton object
* Create a recycle method to wipe all data from the singleton object

## Abstract Factory (W.I.P.)
Provides an interface for creating families of related or dependant objects without specifying their concrete classes

## Adaptor
Todo

## Builder
Todo

## Chain of Responsibility
Todo

## Command
Todo

## Decorator
Todo

## Facade
Todo

## Factory (W.I.P.)
Define an interface for creating an object but lets subclasses decide which class to instantiate. Factory pattern replaces direct object construction calls, defering it to factory methods. Also known as Virtual Constructor.

This pattern is used when
* A subclass cannot predict the class of object it must create
* A class wants its subclasses to specify the objects it creates

Implementation

## Flyweight
Todo

## Model - View - Controller
Todo

## Observer
Todo

## Object Oriented Programming
Todo

## Prototype
Todo

## Proxy
Todo

## State
Todo

## Strategy
Todo

## Template