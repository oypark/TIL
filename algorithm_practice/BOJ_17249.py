after_image = input()
face = after_image.find("(^0^)")

left = after_image[:face].count("@=")
right = after_image[face:].count("=@")

print(left, right)