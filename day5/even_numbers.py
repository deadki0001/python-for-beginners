# Adding evens

evens = []
addition = 0

for num in range(1, 101):
    if num % 2 == 0:
        evens.append(num)

for even in evens:
    addition += even

print(addition)