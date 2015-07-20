#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python is "object oriented". This means a lot of nebulous and uninteresting
# things, but you have to know what it is to get a job.

# Object-oriented programming (OOP) is a means of "abstracting" a program's
# structure.
# A language described as "OO" usually has direct support for
#     Encapsulation
#     Inheritance
#     Delegation

# I am not a fan of OOP, but you need to know it. Sorry!

# In Python, and many languages, all three of these properties are gained
# by creating data structures known as "objects" or "classes"
# (same thing (in Python)). A `list` is an example of a a class.

# 2.0) Object basics

class MyObject:
    pass

# This is the simplest class definition. The `class` keyword introduces
# a class definiton/declaration (both must occur in the same place in Python).
# `MyObject` is the name of the class.

# A class definition is comprised of a list of statements, which we have just
# speficied as `pass` here.

def class_fun():
    # Classes can be "instantiated". This means creating an "instance" of
    # the class. You can think back to the blueprint metaphor. The class
    # definition is the blueprint, the "instance" is a building made from the
    # blueprint, which may be slightly different.
    x = MyObject()

    # Declaring a class automatically creates a function named the same as
    # the name of the class. This function is called the class's "constructor".
    # By default, the function takes no arguments and does nothing special.

    # An object instance has it's own environment. It can be accessed using
    # `.` syntax.

    x.a = 1

    # 2.0.1) What does the following print?
    print(x.a)




    y = MyObject()

    y.a = 1

    # 2.0.1) What does the following print?
    if x is y:
        print("yes")
    else:
        print("no")


# 2.1) Methods

# Functions defined on a class have a special name: "methods".

class Stuff:
    def print_stuff(self): #ignore that "self" for now
        print("stuff")

def method_fun():
    y = Stuff()

    # Methods are also called with `.` syntax, but with parentheses to
    # indicate a function is being called.
    y.print_stuff() # (Sta. 2.1.0) # prints "stuff"

    # Wait, what the fuck?
    # 2.1.1) Why does (Sta. 2.1.0) printing "stuff" contradict what we
    #        already learned?

    # You see, method calls are special. They are a shortcut for a longer
    # notation. They are related thus:

    y.print_stuff()

    # is actually interpreted as

    Stuff.print_stuff(y)

    # The instance of `Stuff` called `y` is passed in to print_stuff. This
    # allows us to mutate instance variables with . notation and call methods
    # on our "selves". That is why this first variable is called "self" by
    # convention.

    class OtherStuff:
        def blah(self, a, b, c):
            print(b)

    z = OtherStuff()

    # 2.1.2) What does the following print?
    z.blah(1, 2, 3)

    # 2.1.3) The following gives an error when interpreted, saying
    #        the number of arguments given is wrong. Why is this? If `blah`
    #        z.blah(1, 2, 3, 4)
    #        Hint: How does CPython interpret z.blah(1, 2, 3, 4)?

# 2.2) Custom constructors

# You can define a custom constructor by defining a method called __init__.

class Point:
    def __init__(self, x, y):
        # see how namespaces can be handy?
        self.x = x
        self.y = y

    def __len__(self):
        return math.sqrt(x * x + y + y) # boring vector math shit

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

def pointless():
    p = Point(3, 4) # only 2 arguments as per (Ex 2.1.3)

    # 2.2.1) What do the following print?
    print(p.x)
    print(p.y)

    q = Point(3, 4)

    # 2.2.2) What does the following print?
    print(p is q)

    # 2.2.2) What does the following print?
    print(p == q) # recall, a == b generally calls a.__eq__(b)

    # 2.2.3) No one cares about math, but what does the interpreter
    #        interpret this expression as?
    print(len(p))


# 2.3 & beyond) Todo later
