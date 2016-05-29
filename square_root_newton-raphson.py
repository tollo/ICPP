# Square root using Newton-Raphsom method
# Introduction to Computation and Programming Using Python
# Find x such that x**2 - 24 is within epsilon of 0

epsilon = 0.01
k = 25.0
guess = k/2.0
numGuesses = 0

while abs(guess*guess - k) >= epsilon:
    guess = guess - (((guess**2) - k)/(2*guess))
    numGuesses += 1
print('Square root of', k, 'is about', guess)
print('Number of Guesses is ', numGuesses)
