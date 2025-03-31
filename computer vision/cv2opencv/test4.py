import cv2
import numpy as np

# Step 1: Load the image
image = cv2.imread('I112.png')

# Step 2: Define the bounding box coordinates for the text area (x, y, width, height)
x, y, w, h = 100, 200, 300, 50  # Adjust these values to fit the bounding box around the text

# Step 3: Create a mask for the bounding box area (text area)
mask = np.zeros(image.shape[:2], dtype=np.uint8)
mask[y:y+h, x:x+w] = 255  # Filling the text bounding box with white in the mask

# Step 4: Inpaint the region inside the bounding box to remove the text
inpainted_image = cv2.inpaint(image, mask, 7, cv2.INPAINT_TELEA)

# Step 5: Save the resulting image
cv2.imwrite('output_image_without_text3.jpg', inpainted_image)

# (Optional) Display the result
cv2.imshow("Original Image", image)
cv2.imshow("Inpainted Image", inpainted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
