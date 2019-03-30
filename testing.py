from classify.py import is_apple, is_rotten

a = open(apple_logo.png)
b = open(apple_w_background.jpg)
c = open(car.jpg)
d = open(cartoon_apple.jpg)
e = open(pear.jpg)
f = open(rotten_apple_1.jpg)
g = open(rotten_apple_2.jpg)

print("apple_logo:")
print(is_apple(a))
print()

print("apple_w_background:")
print(is_apple(b))
print()

print("car:")
print(is_apple(c))
print()

print("cartoon_apple:")
print(is_apple(d))
print()

print("pear:")
print(is_apple(e))
print()

print("rotten_apple_1:")
print(is_apple(f))
print()

print("rotten_apple_2:")
print(is_apple(g))
print()