import cv2
import numpy as np

# Step 1: Load the image
image = cv2.imread('I168.png')

# Step 2: Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Use thresholding to create a mask where the text is
_, mask = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY_INV)  # Assuming the text is white or light-colored

# Step 4: Dilate the mask to cover the text area fully (this step is optional, helps with small gaps)
kernel = np.ones((3, 3), np.uint8)
mask = cv2.dilate(mask, kernel, iterations=2)

# Step 5: Inpaint the image using the mask (removes the text)
inpainted_image = cv2.inpaint(image, mask, 7, cv2.INPAINT_TELEA)

# Step 6: Save the output image
cv2.imwrite('output_image_without_text.jpg', inpainted_image)

# Step 7: Display images (optional)
cv2.imshow("Original Image", image)
cv2.imshow("Inpainted Image", inpainted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
