import cv2

# Read the image (raw string for Windows path)
img = cv2.imread(
    r"C:\Users\ADHAVAN GNANASEKAR\OneDrive\Desktop\air_canvas\python\lab program\Screenshot 2025-12-17 122641.png"
)

# Check image loaded
if img is None:
    print("Error: Image not found")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Histogram Equalization
equalized = cv2.equalizeHist(gray)

# Display results
cv2.imshow("Original Grayscale Image", gray)
cv2.imshow("Histogram Equalized Image", equalized)

cv2.waitKey(0)
cv2.destroyAllWindows()
