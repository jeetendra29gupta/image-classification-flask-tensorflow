from PIL import Image

# Open an image file
img = Image.open('apple.jpg')

# Resize it to 224x224
img = img.resize((224, 224))

# Save the resized image
img.save('resized_apple.jpg')