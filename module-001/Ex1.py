#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This is a Python script or program or Python source code. These terms
# are more or less interchangeable, but have subtle and boringly pedantic
# differences.

# (?) On line 1, the #! is called the "shebang" or "hashbang"
# When the script is executed by directly invocing the file on linux,
# this line tells the shell what program to use to run the script.
# `/usr/bin/env` is an executable which will run it's first argument
# according to what the current user has set in their environment. In this case
# `/usr/bin/env python3` will run the same program that would run if the user
# typed `python3` and hit enter into their shell.

# (?) Differences between Python 2.7 and Python 3.x are unimportant. We will
# be using Python 3 exclusively.

# (?) The second line says that the file should be encoded in *UTF-8* rather than
# *ascii*. Don't worry about this.

# (?) Python is a *high level*, *strongly typed*, *dynamic*, *duck-typed*
# programming language. A programming language is a formal language. CPython
# (which we will be using) is an *interpreted* (rather than *compiled*)
# *implementation* of Python. The distinction between a programming language
# and an implementation of that language is like the difference between a
# blueprint and a building built with the blueprint. Other implementations
# of Python include PyPy, IronPython, and JPython. When people use "Python"
# imprecisely to refer to an implementation of Python, they are always
# referring to CPython.

# Uhhh don't worry about this for now
import codecs

# 1.0) Evaluation model

# Python variables are boxes which contain values. In a "statement" like:

a = (10 + 1)

# the expression on the "right hand side" (rhs) namely `(10 + 1)` is "evaluated"
# to `11` and then put into the box named `a` on the left hand side (lhs).

# Similarly with a function call:

a = abs(-10) # Fig. 1.0.1, Note: abs is the absolute value function from math

# the expression on the rhs evaluates to 10, and then this value is put into
# the value denoted on the lhs.

# Unsimilarly to pure mathematics, one can say:

a = a + 500

# What happens is exactly as I described above. The rhs is evaluated and then
# the resulting value is stored into the box named `a`.

# Let's take a look at the expression (a + 500). When the Python interpreter
# sees a "variable" or "identifier" (same thing) that needs to be "evaluated",
# it will look up the value of that identifier in the "environment".

# In Fig. 1.0.1, we stored the result `10` in `a`, so when the interpreter
# looks up `a` in the expression, it will get back this value. So then
# the interpreter will see the expression as `(10 + 500)` rather than
# `(a + 500)` and we no longer have that confusing paradoxical looking
# statement.

# This of course evaluates to `510` and then this value is stored in `a`,
# irretrievably overwriting the `10` value that was there before.

# Note. 1.0.1
# (?) The "environment" it turns out is actually just another Python
# data structure that can be accessed and manipulated directly! Its "type"
# is `dict`, or dictionary and the above could be decomposed into:
#     global_d = globals() # magic "built-in" function
#     a_temp = global_d["a"]
#     global_d["a"] = a_temp + 500
# Under the hood these are equivalent to
#     a_temp = global_d.__getitem__("a")
# and
#     global_d.__setitem__("a", a_temp + 500)

# Exercises
# 1.0.1) Read the following statements and tick the box next to the correct
#        answer.

# a = 10
# b = 20
# a = b

# The new values of a and b are:
# [ ] a = 20  b = 0
# [ ] a = 20  b = 20
# [ ] a = 0   b = 10
# [ ] a = 10  b = 10
# [ ] a = 30  b = 20
# [ ] a = 30  b = 0
# [ ] a = 10  b = 30
# [ ] a = 0   b = 30
# [ ] a = 10  b = 20
# [ ] a = 20  b = 10


# 1.1) functions

#↓A ↓B   ↓C
def func(a, b, c):
# A) This is the *keyword* introducing functions. This word must be present so
#    that the python interpreter can tell that you want to declare a function
#    rather than some other construct such as a loop or conditional.

# (?) A keyword is a special word that cannot be used in other places in the
#     language, such as the name of a function or as a variable name. These
#     reserved terms are used by the *parser* to determine the meaning of the
#     program more easily.

# B) `func` here is the name of the function being declared or defined. In
#    some languages, function declaration (saying what the function looks like)
#    and definition (how it works) are separate. In Python they are always
#    done together.

# C) `a`, `b`, and `c` are the function's arguments (or formal parameters (or
#     just parameters), same thing). A function may have zero parameters,
#     and may even take a variable number of parameters, such as `print()`.
#     Arguments which must be specified are called non-optional arguments.
#     The above function has 3 non-optional arguments.
#     If a non-optional argument is left out of the function, the Python
#     interpreter will crash with an error message.

# B & C together represent the "function('s) signature" or "prototype". I will
# often ask what the signature of a function is. For instance if you call
# `func(1,2)` I may ask "what is the signature of func?" to try to point out
# that func is declared with 3 parameters but you have provided only two.


# Below is known as the "function body" or definition (same thing). All
# functions in python must have a definition. The simplest definition is
# `pass`, which does nothing.

# The function body must be indented one level from the declaration (the line
# beginning with the `def` keyword)

# Explanation of how if and return statements work would go here
# ask me if you need it~
    if a == b:
        print("a is equal to b")
    elif b == c:
        print("b is equal to c")
    if a == c:
        print("a is equal to c")
        return
    else:
        print("stuff")
    print("done")

# What is printed in the following function calls?
# 1.1.1) func(1,1,2)
# 1.1.2) func(2,1,1)
# 1.1.3) func(1,1)
# 1.1.4) func(1,2,1)

# 1.1.5) In each of the above function calls, a different sequence of `print`
#        "statement"s are executed. There is a sequence of `print` statements
#        that is possible to execute that is not represented in 1.1.1-1.1.4.
#        What arguments to `func` will "hit" this "execution path"?

# 1.2 Lists

# A list is a "data structure" which holds a finite or zero number of values.
# Python has special syntax for creating lists:
def useless_list_example():
    mylist = [10, 20, 30, 40, 50]
    emptylist = []
    altsyntax = list(10, 20, 30, 40, 50)

    # The contents of the lists `mylist` and `altsyntax` will be
    # indistinguishable

    altempty = list()

    mylength = len(mylist) # 1.2.1) what do you think the value of `mylength`
                           #        will be after this line?

    mylength = len([]) # 1.2.2) or this one?

    # (?) Under the hood, `len(t)` calls the `t.__len__()` method on the
    # underlying list object

    # lists can be "indexed" using a special syntax

    x = mylist[0] # `x` is assigned the value `10`

    # Lists can be "mutated" using the same syntax, assigning a value to the
    # given index:

    mylist[1] = x # tricky!

    print(mylist) # 1.2.3) What gets printed?

    altsyntax[0] = x

    # Note that two lists which happen to have the same elements are NOT
    # the same list!

    print(altsyntax) # 1.2.4) what gets printed?

# We put the above statements in a function for a reason. Variables assigned
# in a function are "local" to that function's body and cannot be accessed
# outside it (unless they are "returned" from the function)
# This way we do not "pollute" the "global namespace" with these variables,
# which can cause confusion in large programs/scripts.


# 1.3) Lists and object assignments
#      This section is really hard, don't get discouraged!


# NOTE this is an 'l' not a '1'. Make sure you can see the difference
def modlist(l):
    l.append(420)

def nonelist(lll):
    lll = None


def dosomethingint(i):
    i = i + 1


def tricky_assignments():
    a = 50
    b = a

    l = [10, 20, 30, 40, 50]
    r = [10, 20, 30, 40, 50]

    if l == r: # (?) under the hood, `l.__eq__(r)`
        print("equal") # if, for every element in both lists, in order,
                       # each element compares equal, then `l == r`
                       # will evaluate to `True`

    # Freebie. This will print "equal"!

    lref = l

    # A list in python is "mutable". This means that you can alter the list
    # "in-place" in the environment, as you have already seen above.

    # An integer on the other hand, is "immutable". You cannot modify an
    # integer stored in the global environment, you may only assign
    # a new value to that name in the environment.

    # Compare:

    l.append(1) # modifies `l` "in-place"

    # a.addto(1) #doesn't exist! not possible!

    # by calling `l.append(1)`, we have updated the value, the
    # "reference to the list" l in the environment directly

    if l == lref: # (?) under the hood, `l.__eq__(r)`
        print("equal")
    else:
        print("not equal")

    # 1.3.1) What will be printed in the conditional above?

    a = a + 1

    if a == b: # (?) under the hood int(a).__eq__(int(b))
        print("equal")
    else:
        print("not equal")

    # 1.3.2) What will be printed in the conditional above?
    #        Refer to (Note. 1.0.1) if unsure.

    # It is possible to check if two labels/names/boxes contain the same
    # "reference". To do this, we use the `is` keyword.

    # First, let's make l and r compare `True` with `==`. Did you notice
    # that I didnt say "let's make sure l and r are equal"?
    # This is because "equal" is not a precise term in programming. It means
    # multiple things, so it pays to be precise!

    print(l) # print [10, 20, 30, 40, 50, 1]
    print(r) # print [10, 20, 30, 40, 50]

    # 1.3.3) What statement should we use to make l and r compare `True` with
    #        `==`?

    # Ignore this line, im just hiding the answer :)
    eval(codecs.encode("e.nccraq(1)","rot_13"))

    # Okay now lets try:
    if l is r:
        print("l and r reference the same list in memory!")
    else:
        print("they don't")
    # 1.3.4) What do you think above will print?


    if l is lref:
        print("l and lref reference the same list in memory!")
    else:
        print("they don't")
    # 1.3.5) What do you think above will print?

    # There is a special syntax for incrementing an integer. It is confusing
    # because it sort of looks like it should mutate the variable. Let's
    # set things up again:

    a = 1
    b = a

    a += 1 # SAME AS a = a + 1

    print(a) # prints 2

    # 1.3.6) What will the following print?
    #        Refer to (Note. 1.0.1) if unsure.
    print(b)


    lll = [1,2,3]
    # Remember: lists are mutable. When you pass a mutable variable to a
    # function, that function can change the result of the list by
    # mutating the variable
    modlist(lll)

    print(lll) # 1.3.7) What prints?


    # Let's try
    nonelist(lll)

    # Ohhh this is tricky. What does that function above do exactly?
    # It looks like it reassigns its parameter `l` to the value `None`.
    # But: functions each have their own scope. You can think of our `lll`
    # as actually referring to `tricky_assignments::lll`
    # and `nonelist`'s `lll` as referring to `nonelist::lll`.
    # When nonelist reassigns `lll`, it is doing so to its own local copy.
    # This naming scheme is called "variable scope" or just "scope".

    # 1.3.7) With that in mind, what does the following print?
    print(lll)


    k = 1
    dosomethingint(k)

    # 1.3.7) What does the following print?
    print(k)


# 1.3.8) Write a function that takes in a list `l` and mutates its first
#        element to be the value `1`.


# 1.4) Loops

# Lists can be "iterated" over using a for loop.


def print_list(l):

    # Let's try to print each element from our input list `l`

    for x in l:
        print(x)

    # You can think of the above as assigning the value of the elements of `l`
    # in turn to the name `x`.


def more_exercises():

    l = [1, 2, 3]

    # 1.4.1) What does the following print?
    print_list(l)

    # 1.4.2) What do you thing the following prints?
    #        Note: reversed is a built-in function.
    print(reversed(l))

    l.reverse() # this function mutates the list

    # 1.4.2) What does the following print?
    print(l)


# 1.5) Misc

# 1.5.1) Whats wrong with the following program?
"""
def def():
    return 1

print(def())

"""

# 1.5.2) Whats wrong with the following program?
"""
def func(a):
    return 1

print(func())

"""


