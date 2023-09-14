# Unit 2; Part 1: Classes in Python
# Description: This file demonstrates how to use classes in Python.
from datetime import date


# We will cover imports in Unit 3.


# --------------------------------------------------
# Section 0: Defining and instantiating classes
# Classes are defined using the class keyword. The first argument is the name of the class. The second argument is the
#   class that this class inherits from. If you do not specify a class to inherit from, it will inherit from the
#   built-in object class.
class Person:
    # The __init__() function is the constructor of the class. It is called when the class is instantiated.
    def __init__(self, name, age):
        # The self parameter is a reference to the current instance of the class, and is used to access variables that
        #   belong to the class. It does not need to be named self, you can call it whatever you like, but it has to be
        #   the first parameter of any function in the class.
        self.name = name
        self.age = age
        # Self is not a keyword in Python, it is just a naming convention. You can call it whatever you like, but it
        #   has to be the first parameter of any function in the class. It is a reference to the current instance of
        #   the class, and is used to access variables that belong to the class.

    # Functions in a class are called methods.
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def say_hello(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


# Classes are instantiated using the class name and parentheses.
person = Person("John Doe", 20)
print(person.say_hello())


# --------------------------------------------------
# Section 1: Class inheritance
# Classes can inherit from other classes. The class that inherits from another class is called the child class, and the
#   class that is inherited from is called the parent class. The child class will inherit all the methods and
#   attributes of the parent class.
class Student(Person):
    def __init__(self, name, age, major):
        # To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function.
        Person.__init__(self, name, age)
        self.major = major

    def get_major(self):
        return self.major

    def set_major(self, major):
        self.major = major

    # You can override methods from the parent class.
    def say_hello(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old. My major is {self.major}."


# Let's instantiate a Student object.
student = Student("Jane Doe", 20, "Computer Science")
print(student.say_hello())


# --------------------------------------------------
# Section 2: Class inheritance with super()
# Python also has a super() function that will make the child class inherit all the methods and attributes from its
#   parent. This will make the code more maintainable because you will not have to change the code in multiple places
#   if you change the parent class.
class Teacher(Person):
    def __init__(self, name, age, subject):
        # To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function.
        super().__init__(name, age)
        self.subject = subject

    def get_subject(self):
        return self.subject

    def set_subject(self, subject):
        self.subject = subject

    # You can override methods from the parent class.
    def say_hello(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old. I teach {self.subject}."


# Let's instantiate a Teacher object.
teacher = Teacher("Teacher Guy", 30, "Computer Science")
print(teacher.say_hello())


# --------------------------------------------------
# Section 3: Class attributes
# Classes can also have class attributes. Class attributes are attributes that are shared by all instances of the class.
#   Class attributes are defined outside of the __init__() function.
class Car:
    # Class attributes are defined outside of the __init__() function.
    wheels = 4

    def __init__(self, make, model, year):
        # Attributes are variables that belong to the class.
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        # Two underscores before and after a function name means that it is a special function. This is called the
        #   dunder method. The __str__() function is called when you use the str() function on an object.
        return f"{self.year} {self.make} {self.model}"


# --------------------------------------------------
# Section 4: Class properties
# Classes can also have properties. Properties are attributes that are accessed like attributes, but are actually
#   methods. This allows you to add logic to the getter and setter methods.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property  # This is called a decorator. It is used to modify a function or class definition.
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name == "":
            raise ValueError("Name cannot be empty.")
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            # Raise an exception if the age is negative. We will talk more about exceptions in Unit 3.
            raise ValueError("Age cannot be negative.")
        self._age = age


# --------------------------------------------------
# Section 5: PolyMorphism
#  PolyMorphism is the ability to use the same interface for different types of objects. This allows us to perform the
#   same action on different types of objects. For example, the len() function can be used on lists, tuples, and
#   dictionaries.
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_dict = {"a": 1, "b": 2, "c": 3}
len(my_list)


# We can also create our own polymorphic functions.
def add(x, y):
    return x + y


add(1, 2)
add("Hello", "World!")
add([1, 2, 3], [4, 5, 6])


# Let's add a polymorphic method to our Person class.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

    def __len__(self):
        # The __len__() function is called when you use the len() function on an object.
        return len(self.name)


person = Person("John Doe", 20)
print(len(person))


# --------------------------------------------------
# Section 6: Class methods
# Class methods are methods that are bound to the class, not an instance of the class. They are defined using the
#   @classmethod decorator.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        # This is a class method. It is bound to the class, not an instance of the class.
        # 'cls' stands for class. It's a naming convention in Python for class methods.
        return cls(name, date.today().year - birth_year)

    def say_hello(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


print(Person.from_birth_year("John Doe", 2000).age)


# --------------------------------------------------
# Section 7: Static methods
# Static methods are methods that are bound to the class, not an instance of the class. They are defined using the
#   @staticmethod decorator.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def is_adult(age):
        # This is a static method. It is bound to the class, not an instance of the class.
        return age >= 18

    def say_hello(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


print(Person.is_adult(20))


# --------------------------------------------------
# Section 8: Overloading operators
# Python allows you to overload operators. This means that you can define what happens when you use an operator on an
#   object. For example, you can define what happens when you use the + operator on two objects.
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    # Overload the '+' operator
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

# Create instances
v1 = Vector(2, 3)
v2 = Vector(1, 4)

# Use the overloaded '+' operator
print(v1 + v2)  # Outputs: (3, 7)


# Python doesn't support traditional overloading, however, you can use default arguments to simulate overloading.
class Greet:
    def hello(self, name=None):
        # Default arguments can be used to simulate overloading. In this case, the name parameter is optional.
        if name is not None:
            print(f"Hello {name}")
        else:
            print("Hello ")

# Create instance
greeting = Greet()

# Call the method
greeting.hello()

# Call the method with a parameter
greeting.hello("Alice")

# --------------------------------------------------
# Exercise 1: Create a module called `my_bus.py` in this folder and add a class named 'Bus' that has
#   the following properties:
#   - driver: Person
#   - passengers: dict(Person)
#   - seats: int
#   - standing_room: int
#   - stops: list[str]

#   The constructor should take the following parameters:
#   - driver: Person
#   - seats: int
#   - standing_room: int
#   - stops: list[str]

#   The class should have the following methods:
#   - get_driver(): Person
#   - get_passengers(): list[Person]
#   - get_seats(): int
#   - get_standing_room(): int
#   - get_stops(): list[str]
#   - add_passenger(passenger: Person): void
#   - remove_passenger(passenger: Person): void
#   - add_stop(stop: str): void
#   - remove_stop(stop: str): void
#   - get_num_passengers(): int
#   - get_num_stops(): int

#   The class should also have a __str__() method that returns a string representation of the class.

# Exercise 2: Create a class that inherits from the Bus class called 'SchoolBus' that adds the following properties:
#   - school: str
#   - bus_number: int
