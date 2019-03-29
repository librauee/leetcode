# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 17:54:17 2019

@author: Administrator

Instance Methods

The first method on MyClass, called method, is a regular instance method. 
That’s the basic, no-frills method type you’ll use most of the time. 
You can see the method takes one parameter, self, which points to an instance of MyClass when the method is called (but of course instance methods can accept more than just one parameter).

Through the self parameter, instance methods can freely access attributes and other methods on the same object. 
This gives them a lot of power when it comes to modifying an object’s state.

Not only can they modify object state, instance methods can also access the class itself through the self.__class__ attribute. This means instance methods can also modify class state.

Class Methods
Let’s compare that to the second method, MyClass.classmethod. 
I marked this method with a @classmethod decorator to flag it as a class method.

Instead of accepting a self parameter, class methods take a cls parameter that points to the class—and not the object instance—when the method is called.

Because the class method only has access to this cls argument, it can’t modify object instance state. 
That would require access to self. However, class methods can still modify class state that applies across all instances of the class.

Static Methods
The third method, MyClass.staticmethod was marked with a @staticmethod decorator to flag it as a static method.

This type of method takes neither a self nor a cls parameter (but of course it’s free to accept an arbitrary number of other parameters).

Therefore a static method can neither modify object state nor class state. 
Static methods are restricted in what data they can access - and they’re primarily a way to namespace your methods.



"""

class MyClass:
    
    #Instance Method
    def method(self):
        return 'instance method called',self
    #Class Method
    @classmethod
    def classmethod(cls):
        return 'class method called',cls
    #Static Method
    @staticmethod
    def staticmethod():
        return 'static method called'
    
    
obj=MyClass()
print(obj.method())
'''
('instance method called', <__main__.MyClass object at 0x000002473C408240>)
'''
print(MyClass.method(obj))
'''
('instance method called', <__main__.MyClass object at 0x000002473C408240>)
'''
print(obj.classmethod())
'''
('class method called', <class '__main__.MyClass'>)
'''
print(obj.staticmethod())
'''
static method called
'''
print(MyClass.classmethod())
'''
('class method called', <class '__main__.MyClass'>)
'''
print(MyClass.staticmethod())
'''
static method called
'''
print(MyClass.method())
'''
TypeError: method() missing 1 required positional argument: 'self'
'''

#Delicious Pizza Factories With @classmethod
class Pizza:
    def __init__(self,ingredients):
        self.ingredients=ingredients
        
    def __repr__(self):
        return 'Pizza(%r)' % self.ingredients
    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])
    
print(Pizza(['cheese','tomatoes']))
'''
Pizza(['cheese', 'tomatoes'])
'''
print(Pizza.margherita())
'''
Pizza(['mozzarella', 'tomatoes'])
'''
print(Pizza.prosciutto())
'''
Pizza(['mozzarella', 'tomatoes', 'ham'])
'''


#When To Use Static Methods
import math

class Pizza2:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius!r}, '
                f'{self.ingredients!r})')

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi
    
p = Pizza2(4, ['mozzarella', 'tomatoes'])
print(p)
'''
Pizza(4, ['mozzarella', 'tomatoes'])
'''
print(p.area())
'''
50.26548245743669
'''
print(Pizza2.circle_area(4))
'''
50.26548245743669
'''