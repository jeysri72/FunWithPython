import random

import random as rand

# random() - Returns a random float number between 0 and 1
print(random.random())
print(rand.random())


fruits = ['Apple','Orange', 'Banana', "Grapes", "Pear"]
# choice() - Returns a random element from the given sequence
print (rand.choice(fruits))


# sample() - Returns a given sample of a sequence
print(rand.sample(fruits, k=2)) # k is the sampling size


# shuffle() - Takes a sequence and returns the sequence in a random order
random.shuffle(fruits)
print(fruits)
