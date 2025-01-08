import cv2
import numpy as np

def enhance_image(image_path):
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found!")
        return None

    # Example Enhancement 1: Adjust Contrast using Histogram Equalization
    # Convert the image to Lab color space (better for contrast enhancement)
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

    # Split the LAB image into L, A, B channels
    l, a, b = cv2.split(lab_image)

    # Apply Histogram Equalization on the L channel (luminance)
    enhanced_l = cv2.equalizeHist(l)

    # Merge the enhanced L channel back with the original A and B channels
    enhanced_lab_image = cv2.merge((enhanced_l, a, b))

    # Convert the image back to BGR color space
    enhanced_image = cv2.cvtColor(enhanced_lab_image, cv2.COLOR_LAB2BGR)

    # Example Enhancement 2: Sharpen the Image
    # Define a kernel for sharpening
    kernel = np.array([[0, -1, 0],
                       [-1, 5,-1],
                       [0, -1, 0]])

    sharpened_image = cv2.filter2D(enhanced_image, -1, kernel)

    # Return the enhanced image
    return sharpened_image

# Test the function
if __name__ == "__main__":
    # Replace with your image path
    enhanced_img = enhance_image('plant-grass-flower-selected-focus-blur-background-little-bit-green-patel-wild-park-330026275.webp')
    
    if enhanced_img is not None:
        # Show the enhanced image
        cv2.imshow("Enhanced Image", enhanced_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
