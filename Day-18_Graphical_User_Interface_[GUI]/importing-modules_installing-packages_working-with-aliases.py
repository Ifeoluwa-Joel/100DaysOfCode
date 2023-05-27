# A. IMPORTING MODULES
"""
All the ways we can import modules
"""
"""
1.  BASIC IMPORT
    <keyword> <module_name>
    E.G: import turtle.

To use this method, when we want to create an object from a class in the module.
We will have to specifically mention which class we are referring to. It is more expressive 
self-explanatory in terms of code readability:-
E.G: tim = turtle.Turtle()   # We will have to always include the name of the module 
                                dot the class name.
Example 2:
import random
generated_no = random.randint(0, 100)
"""

"""
2. from ..... import ......
    <keyword> <module_name>  <keyword> <what_we_need_in_module>
    E.G: from random import randint
        guessed_num = randint(0, 100)
    
We will not have to always include module name when tapping into the module. 
It is a very helpful approach if we are going to be tapping into the module several times.
Example 2:
from turtle import Turtle
tim = Turtle()
tom = Turtle()
terry = Turtle()
vamp = Turtle()
nemo = Turtle()
"""

"""
3. from xxxxx import *
Not advisable. It gets confusing
"""

# B. ALIASING MODULES
"""
This basically has to do with changing the identifier of a module.
import turtle as t
timmy_the_turtle = t.Turtle()

Why is this a good idea though? 🤔🤔
It is used to import modules that have very very long identifiers.
"""

# C. INSTALLING MODULES (or PACKAGES)
"""
There are some modules we can't just import because they are not in the standard library of Python.
"""
