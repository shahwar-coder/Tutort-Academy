'''
>> make_it_fly_and_swim
Task:
Define a function make_it_fly_and_swim(thing) that calls thing.fly() and thing.swim(). You must not check the type of thing—just assume it has those methods and rely on duck typing.
'''

# Class 1
class Bird:
    def fly(self):
        print("Bird can fly")
    def swim(self):
        print("Bird can swim")

# Class 2
class Fish:
    def fly(self):
        print("Fish cannot fly")
    def swim(self):
        print("Fish can swim")

# Class 3 (I am putting here to also demonstarate how duck typing can fail)
class Rock:
    pass

# Function
def make_it_fly_and_swim(creature):
    """Calls fly() and swim() on any creature with those methods."""
    creature.fly()
    creature.swim()

# Objects
seagull=Bird()
salmon=Fish()
rock=Rock()

# Function Call
make_it_fly_and_swim(seagull) # some output, as behaviour present
make_it_fly_and_swim(salmon) # some output, as behaviour present
make_it_fly_and_swim(rock) # AttributeError: 'Rock' object has no attribute 'fly' (as nor expected behaiour present, hence defies 'duck typing' there)


# Perfect Solution as:
'''
- Perfect use of duck typing: no type checking, no isinstances, just method calls (expected behaviour)
'''
