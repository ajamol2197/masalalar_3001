# 1.1
numbers = [10, 20, 30, 40, 50,]

print(len(numbers))

print(numbers[2])

print(numbers.count(30))

new_roy = numbers[-2:]
print(new_roy)

summma = sum(numbers)
print(summma)


# 1.2
meva = ["apple", "banana", "cherrry"]

meva.append("kiwi")
print(meva)

meva.pop(1)
print(meva)


meva.insert(2, "peach")
print(meva)

meva.sort()
print(meva)

print(meva)


# 1.3
score = [85, 90, 78, 92, 88]

summa = sum(score)
print(summa)

sumaa = summa / 2
print(sumaa)

print(score[::-1])

print(score)

# 1.4
it = [1, 2, 2, 3, 3, 4, 1]

natija = set(it)
print(natija)

it.sort()
print(it)

print(it[1::-1])

print(len(it))

print(it)

# 1.5
a1 = [1, 3, 5]
a2 = [2, 4, 6]

a3 = a1 + a2
print(a3)

a3.sort()
print(a3)

summa = sum(a3)
print(summa)

print(a3)
