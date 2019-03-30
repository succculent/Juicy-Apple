from classify import is_rotten, is_rotten
import io

with io.open("apple_logo.png", 'rb') as image_file:
	content = image_file.read()
	print("apple_logo:")
	print(is_rotten(content))
	print()

with io.open("apple_w_background.jpg", 'rb') as image_file:
	content = image_file.read()
	print("apple_w_background:")
	print(is_rotten(content))
	print()

with io.open("car.jpg", 'rb') as image_file:
	content = image_file.read()
	print("car:")
	print(is_rotten(content))
	print()

with io.open("cartoon_apple.jpg", 'rb') as image_file:
	content = image_file.read()
	print("cartoon_apple:")
	print(is_rotten(content))
	print()

with io.open("pear.jpg", 'rb') as image_file:
	content = image_file.read()
	print("pear:")
	print(is_rotten(content))
	print()

with io.open("rotten_apple_1.jpg", 'rb') as image_file:
	content = image_file.read()
	print("rotten_apple_1:")
	print(is_rotten(content))
	print()

with io.open("rotten_apple_2.jpg", 'rb') as image_file:
	content = image_file.read()
	print("rotten_apple_2:")
	print(is_rotten(content))
	print()