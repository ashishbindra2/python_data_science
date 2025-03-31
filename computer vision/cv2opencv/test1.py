from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np

# Step 1: Load the image using OpenCV
image = cv2.imread('I168.png')

# Step 2: Convert the image from BGR (OpenCV format) to RGB (Pillow format)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Step 3: Blur the entire image using Gaussian Blur
blurred_image = cv2.GaussianBlur(image, (25, 25), 0)

# Step 4: Define the region to keep sharp (text area) - Here, I'm assuming it's the center
height, width, _ = image.shape
center_x, center_y = width // 2, height // 2
text_width, text_height = 400, 200  # Adjust according to your text box size

# Create a mask for the sharp text area
mask = np.zeros_like(image_rgb)
mask[center_y - text_height // 2:center_y + text_height // 2,
     center_x - text_width // 2:center_x + text_width // 2] = image_rgb[center_y - text_height // 2:center_y + text_height // 2,
                                                                        center_x - text_width // 2:center_x + text_width // 2]

# Combine blurred background with sharp foreground (text area)
combined_image = np.where(mask != 0, mask, blurred_image)

# Step 5: Convert the image back to Pillow format for adding text
combined_image_pil = Image.fromarray(combined_image)

# Step 6: Add text using Pillow
draw = ImageDraw.Draw(combined_image_pil)
font = ImageFont.truetype("arial.ttf", 50)  # Adjust font size and path if necessary

# Define the text and position
text = "Sample Text"
text_position = (center_x - text_width // 2 + 50, center_y - text_height // 2 + 50)  # Adjust text position

# Add text to the image
draw.text(text_position, text, font=font, fill=(255, 255, 255))  # White text

# Step 7: Save the final image
combined_image_pil.save('output_image_with_text.jpg')
