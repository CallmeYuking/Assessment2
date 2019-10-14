
"""1. Discussion Questions

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

    -1: Can store date.
    -2: Has structure that's relatively stable.
    -3: Has own smarts.


2. What is a class?

    It's a type of a thing, like a container that can store information of data.


3. What is a method?
    It's like a function defined on a class.


4. What is an instance in object orientation?

    An individual occurrence of a class. Personally, I feel if the class is like
    a framework then instances are like the bricks.


5. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

    Class attributes can share across all instances under the class but instance
    doesn't. Instance attributes take precedence over class attributes.
"""



#####################################################################

"""2. Road Class"""
class Road():
    num_lanes = 2
    speed_limit = 25

    def __init__(self, lanes, limit):
        self.lanes = lanes
        self.limit = limit


road_1 = Road(4, 60)

road_2 = Road(2, 25)

print(road_1.num_lanes)

print(road_2.num_lanes)


#####################################################################

"""3. Update Password"""

class User(object):
    """A user object."""

    def __init__(self, username, password):
        """Create a user with the given username and password."""
        self.username = username
        self.password = password

    def update_password(self, current_psw, new_psw):
        if self.password is not current_psw:
            print('Invalid password')
        elif self.password is current_psw:
            self.new_psw = self.password


#####################################################################

"""4. Build a Library"""

class Book(object):
    """A Book object."""

    def __init__(self, title, author):
        """Create a book with the given title and author."""

        self.title = title
        self.author = author
