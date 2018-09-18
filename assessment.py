"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
   close to
   --- Easier debugging
   --- Reuse of code  (inheritance)
   --- Flexibility
   --- data lives close to it's functionality : you don't need to know info a method uses:
       Easy to make different interchangeable types of animals .
2. What is a class?
   --- All code iplemented using a special construct

3. What is a method?
   --- a function that takes a class instance as it's first parameter
4. What is an instance in object orientation?
   --- an object that was built from a class
5. How is a class attribute different than an instance attribute?
   --- Class attributes are owned by the class itself . instance attributes belong
       to the instance and are unique
   Give an example of when you might use each.
   --- Class attributes when you have many objects that share the same traits
   --- instance attribute when you want to override the parent class


"""


# Part 2: Road Class
# #############################################################################

# Create your Road class here
class Road:
    def __init__(self, num_lanes, speed_limit):
        self.num_lanes = 2
        self.speed_limit = 25

# Instantiate Road objects here
road_1 = Road ()
  road_1.num_lanes = 2
  road_1.speed_limit = 25

road_2 = Road()
  road_2.num_lanes = 4
  road_2.num_lanes = 60

#print(road_2.numlanes)
#print(road_1.speed_limit)

# Part 3: Update Password
# #############################################################################
class User(object):
    """A user object."""

    def __init__(self, username, password):
        self.username = username
        self.password = password

    # write the update_password method here
    def update_password(self,username,password):
        if self.password == password:
            self.password = new_password
        else:
            print('Invalid password')



# Part 4: Build a Library
# #############################################################################
class Book(object):
    """A Book object."""

    def __init__(self, title, author):
        self.title = title
        self.author = author

# Create your Library class here
class Library(self, title, author):
    def __init__()
    books = []                                      #  :'-(

# Part 5: Rectangles
# #############################################################################

class Rectangle(object):
    """A rectangle object."""

    def __init__(self, length, width):
        self.length = float(length)
        self.width = float(width)

    def calculate_area(self):
        """Return the rectangle's area (length * width)."""
        return self.length * self.width


# Create the Square class here
class Square(object):
    def __init__(self,x):
        self.x = x
        self.y = x



