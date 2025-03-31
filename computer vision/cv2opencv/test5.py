import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Step 1: Load the image using OpenCV
image = cv2.imread('I112.png')

# Step 2: Define the bounding box coordinates for the text area (x, y, width, height)
x, y, w, h = 100, 200, 300, 50  # Adjust these values to fit the bounding box around the text

# Step 3: Create a mask for the bounding box area (text area)
mask = np.zeros(image.shape[:2], dtype=np.uint8)
mask[y:y+h, x:x+w] = 255  # Filling the text bounding box with white in the mask

# Step 4: Inpaint the region inside the bounding box to remove the text
inpainted_image = cv2.inpaint(image, mask, 7, cv2.INPAINT_TELEA)

# Step 5: Convert the inpainted image to RGB format (for Pillow compatibility)
inpainted_image_rgb = cv2.cvtColor(inpainted_image, cv2.COLOR_BGR2RGB)

# Step 6: Use Pillow to add new text to the inpainted image
# Convert OpenCV image to PIL Image
inpainted_image_pil = Image.fromarray(inpainted_image_rgb)

# Create a drawing context
draw = ImageDraw.Draw(inpainted_image_pil)

# Specify the font and size (You may need to provide the path to a .ttf file if necessary)
font = ImageFont.truetype("arial.ttf", 30)  # Adjust font size as needed

# Define the new text and position
new_text = "Your New Text"
text_position = (x, y)  # Position where the text should go (same as bounding box top-left)

# Add the new text to the image
# draw.text(text_position, new_text, font=font, fill=(255, 255, 255))  # White text
# Add the new text to the image with black color
draw.text(text_position, new_text, font=font, fill=(0, 0, 0))  # Black text

# Step 7: Convert back to OpenCV format (BGR)
final_image = cv2.cvtColor(np.array(inpainted_image_pil), cv2.COLOR_RGB2BGR)

# Step 8: Save the final image with new text
cv2.imwrite('output_image_with_new_textt.jpg', final_image)

# (Optional) Display the final image
cv2.imshow("Inpainted Image with New Text", final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
