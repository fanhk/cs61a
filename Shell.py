# 01.py
# Numeric expressions
# pass

# Functions
# abs(-2)
# abs(2301 - 4321)

# Values
# "Go Bears"
# "Gob" + "ears"

# Objects
# Note: Download from http://composingprograms.com/shakespeare.txt
shakes = open('shakespeare.txt')
text = shakes.read().split()
print(len(text))
print(text[:25])
print(text.count('the'))
print(text.count('thou'))
print(text.count('you'))
print(text.count('forsooth'))
print(text.count(','))

# Sets
words = set(text)
print(len(words))

# Combinations
'draw'
print('draw'[0])
print({w[0] for w in words})

# Data
print('draw'[::-1])
print({w for w in words if w == w[::-1] and len(w)>4})
print({w for w in words if w[::-1] in words and len(w) == 4})
print({w for w in words if w[::-1] in words and len(w) > 6})
