import random

def num_generator():
    # returns 10 numbers between 1 and 100
    for i in range(6):
        yield random.randint(1, 100)

    # returns a 7th number between 10 and 20
    yield random.randint(10,20)

for random_number in num_generator():
       print("And the next number is... %d!" %(random_number))