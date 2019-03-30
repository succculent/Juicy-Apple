from classify import is_apple, is_rotten
import io

with io.open("apple_logo.png") as image_file:
	content = image_file.read()
	print("apple_logo:")
	print(is_apple(content))
	print()

with io.open("apple_w_background.jpg") as image_file:
	content = image_file.read()
	print("apple_w_background:")
	print(is_apple(content))
	print()

with io.open("car.jpg") as image_file:
	content = image_file.read()
	print("car:")
	print(is_apple(content))
	print()

with io.open("cartoon_apple.jpg") as image_file:
	content = image_file.read()
	print("cartoon_apple:")
	print(is_apple(content))
	print()

with io.open("pear.jpg") as image_file:
	content = image_file.read()
	print("pear:")
	print(is_apple(content))
	print()

with io.open("rotten_apple_1.jpg") as image_file:
	content = image_file.read()
	print("rotten_apple_1:")
	print(is_apple(content))
	print()

with io.open("rotten_apple_2.jpg") as image_file:
	content = image_file.read()
	print("rotten_apple_2:")
	print(is_apple(content))
	print()