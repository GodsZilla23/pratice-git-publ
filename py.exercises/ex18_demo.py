# Exercise 18 demo

#def do_nothing():
#    pass

def do_something():
    print("I did something!")

# now we can call it by its name
do_something()

def do_more_things(a, b):
    print("A IS", a, "B IS", b)

do_more_things("hello", 1)    

c = "hi"
d = 1

def do_more_thingsS(c, d):
    print("C IS:", c, "D IS:", d)

do_more_thingsS(c, d)