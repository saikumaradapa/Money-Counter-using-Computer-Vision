import cvzone
import cv2
import numpy as np

# Preset values for the coin areas
areaOfOne = 7300
areaOfTwo = 8350
areaOfFive = 6450

# Placeholder image for the results
imgResult = np.zeros((480, 640, 3), np.uint8)

# Initialize camera capture
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Set the width
cap.set(4, 480)  # Set the height

threshold = 100

# Function for image preprocessing
def preProcessing(img):
    # Apply Gaussian blur
    imgPre = cv2.GaussianBlur(img, (5, 5), 3)
    # Detect edges using Canny edge detector
    imgPre = cv2.Canny(imgPre, 225, 120)
    kernel = np.ones((3, 3), np.uint8)
    # Dilate the image to enhance the main features
    imgPre = cv2.dilate(imgPre, kernel, iterations=1)
    # Close small holes using morphology
    imgPre = cv2.morphologyEx(imgPre, cv2.MORPH_CLOSE, kernel)
    return imgPre

# Main loop to process video frames
while True:
    k = 1  # Variable to label contours
    # Read a frame from the camera
    success, img = cap.read()
    # Process the frame
    imgPre = preProcessing(img)
    # Find contours on the processed image
    imgContours, conFound = cvzone.findContours(img, imgPre, minArea=20)

    # Variables to hold coin counts and total value
    totalMoney = 0
    nOnes, nTwos, nFives = 0, 0, 0

    # If contours are found
    if conFound:
        for contour in conFound:
            # Calculate the perimeter of each contour
            peri = cv2.arcLength(contour['cnt'], True)
            # Approximate the contour
            approx = cv2.approxPolyDP(contour['cnt'], 0.02 * peri, True)

            # Process only those contours with more than 5 vertices (likely to be coins)
            if len(approx) > 5:
                area = contour['area']
                x, y, w, h = contour['bbox']
                # Label the contour on the original image
                cvzone.putTextRect(img, str(k), (x, y), scale=2, offset=5, thickness=3)
                # Display the contour label and its area on the results image
                cvzone.putTextRect(imgResult, str(k) + ':' + str(area), (100, 50 * k), scale=2, offset=5, thickness=3)
                k += 1  # Increase the label for the next contour

    # Stack and display the images
    stacked = cvzone.stackImages([img, imgPre, imgContours, imgResult], 2, 0.5)
    cv2.imshow("stacked image", stacked)

    # Quit loop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
