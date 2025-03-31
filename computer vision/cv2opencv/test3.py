from PIL import Image

# Step 1: Load the image
image = Image.open('I112.png')

# Step 2: Define the bounding box coordinates (left, top, right, bottom)
bounding_box = (100, 200, 400, 250)  # Replace with your own bounding box coordinates

# Step 3: Get a portion of the image (background) from a nearby region
background_patch = image.crop((100, 150, 400, 200))  # Pick a nearby area that matches the background

background_patch.convert(colors='red')
# Step 4: Paste the background patch over the text area (bounding box)
image.paste(background_patch, bounding_box)

# Step 5: Save the output image
image.save('output_image_without_text.jpg')

# (Optional) Display the result
image.show()
